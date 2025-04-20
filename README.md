# 📨 Agentic Email Extractor

An intelligent, agentic AI-powered tool that reads a folder of JSON files, extracts email addresses using pattern recognition, validates them using a Large Language Model (LLM), and outputs the clean list to a `.txt` file. Built using Python and LangChain.

---

## 🚀 Features

- 📂 Reads and parses JSON files from a folder
- 📧 Extracts email-like patterns using regex
- 🧠 Uses OpenAI (via LangChain) to validate emails
- 📝 Saves unique, validated emails to a notepad (`.txt`)
- 🧱 Modular architecture with agents: `Ingest`, `Extract`, `Validate`, `Output`

---

## 🧠 Agent Architecture

| Agent Name         | Responsibility                         |
|--------------------|----------------------------------------|
| Ingest Agent       | Loads JSON files from a specified folder |
| Extraction Agent   | Extracts email addresses using regex     |
| Validation Agent   | Uses OpenAI LLM to verify valid-looking emails |
| Output Agent       | Saves final list to `output/emails.txt` |

---

## 📁 Project Structure

<img width="180" alt="Image" src="https://github.com/user-attachments/assets/d50278ec-efb3-4f74-b232-bdf0374c7948" />



---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/agentic-email-extractor.git
cd agentic-email-extractor


OPENAI_API_KEY=your-openai-key


Run the Project
Place your .json files in the data/ folder, then run:

python main.py
