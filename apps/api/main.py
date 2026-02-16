from fastapi import FastAPI

app = FastAPI(title="Ohjausjärjestelmä API")

@app.get("/health")
def health():
    return {"ok": True}
