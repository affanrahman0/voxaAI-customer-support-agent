from backend.memory.mongodb import sessions_col
from datetime import datetime

def add_message(session_id, user_id, role, content):
    sessions_col.update_one(
        {"session_id": session_id},
        {
            "$setOnInsert": {
                "session_id": session_id,
                "user_id": user_id,
                "created_at": datetime.utcnow()
            },
            "$push": {
                "messages": {
                    "role": role,
                    "content": content,
                    "timestamp": datetime.utcnow()
                }
            }
        },
        upsert=True
    )

def get_session_history(session_id, limit=6):
    session = sessions_col.find_one({"session_id": session_id})
    if not session:
        return []
    return session.get("messages", [])[-limit:]
