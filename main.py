from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import llm

app = FastAPI()

class SummarizeRequest(BaseModel):
    text: str = Field(min_length=20)

class SummarizeResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummarizeResponse)
def summarize_text(request: SummarizeRequest):
    try:
        result = llm.summarize(request.text)
    except Exception:
        raise HTTPException(status_code=502, detail="The AI service failed, try again")
    return {"summary": result}
#

class TranslateRequest(BaseModel):
    text: str = Field(min_length=1)
    language: str = Field(min_length=2)

class TranslateResponse(BaseModel):
    result: str

@app.post("/translate", response_model=TranslateResponse)
def translate_text(request: TranslateRequest):
    try:
        result =llm.translate(request.text, request.language)
    except Exception:
        raise HTTPException(status_code=502, detail="The AI service failed, try again")
    return {"result":result}

class Json_translate_request(BaseModel):
    text: str = Field(min_length=10)

class Json_translate_response(BaseModel):
    title :str | None=None
    company: str | None = None
    location: str | None = None
    skills: list[str] = []

@app.post("/extract_job",response_model=Json_translate_response)
def Json_text(request: Json_translate_request):
    try:
        result =llm.extract_job(request.text)
    except Exception:
            raise HTTPException(status_code=502, detail="The AI service failed, try again")
    return result