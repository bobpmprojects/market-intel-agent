# Market Intel Agent

One-click **competitive market intelligence** in the browser: paste a research brief, get a cited executive memo, charts, and follow-up questions.

## Quick start (this repository)

This repo includes the app inside a **Git submodule**. Clone with submodules so the code is present:

```bash
git clone --recurse-submodules https://github.com/bobpmprojects/market-intel-agent.git
cd market-intel-agent
```

**Windows (PowerShell):**

```powershell
.\run-market-intel.ps1
```

**Any OS — from this folder:**

```bash
streamlit run app.py
```

The root `app.py` forwards to the real app under `Generative-AI-Projects_bob/market-intel-agent/`.

### If the submodule folder is empty

```bash
git submodule update --init --recursive
```

---

**Full guide** (setup, keys, tabs, deploy, costs, troubleshooting):  
→ [Generative-AI-Projects_bob/market-intel-agent/README.md](Generative-AI-Projects_bob/market-intel-agent/README.md)

**Same app from the monorepo only** (no submodule): clone  
[github.com/bobpmprojects/Generative-AI-Projects_bob](https://github.com/bobpmprojects/Generative-AI-Projects_bob), then run Streamlit with main file `market-intel-agent/app.py`.
