from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from graph.state import RedTeamState, AttackResult
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

load_dotenv()

def run_single_attack(llm: ChatGroq, system_prompt: str, attack: dict) -> AttackResult:
    """Send one adversarial prompt to the target bot and get its response."""
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=attack["prompt"])
    ])

    return AttackResult(
        prompt=attack["prompt"],
        category=attack["category"],
        response=response.content.strip(),
        score=0,    # judge will fill this
        reason=""   # judge will fill this
    )

def executor_node(state: RedTeamState) -> dict:
    llm = ChatGroq(
        model=state["model"],
        api_key=state.get("api_key") or os.getenv("GROQ_API_KEY")
    )

    system_prompt = state["system_prompt"]
    attack_prompts = state["attack_prompts"]
    results = []

    print(f"⚡ Executing {len(attack_prompts)} attacks in parallel...")

    # run all attacks in parallel using threads
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(run_single_attack, llm, system_prompt, attack): attack
            for attack in attack_prompts
        }

        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
                print(f"  ✅ [{result['category']}] done")
            except Exception as e:
                attack = futures[future]
                print(f"  ❌ [{attack['category']}] failed: {e}")

    return {"attack_results": results}