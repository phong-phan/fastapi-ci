# hello_api.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn

app = FastAPI()

@app.get("/status")
def status():
    return JSONResponse(content={"status": "ok"})

@app.get("/hello")
def hello():
    return PlainTextResponse("Welcome to my test site")
@app.get("/about")
def hello():
    return PlainTextResponse("This is a simple web site to test")

# Optional: Run with `python hello_api.py`
if __name__ == "__main__":
    uvicorn.run("hello_api:app", host="0.0.0.0", port=8000, reload=True)
