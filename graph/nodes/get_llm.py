def get_llm(state):
    provider = state.get("provider", "Groq")
    api_key = state.get("api_key")
    model = state["model"]

    if provider == "OpenAI":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model, api_key=api_key)
    elif provider == "Gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(model=model, google_api_key=api_key)
    else:
        from langchain_groq import ChatGroq
        return ChatGroq(model=model, api_key=api_key)