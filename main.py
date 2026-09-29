from fastapi import FastAPI

app = FastAPI(title="API Manutenção Industrial")

@app.get("/")
def health_check():
    return {"status": "ok"}
