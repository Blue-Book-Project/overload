from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from core.orchestrator import Orchestrator
from config.settings import settings

app = App(token=settings.SLACK_BOT_TOKEN)
orchestrator = Orchestrator()

@app.command("/overlord")
def handle_overlord_command(ack, say, command):
    ack()
    user = command["user_name"]
    request = command["text"]
    
    if not request:
        say("Hey! Please provide a request. Example: `/overlord fix my login bug`")
        return
    
    say(f"⚡ *Overlord is processing your request...*\n> {request}")
    
    try:
        result = orchestrator.process(request)
        intent = result["intent"].replace("_", " ").title()
        response = result["response"]
        
        say(f"""✅ *Overlord Response*
*Intent Detected:* {intent}
*Request:* {request}

{response}
---
_Powered by Overlord AI_""")
    
    except Exception as e:
        say(f"❌ Error: {str(e)}")

@app.event("app_mention")
def handle_mention(event, say):
    text = event.get("text", "")
    request = text.split(">", 1)[-1].strip()
    
    if not request:
        say("Hey! Mention me with a request. Example: `@Overlord fix my login bug`")
        return
    
    say(f"⚡ *Processing your request...*\n> {request}")
    
    try:
        result = orchestrator.process(request)
        intent = result["intent"].replace("_", " ").title()
        response = result["response"]
        
        say(f"""✅ *Overlord Response*
*Intent:* {intent}

{response}
---
_Powered by Overlord AI_""")
    
    except Exception as e:
        say(f"❌ Error: {str(e)}")

def start_slack_bot():
    handler = SocketModeHandler(app, settings.SLACK_APP_TOKEN)
    handler.start()