from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from translator import SentenceLaunderer
import uvicorn

app = FastAPI(
    title="Sentence Laundry API",
    description="A Sentence Laundry Machine that spins your text through multiple languages.",
    version="1.1.0"
)

# Use the cleaner name 'launderer' instead of 'villain'
launderer = SentenceLaunderer()

class LaundryRequest(BaseModel):
    text: str
    chain: Optional[List[str]] = None
    random_count: Optional[int] = 0

@app.post("/wash")
def wash_text(request: LaundryRequest):
    """
    Washes (translates) text through a specified or default chain of languages.
    """
    result = launderer.wash_loop(request.text, request.chain, 0)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.post("/random-spin")
def random_spin(request: LaundryRequest):
    """
    Washes text through a random selection of languages (Random Spin).
    Ignores 'chain' parameter, uses 'random_count' (default 2 if 0).
    """
    count = request.random_count if request.random_count > 0 else 2
    result = launderer.wash_loop(request.text, chain=None, random_count=count)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.get("/")
def read_root():
    return {"message": "Welcome to Sentence Laundry. Use POST /wash or /random-spin."}

if __name__ == "__main__":
    import os
    # Use PORT environment variable (injected by OpenSeal) or default to 8001
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
