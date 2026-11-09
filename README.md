# 🤝 Nexus: Deep Semantic Matchmaker

An AI-powered **expert matching system** that scans **10,000+ synthetic global experts** using semantic search to connect you with the right talent for your technical bottlenecks.

## 🚀 Features

- **Semantic Skill Extraction** — Gemini 2.5 Flash extracts core skills from your problem description
- **FAISS Vector Search** — Milliseconds-level similarity search across 10K expert profiles
- **Synergy Score** — Visual gauge showing match percentage based on embedding distance
- **AI Match Dossier** — Auto-generated 4-point breakdown (Why Matched, Profile, Pros, Friction)
- **Intro Email Drafting** — One-click personalized outreach email generation
- **Streamlit UI** — Clean, responsive interface with dark/light mode support

## 🧰 Tech Stack

| Component          | Technology                          |
|--------------------|-------------------------------------|
| Frontend           | Streamlit                           |
| Embedding Model    | SentenceTransformer (all-MiniLM-L6-v2) |
| Vector DB          | FAISS                               |
| LLM                | Google Gemini 2.5 Flash             |

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-org/Nexus-Matcher.git
cd Nexus-Matcher

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Gemini API key to .env
GEMINI_API_KEY=your_key_here

# 4. Launch the app
streamlit run app.py
```

## 🗂️ Dataset

The synthetic employee dataset (`dataset/`) contains **10,000+ profiles** across sectors like IT, Finance, CA, and Digital Marketing, pre-embedded and indexed with FAISS.

## 🎯 Usage

1. Describe your problem in the text area (e.g., *"I need to build a scalable cloud-based financial forecasting model"*)
2. Click **Find My Match**
3. Review the AI-generated dossier and synergy score
4. Approve to draft an intro email or pass to see the next match

## 📁 Project Structure

```
Nexus-Matcher/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # API key configuration
├── dataset/
│   ├── employee_index.faiss    # FAISS vector index
│   ├── employee_metadata.pkl   # Employee metadata
│   └── cleaned_employee_llm_data.csv  # Raw dataset
└── assets/                     # Static assets
```
