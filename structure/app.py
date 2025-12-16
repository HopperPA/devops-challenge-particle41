from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from datetime import datetime

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root(request: Request):
    timestamp = datetime.utcnow().isoformat()
    ip = request.client.host

    response = f'''{{
  "timestamp": "{timestamp}",
  "ip": "{ip}"
}}'''

    return response
