# 🤖 Text Summarizer

A simple AI-powered **Text Summarization Web Application** built using **Hugging Face T5 Transformer, FastAPI, HTML, CSS, and JavaScript**.

The application allows users to enter or paste long text and generates a concise summary using a locally trained/fine-tuned T5 model.

---

## 🚀 Features

- 🤖 AI-based text summarization
- 🧠 Hugging Face T5 Transformer model
- ⚡ FastAPI backend
- 🌐 HTML, CSS, and JavaScript frontend
- 💻 Runs locally using CPU
- ✨ Clean and simple user interface
- 🔄 Real-time communication between frontend and backend
- 🧹 Basic text preprocessing
- 📦 Saved model support

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### AI / Machine Learning
- Hugging Face Transformers
- T5
- PyTorch
- SentencePiece

---

## 📂 Project Structure

```text
Text-Summarizer/
│
├── app.py
├── index.html
├── requirements.txt
├── saved_summary_model/
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   └── ...
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Text-Summarizer.git
```

### 2. Open the project folder

```bash
cd Text-Summarizer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
python -m uvicorn app:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

Open this address in your browser.

---

## 🧠 How It Works

```text
User enters text
       ↓
Frontend sends text to FastAPI
       ↓
Text preprocessing
       ↓
T5 Tokenizer
       ↓
T5 Transformer Model
       ↓
Text Generation
       ↓
Generated Summary
       ↓
Frontend displays summary
```

---

## 🔌 API Endpoint

### POST `/summarize/`

This endpoint accepts text and returns the generated summary.

### Request

```json
{
    "dialogue": "Enter your text here..."
}
```

### Response

```json
{
    "summary": "Generated summary..."
}
```

---

## 🖥️ User Interface

The application provides:

- Text input area
- Summarize button
- Processing status
- Generated summary section
- Simple AI-agent themed interface

---

## 🤖 Model

This project uses a **T5 Transformer model** for text summarization.

The trained model is loaded from:

```text
./saved_summary_model
```

The model performs inference locally using PyTorch.

---

## 🧹 Text Preprocessing

Before summarization, the application performs basic cleaning:

- Removes unnecessary whitespace
- Handles line breaks
- Removes HTML tags
- Trims unnecessary spaces

---

## 📊 Model Training

The model was trained for text summarization using a T5-based architecture.

Example training result:

```text
Training Loss:   0.608045
Validation Loss: 0.559926
```

The trained model is saved locally and loaded by the FastAPI application.

---

## 💻 Hardware

The application can run on CPU.

GPU acceleration is used when supported by the environment.

Current fallback:

```text
CPU
```

---

## 🔮 Future Improvements

- Add user authentication
- Add multiple summarization modes
- Add summary length controls
- Add document/PDF upload
- Add text file upload
- Add summarization history
- Improve model accuracy
- Deploy the application online
- Add API documentation
- Add Docker support

---

## 📌 Future Deployment

The project can be deployed using platforms such as:

- Render
- Railway
- Hugging Face Spaces
- AWS

---

## 👨‍💻 Author

**Thulasi Teja Kuruva**

B.Tech – Computer Science and Engineering  
Cyber Security

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

```text
Text Summarizer
AI + NLP + FastAPI + Hugging Face Transformers
```
