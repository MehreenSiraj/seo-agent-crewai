# SEO Agent Crew (CrewAI)

An AI-powered SEO content workflow built with **CrewAI** that automates:
- Keyword research
- SERP intent analysis
- Long-form SEO blog writing

The system outputs **editor-ready Markdown files** and keeps humans fully in control of publishing.

---

## 🚀 What This Project Does

This crew runs a **3-agent SEO pipeline**:

1. **Keyword Strategist**
   - Generates SEO-friendly keywords
   - Classifies search intent
   - Estimates difficulty

2. **Research Analyst**
   - Analyzes SERP intent
   - Extracts subtopics & user questions
   - Provides factual context

3. **SEO Writer**
   - Creates structured outlines
   - Writes long-form SEO articles (2k+ words)
   - Outputs clean Markdown

Final output is saved locally — **no auto-publishing**.

---

## 📁 Project Structure

```

seo_agent_crew/
├── src/
│   └── seo_agent_crew/
│       ├── crew.py
│       ├── main.py
│       ├── agents.yaml
│       ├── tasks.yaml
│       └── **init**.py
├── output/
│   └── seo-blog.md
├── .env
├── pyproject.toml
└── README.md

````

---

## ⚙️ Requirements

- Python **3.10+**
- Conda or virtualenv
- CrewAI **v1.7.x**
- Google Gemini API key

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
# Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
CREWAI_TRACING_ENABLED=false
````

---

## 📦 Installation

### 1️⃣ Create Environment

```bash
conda create -n crew.env python=3.10 -y
conda activate crew.env
```

### 2️⃣ Install CrewAI with Gemini Support

```bash
pip install crewai
pip install "crewai[google-genai]"
```

OR using `uv`:

```bash
uv add crewai
uv add "crewai[google-genai]"
```

---

## ▶️ Running the Crew

From the project root:

```bash
crewai run
```

This executes:

* `main.py`
* Loads agents from `agents.yaml`
* Loads tasks from `tasks.yaml`
* Runs tasks sequentially
* Saves output to:

```
output/seo-blog.md
```

---

## 🧪 Training (Optional)

```bash
crewai train 5 training.json
```

* Runs 5 iterations
* Saves learning data to `training.json`

---

## 🔁 Replay a Task

```bash
crewai replay <task_id>
```

Useful for debugging a single failed task.

---

## 🧠 Change Topic

Edit `main.py`:

```python
inputs = {
    "topic": "Agentic AI workflows for SEO",
    "current_year": "2025"
}
```

---

## 🧾 Output Files

| File                 | Purpose                       |
| -------------------- | ----------------------------- |
| `output/seo-blog.md` | Final SEO article             |
| Console logs         | Agent reasoning & task status |

---

## 🚫 What This Crew Does NOT Do

* ❌ No auto-posting
* ❌ No scraping copyrighted content
* ❌ No black-hat SEO
* ❌ No CMS access

This is **assistive AI**, not uncontrolled automation.

---

## 🛠 Common Issues

### Gemini quota error (429)

* Free tier quotas may be zero
* Switch to **Gemini 1.5 Flash**
* Or add billing in Google AI Studio

### Agent not found / config errors

* Ensure **YAML names match exactly**
* Do not reference `self.agents` manually
* Let CrewAI load configs automatically

---

## 📌 Next Improvements

* Meta title & description agent
* FAQ + schema generator
* Content quality validator
* FastAPI wrapper (internal tools)

---


## 🧾 All Commands Cheat-Sheet

### Environment
```bash
conda create -n crew.env python=3.10 -y
conda activate crew.env
````

### Install

```bash
pip install crewai
pip install "crewai[google-genai]"
```

### Run crew

```bash
crewai run
```

### Train

```bash
crewai train 5 training.json
```

### Replay task

```bash
crewai replay <task_id>
```

### Enable tracing (optional)

```bash
crewai traces enable
```

OR

```bash
export CREWAI_TRACING_ENABLED=true
```

### Check version

```bash
crewai --version
```
## 👤 Author

Built by **Mehreen Siraj**
SEO · Automation · AI Workflows

---

## 📄 License

MIT 

````

---