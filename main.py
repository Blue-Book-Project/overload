import uvicorn
import threading

def run_api():
    uvicorn.run(
        "api.router:app",
        host="0.0.0.0",
        port=8001,
        reload=False
    )

if __name__ == "__main__":
    api_thread = threading.Thread(target=run_api)
    api_thread.daemon = True
    api_thread.start()
    
    from core.slack_bot import start_slack_bot
    start_slack_bot()