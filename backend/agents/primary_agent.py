from backend.utils.intent import detect_intent
from backend.utils.groq_client import groq_llm
from backend.rag.retriever import retrieve_knowledge
from backend.memory.session_repo import add_message, get_session_history
from backend.agents.order_agent import handle_order_query

def handle_query(user_id, session_id, user_query):

    add_message(session_id, user_id, "user", user_query)

    intent = detect_intent(user_query)
    history = get_session_history(session_id)

    history_text = "\n".join(
        f"{m['role']}: {m['content']}" for m in history
    )

    if user_query.strip().startswith("FK"):
        response = handle_order_query(
            order_id=user_query.strip(),
            user_id=user_id,
            intent_hint=intent
        )
    else:
        knowledge = retrieve_knowledge(user_query)

        prompt = f"""
Conversation so far:
{history_text}

Relevant support knowledge:
{chr(10).join(knowledge)}

User question:
{user_query}

Answer clearly and professionally.
"""
        response = groq_llm(prompt)

    add_message(session_id, user_id, "assistant", response)
    return response
