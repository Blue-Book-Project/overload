# ⚡ Overload — AI Dev Agent Platform

> Inspired by Spotify's internal Honk system — built for dev teams who want to ship faster without changing how they work.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-orange)
![License](https://img.shields.io/badge/license-MIT-purple)

---

## 🚀 What is Overload?

Overload is an open source AI coding agent platform that lets developers describe what they need in plain English — directly inside **Slack** or a **web dashboard** — and get results in seconds.

Bug fixes. Code generation. Security audits. All from a simple message.

> "GPT is the engine. Overload is the car."

---

## ✨ Features

- ⚡ **Bug Fix** — describe the bug, get the fix instantly
- 🔨 **Code Generation** — describe a feature, get production-ready code
- 🔒 **Security Audit** — scan your code for vulnerabilities automatically
- 💬 **Slack Native** — works inside Slack where your team already works
- 🖥️ **Web Dashboard** — clean React-powered UI for non-Slack users
- 🤖 **Multi-model Support** — Claude, GPT, Gemini, Groq — switch with one config change
- 🔄 **API Agnostic** — never locked into one AI provider
- 📱 **Use anywhere** — send instructions while walking to the office

---

## 🏗️ Architecture
```
Developer (Slack / Dashboard)
            ↓
    FastAPI Backend
            ↓
    Orchestrator (Intent Detection)
            ↓
    AI Engine Factory
            ↓
[Claude] [GPT] [Gemini] [Groq]
```

---

## 📁 Project Structure
```
overload/
├── core/
│   ├── orchestrator.py          # Intent detection & prompt building
│   ├── slack_bot.py             # Slack bot integration
│   └── ai_engine/
│       ├── base.py              # Abstract base class
│       ├── claude.py            # Anthropic Claude
│       ├── gpt.py               # OpenAI GPT
│       ├── gemini.py            # Google Gemini
│       ├── groq_engine.py       # Groq/Llama
│       └── factory.py           # Provider selection
├── api/
│   └── router.py                # FastAPI endpoints
├── dashboard/
│   └── index.html               # React dashboard
├── demo/
│   ├── scenario1_bug_fix/       # Demo scenario 1
│   ├── scenario2_code_generation/ # Demo scenario 2
│   └── scenario3_security_audit/  # Demo scenario 3
├── config/
│   └── settings.py              # Configuration
├── main.py                      # Entry point
└── requirements.txt
```

---

## ⚡ Quick Start

**1. Clone the repo:**
```bash
git clone https://github.com/Blue-Book-Project/overload.git
cd overload
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Configure environment:**
```bash
cp .env.example .env
```

Edit `.env` with your API keys:
```env
AI_PROVIDER=groq
GROQ_API_KEY=your_key_here
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_APP_TOKEN=your_slack_app_token
```

**4. Run Overload:**
```bash
python main.py
```

**5. Open the dashboard:**
```
http://localhost:8001/dashboard
```

---

## 🤖 Supported AI Providers

| Provider | Model | Free Tier |
|---|---|---|
| Groq | Llama 3.3 70B | ✅ Yes |
| Anthropic | Claude 3.5 Sonnet | ❌ Paid |
| OpenAI | GPT-4 | ❌ Paid |
| Google | Gemini 1.5 Pro | 🟡 Limited |

**Recommended for getting started:** Groq — free, fast, powerful.

Get your free Groq API key at: `console.groq.com`

---

## 🎯 Demo Scenarios

Three ready-made demo scenarios included:

| Scenario | Description | Time Saved |
|---|---|---|
| 🔴 Bug Fix | Fix a crashing e-commerce order processor | 45 minutes |
| 🔵 Code Generation | Generate complete JWT auth system | 3 hours |
| 🟡 Security Audit | Detect and fix 8 critical vulnerabilities | $50,000 audit |

Run any scenario:
```bash
python demo/scenario1_bug_fix/broken_code.py
```

---

## 🔧 Configuration

Switch AI providers by changing one line in `.env`:
```env
AI_PROVIDER=groq      # Use Groq (free)
AI_PROVIDER=claude    # Use Anthropic Claude
AI_PROVIDER=gpt       # Use OpenAI GPT
AI_PROVIDER=gemini    # Use Google Gemini
```

---

## 🗺️ Roadmap

- [x] Core AI engine with multi-model support
- [x] Web dashboard (React)
- [x] Slack bot integration
- [x] Intent detection (bug fix, code gen, security audit)
- [ ] Phase 5 — CI/CD Integration
- [ ] Phase 6 — GitHub/GitLab repository connection
- [ ] Phase 7 — Automated testing pipeline
- [ ] Phase 8 — Sandboxed code execution
- [ ] Phase 9 — WhatsApp & Teams integration

---

## 🤝 Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 💡 Inspired By

This project was inspired by [Honk](https://nbt.substack.com/p/automate-the-entire-company) — Spotify's internal AI agent that allowed their developers to stop writing code manually.

Overload brings the same concept to any dev team — open source, free, and deployable in minutes.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🌍 Built By

Built  in 48 hours using Claude AI.

*"We don't wait for the future. We build it."*

---

⭐ If this project helped you — give it a star. It means everything.
```
