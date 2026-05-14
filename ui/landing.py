import streamlit as st


def render_landing():
    st.markdown('<div class="section-header">How it works</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="pipeline">
        <div class="pipeline-step">
            <div class="pipeline-step-num">01 / PLAN</div>
            <div class="pipeline-step-title">Attack Planner</div>
            <div class="pipeline-step-desc">Generates 10 adversarial prompts across jailbreak, out-of-scope, prompt injection, and social engineering categories</div>
        </div>
        <div class="pipeline-step">
            <div class="pipeline-step-num">02 / EXECUTE</div>
            <div class="pipeline-step-title">Parallel Executor</div>
            <div class="pipeline-step-desc">Fires all 10 prompts at the target bot simultaneously using ThreadPoolExecutor with 5 parallel workers</div>
        </div>
        <div class="pipeline-step">
            <div class="pipeline-step-num">03 / JUDGE</div>
            <div class="pipeline-step-title">LLM-as-Judge</div>
            <div class="pipeline-step-desc">Scores each bot response 0–10 with a one-sentence justification. Parallel execution across all responses</div>
        </div>
        <div class="pipeline-step">
            <div class="pipeline-step-num">04 / REPORT</div>
            <div class="pipeline-step-title">Report Writer</div>
            <div class="pipeline-step-desc">Compiles scores, failure analysis, and actionable recommendations into a downloadable PDF report</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">Attack Categories</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    cats = [
        ("Jailbreak", "Roleplay, hypotheticals, and authority claims designed to make the bot ignore its instructions"),
        ("Out-of-Scope", "Subtle, indirect requests that fall outside the bot's defined purpose"),
        ("Prompt Injection", "Developer or admin authority claims attempting to override the system prompt"),
        ("Social Engineering", "Emotional manipulation, urgency, and pressure tactics"),
    ]
    for col, (title, desc) in zip([c1, c2, c3, c4], cats):
        with col:
            st.markdown(f"""
            <div style="background:#0f0f0f;border:1px solid #1e1e1e;border-radius:4px;padding:18px 20px;">
                <div style="font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:600;
                            color:#ff3333;letter-spacing:0.1em;margin-bottom:8px;">{title.upper()}</div>
                <div style="font-size:12px;color:#666;line-height:1.6;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)