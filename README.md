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
git clone https://github.com/Harshit-3114/nexus-matcher.git
cd nexus-matcher

# 2. Install dependencies
pip install -r requirements.txt

# 3. Build the vector index from the source dataset (~2 min)
python build_index.py

# 4. Add your Gemini API key to .env
GEMINI_API_KEY=your_key_here

# 5. Launch the app
streamlit run app.py
```

## 🗂️ Dataset

The synthetic employee dataset (`dataset/cleaned_employee_llm_data.csv`) holds
**10,000 profiles** across sectors like IT, Finance, CA and Digital Marketing,
each with an `id` and a `text_for_llm` description.

Two files are **generated** from that CSV and are therefore not committed:

| File | Size | Rebuilt by |
|---|---|---|
| `dataset/employee_index.faiss` | ~15 MB | `build_index.py` |
| `dataset/employee_metadata.pkl` | ~2.8 MB | `build_index.py` |

`build_index.py` embeds every profile with `all-MiniLM-L6-v2` (384 dimensions)
and writes a flat L2 index — lower distance means a closer match, which is the
metric the app uses for the Synergy Score.

## 🎯 Usage

1. Describe your problem in the text area (e.g., *"I need to build a scalable cloud-based financial forecasting model"*)
2. Click **Find My Match**
3. Review the AI-generated dossier and synergy score
4. Approve to draft an intro email or pass to see the next match

## 📁 Project Structure

```
nexus-matcher/
├── app.py                      # Main Streamlit application
├── build_index.py              # Rebuilds the FAISS index from the source CSV
├── requirements.txt            # Python dependencies
├── .env                        # API key configuration (git-ignored)
├── dataset/
│   ├── cleaned_employee_llm_data.csv  # Source dataset (10,000 profiles)
│   ├── employee_index.faiss    # Generated - FAISS vector index
│   └── employee_metadata.pkl   # Generated - profile metadata
└── assets/                     # Static assets
```

## 📄 License

MIT — see [LICENSE](LICENSE).

