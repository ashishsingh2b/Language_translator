from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from deep_translator import GoogleTranslator  # Ensure you have installed deep-translator

app = FastAPI()
templates = Jinja2Templates(directory='templates')

def translate_text(input_text, source_language, target_language):
    translator = GoogleTranslator(source=source_language, target=target_language)
    translated_text = translator.translate(input_text)
    return translated_text

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "translated_text": None})

@app.post("/", response_class=HTMLResponse)
async def translate_text_endpoint(request: Request, text_input: str = Form(...), input_language: str = Form(...), output_language: str = Form(...)):
    translated_text = translate_text(text_input, input_language, output_language)
    return templates.TemplateResponse("home.html", {"request": request, "translated_text": translated_text})
