# 🛡️ Pre-Deploy Guardian
**Pre-Deploy Guardian** is a production-grade **DevOps Helper Agent** that
automates and supervises the complete:
**PLAN → COOK → TEST → DELIVER**
lifecycle by making intelligent decisions *before* deployment.
It acts as a **pre-deployment safety gate**, protecting production from
unsafe releases.
---
## 🚀 What Problem It Solves
Most CI/CD tools **execute pipelines blindly**.
Pre-Deploy Guardian:
- Thinks before deployment
- Enforces quality & safety
- Blocks unsafe releases
- Rolls back failures automatically
---
## 🧠 Core Features
- Repository analysis (language & tests)
- Policy-based **ALLOW / BLOCK** decisions
- Real test execution
- Docker-based build & deploy
- Automatic rollback on runtime failure
- Deployment history & audit trail
- CLI-first, DevOps-friendly design
---
## 🏗️ Architecture
┌──────────────┐
│ CLI (Typer)│ ← guardian check / deploy / history
└──────▲───────┘
│
┌──────┴───────┐
│ Decision │
│ Engine │ ← allow / block / rollback
└──────▲───────┘
│
┌──────┴───────┐
│ Repo Analyzer│
│ Test Runner │
│ Deploy Exec │
└──────────────┘
yaml
Copy code
- **Core Engine** → decision making
- **CLI** → engineer interface
- **Docker** → consistent deployment
- **Audit Log** → governance & traceability
---
## 📦 Installation
```bash
git clone https://github.com/Saifduheenpv/pre-deploy-guardian.git
cd pre-deploy-guardian
pip install -e .
🧪 Usage
Check only (no deployment)
bash
Copy code
guardian check
Safe deploy
bash
Copy code
guardian deploy
Deployment history
bash
Copy code
guardian history
📊 Key Outcomes
✅ Prevented unsafe deployments
✅ Automated decision-making
✅ Zero-touch rollback
✅ Full audit history
✅ Real CI/CD automation
🎯 Project Status
Core Engine: ✅ Complete
CLI Tooling: ✅ Complete
Rollback & Audit: ✅ Complete
Web UI (Figma-based): ⏳ Planned
👨‍💻 Author
Saifudheen PV
Built with discipline, clarity, and real-world DevOps principles.
yaml
Copy code