from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse
from backend.agents.primary_agent import handle_query

app = FastAPI()

@app.post("/twilio/voice")
async def twilio_voice(request: Request):
    try:
        form = await request.form()

        user_speech = form.get("SpeechResult")
        call_sid = form.get("CallSid")
        caller = form.get("From")

        response = VoiceResponse()

        # FIRST TURN: user has not spoken yet
        if not user_speech:
            response.say("Hello. How can I help you today?")
            response.gather(
                input="speech",
                action="/twilio/voice",
                method="POST",
                timeout=5,
                speechTimeout="auto"
            )
            return Response(
                content=str(response),
                media_type="application/xml"
            )

        # USER SPOKE — process with AI
        ai_reply = handle_query(
            user_id=caller,
            session_id=call_sid,
            user_query=user_speech
        )

        response.say(ai_reply)
        response.gather(
            input="speech",
            action="/twilio/voice",
            method="POST",
            timeout=5,
            speechTimeout="auto"
        )

        return Response(
            content=str(response),
            media_type="application/xml"
        )

    except Exception as e:
        print("Twilio voice error:", e)

        error_response = VoiceResponse()
        error_response.say(
            "Sorry, something went wrong on our side. Please try again."
        )

        return Response(
            content=str(error_response),
            media_type="application/xml"
        )
