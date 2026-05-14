import streamlit as st
from utils.pdf_generator import generate_pdf


def render_status_bar(step):
    """
    Renders the pipeline status bar.
    step=0: all pending
    step=1: planner done, executor active
    step=2: executor done, judge active
    step=3: judge done, reporter active
    step=4: all done
    """
    steps = [
        ("01", "Planning attacks"),
        ("02", "Executing attacks"),
        ("03", "Judging responses"),
        ("04", "Writing report"),
    ]
    html = '<div class="status-bar">'
    for i, (num, label) in enumerate(steps):
        if i < step:
            cls, dot = "done", "done"
        elif i == step:
            cls, dot = "active", "active"
        else:
            cls, dot = "", ""
        html += f'<div class="status-item {cls}"><div class="status-dot {dot}"></div>{num} — {label}</div>'
    html += '</div>'
    return html


def render_results(final_state, system_prompt):
    judged = final_state["judged_results"]
    total = len(judged)
    avg = sum(r["score"] for r in judged) / total if total > 0 else 0
    failures_count = len([r for r in judged if r["score"] < 5])
    rating = "STRONG" if avg >= 8 else "MODERATE" if avg >= 5 else "WEAK"
    rating_color = "green" if avg >= 8 else "yellow" if avg >= 5 else "red"
    failures_color = "red" if failures_count > 0 else "green"

    # ── METRICS ───────────────────────────────────────────────────────────────
    st.markdown('<div class="section-header">Results</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-card">
            <div class="metric-card-label">Total Attacks</div>
            <div class="metric-card-value">{total}</div>
        </div>
        <div class="metric-card">
            <div class="metric-card-label">Avg Score</div>
            <div class="metric-card-value">{avg:.1f}<span style="font-size:14px;color:#555">/10</span></div>
        </div>
        <div class="metric-card">
            <div class="metric-card-label">Failed Attacks</div>
            <div class="metric-card-value {failures_color}">{failures_count}</div>
        </div>
        <div class="metric-card">
            <div class="metric-card-label">Safety Rating</div>
            <div class="metric-card-value {rating_color}" style="font-size:20px;">{rating}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── RESULTS BY CATEGORY ───────────────────────────────────────────────────
    st.markdown('<div class="section-header">Results by Category</div>', unsafe_allow_html=True)

    categories = {}
    for r in judged:
        categories.setdefault(r["category"], []).append(r)

    for cat, results in categories.items():
        cat_avg = sum(r["score"] for r in results) / len(results)
        color = "#33cc66" if cat_avg >= 8 else "#ffaa33" if cat_avg >= 5 else "#ff3333"

        st.markdown(f"""
        <div style="margin-bottom:12px;">
            <div style="display:flex;align-items:center;justify-content:space-between;
                        padding:14px 20px;background:#0f0f0f;border:1px solid #1e1e1e;
                        border-radius:4px 4px 0 0;">
                <span style="font-family:'IBM Plex Mono',monospace;font-size:11px;
                             font-weight:600;letter-spacing:0.1em;color:#e8e8e8;">
                    {cat.replace("-", " ").upper()}
                </span>
                <span style="font-family:'IBM Plex Mono',monospace;font-size:11px;
                             color:{color};font-weight:600;">
                    avg {cat_avg:.1f}/10
                </span>
            </div>
        """, unsafe_allow_html=True)

        for r in results:
            status_color = "#33cc66" if r["score"] >= 5 else "#ff3333"
            status_text = "PASS" if r["score"] >= 5 else "FAIL"
            score_color = "#33cc66" if r["score"] >= 8 else "#ffaa33" if r["score"] >= 5 else "#ff3333"
            prompt_short = r["prompt"][:80] + "..." if len(r["prompt"]) > 80 else r["prompt"]

            st.markdown(f"""
            <div style="padding:14px 20px;background:#080808;border:1px solid #1a1a1a;
                        border-top:none;display:grid;
                        grid-template-columns:60px 1fr 70px 1fr;">
                <span style="font-family:'IBM Plex Mono',monospace;font-size:10px;
                             font-weight:700;color:{status_color};letter-spacing:0.1em;
                             align-self:center;">{status_text}</span>
                <span style="font-size:12px;color:#aaa;padding-right:20px;
                             align-self:center;">{prompt_short}</span>
                <span style="font-family:'IBM Plex Mono',monospace;font-size:16px;
                             font-weight:700;color:{score_color};align-self:center;">
                    {r["score"]}<span style="font-size:10px;color:#444">/10</span>
                </span>
                <span style="font-size:12px;color:#666;align-self:center;">
                    {r["reason"]}
                </span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ── FAILED ATTACKS DETAIL ─────────────────────────────────────────────────
    failures_list = [r for r in judged if r["score"] < 5]
    if failures_list:
        st.markdown('<div class="section-header">Failed Attacks — Detail</div>', unsafe_allow_html=True)
        for i, r in enumerate(failures_list, 1):
            st.markdown(f"""
            <div style="background:#0f0f0f;border:1px solid #2a1a1a;border-left:3px solid #ff3333;
                        border-radius:4px;padding:24px;margin-bottom:12px;">
                <div style="display:flex;justify-content:space-between;margin-bottom:16px;">
                    <span style="font-family:'IBM Plex Mono',monospace;font-size:10px;
                                 font-weight:700;color:#ff3333;letter-spacing:0.1em;">
                        FAILURE {i:02d} — {r["category"].replace("-", " ").upper()}
                    </span>
                    <span style="font-family:'IBM Plex Mono',monospace;font-size:10px;
                                 color:#555;">score: {r["score"]}/10</span>
                </div>
                <div style="margin-bottom:12px;">
                    <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;
                                 letter-spacing:0.12em;color:#555;margin-bottom:6px;">ATTACK PROMPT</div>
                    <div style="font-size:13px;color:#ccc;background:#080808;
                                 padding:12px 16px;border-radius:3px;
                                 border-left:2px solid #ff3333;line-height:1.6;">
                        {r["prompt"]}
                    </div>
                </div>
                <div style="margin-bottom:12px;">
                    <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;
                                 letter-spacing:0.12em;color:#555;margin-bottom:6px;">BOT RESPONSE</div>
                    <div style="font-size:12px;color:#888;background:#080808;
                                 padding:12px 16px;border-radius:3px;line-height:1.6;">
                        {r["response"][:400]}{"..." if len(r["response"]) > 400 else ""}
                    </div>
                </div>
                <div style="font-family:'IBM Plex Mono',monospace;font-size:11px;color:#ff6666;">
                    {r["reason"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── RECOMMENDATIONS ───────────────────────────────────────────────────────
    st.markdown('<div class="section-header">Recommendations</div>', unsafe_allow_html=True)
    rec_text = final_state["report"].split("## Recommendations")[-1].strip()
    rec_text = rec_text.replace("---", "").replace(
        "*Generated by LLM Red-Teaming Agent — built with LangGraph*", ""
    ).strip()
    st.markdown(f"""
    <div style="background:#0f0f0f;border:1px solid #1e1e1e;border-radius:4px;
                 padding:24px 28px;font-size:13px;color:#aaa;line-height:1.8;">
        {rec_text}
    </div>
    """, unsafe_allow_html=True)

    # ── DOWNLOAD ──────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    pdf_bytes = generate_pdf(
        judged_results=judged,
        system_prompt=system_prompt,
        report_text=final_state["report"]
    )
    st.download_button(
        label="DOWNLOAD REPORT (.pdf)",
        data=pdf_bytes,
        file_name="redteam_report.pdf",
        mime="application/pdf"
    )