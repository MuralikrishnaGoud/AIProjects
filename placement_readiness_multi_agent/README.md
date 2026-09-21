# Project 1 - Placement Readiness Multi-Agent

## Why an agent is needed
A manager must retrieve authoritative student and role data, delegate factual gap analysis, delegate roadmap design, ask a reviewer to critique the plan, and optionally save the final report. This is more than a single prompt-response.

## Agents
- Placement Readiness Manager
- Profile Analyst
- Roadmap Coach
- Plan Reviewer

## Tools
- student profile lookup
- role requirements lookup
- deterministic skill-gap calculation
- learning-resource lookup
- portfolio-project lookup
- save report

## Setup
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```
Edit `.env`:
```env
OPENAI_API_KEY=sk-your-real-key
OPENAI_MODEL=gpt-5.6-luna
```

## Validate and run
```powershell
python validate_project.py
python check_setup.py
python app.py
```

Default request analyzes `STU-001` (Rohan Kumar) for `AI Engineer`, builds a 30-day plan, reviews it, and asks the agent to save a Markdown report.

## Demo prompts
- `Analyze STU-001 for AI Engineer and create a 30-day plan.`
- `Analyze STU-002 for Data Engineer and show the top five gaps.`
- `Compare STU-001 against Full Stack Developer and create a 45-day plan.`

## Troubleshooting
- Missing key: create `.env` from `.env.example`.
- 401: check key/project access.
- 429: check API billing/limits.
- Network/SSL: corporate network may block outbound OpenAI API traffic.
- Model not found: change `OPENAI_MODEL` to one enabled for your API project.

No Ollama or localhost model is used.
