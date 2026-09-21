# Project 2 - IT Incident Response Agent

## Why an agent is essential
The next step depends on observations from the previous step: incident -> service -> logs -> diagnosis -> remediation -> approval -> action -> verification.

## Safety
Execution is **simulated only**. The action tool updates local JSON state. It does not run shell commands or touch real infrastructure.

## Agents
- Incident Commander
- Triage Specialist
- Diagnosis Specialist
- Remediation Specialist

## Setup
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```
Set your real `OPENAI_API_KEY` in `.env`.

## Validate and run
```powershell
python validate_project.py
python reset_state.py
python check_setup.py
python app.py
```
Default incident: `INC-1001`.

The first turn investigates only. The program then asks you for human approval. Only after you enter `y` does the follow-up turn contain the exact token `APPROVED_BY_USER`, which the execution tool requires.

Expected controlled path for INC-1001:
`503 errors -> student-portal-api -> worker saturation -> restart_api -> approval -> simulated restart -> verify healthy`

No Ollama or localhost model is used.
