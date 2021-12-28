'''
USAGE:
python -m uvicorn app:app --port=80 --reload
'''

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def test(text: str = 'TEST'):
    return text
