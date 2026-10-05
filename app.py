
# FastAPI
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Hugging Face
from transformers import T5ForConditionalGeneration, T5Tokenizer

# PyTorch
import torch

# Regular expression
import re

# UI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


#initalize

app = FastAPI(title="Text Summarizer App", description="Text Summarization using T5", version="1.0")

# model & tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")


#device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print("device: ", device)
model.to(device)

#templates

templates = Jinja2Templates(directory=".")

# input schema for dialogue => string
class DialogueInput(BaseModel):
    dialogue: str

def clean_data(text):
    
    if not isinstance(text, str):
        return ""
    
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    
    return text.strip()

#summary function

def summarize_dialogue(dialogue : str) -> str:
    dialogue = clean_data(dialogue) #clean

    #tokenize 
    inputs = tokenizer(
        dialogue,
        padding = "max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)
    # genrate the summary => token ids
    model.to(device)
    targets = model.generate(
        input_ids = inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )

    # toekn ids convert to summary => decodeing

    summary = tokenizer.decode(targets[0], skip_special_tokens=True) #EOS, SEP
    return summary




# API Endpoints

@app.post("/summarize/")
async def summarize(dialogue_Input: DialogueInput):
    sumamry = summarize_dialogue(dialogue_Input.dialogue)
    return {"summary":sumamry}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

