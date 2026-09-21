from agents import Runner
from config import require_api_key
from agents_app import incident_commander

DEFAULT_INCIDENT = "INC-1001"


def main() -> None:
    require_api_key()
    print("=" * 72)
    print("IT INCIDENT RESPONSE AGENT")
    print("=" * 72)

    incident_id = input(f"Incident ID [{DEFAULT_INCIDENT}]: ").strip() or DEFAULT_INCIDENT

    first_request = (
        f"Investigate incident {incident_id}. Triage it, diagnose the likely cause, "
        "and recommend the safest remediation. Do NOT execute any remediation in this turn."
    )

    print("\nPhase 1: investigation and recommendation...\n")
    first = Runner.run_sync(incident_commander, first_request)
    print(first.final_output)

    approval = input("\nApprove the recommended SIMULATED remediation? (y/n): ").strip().lower()
    if approval != "y":
        print("\nNo action executed. Demo ended at the human approval checkpoint.")
        return

    followup = (
        f"APPROVED_BY_USER. Execute the safest supported remediation you recommended for {incident_id}. "
        "Use approval_token exactly APPROVED_BY_USER, then verify service health."
    )

    history = first.to_input_list()
    history.append({"role": "user", "content": followup})

    print("\nPhase 2: approved simulated remediation and verification...\n")
    second = Runner.run_sync(incident_commander, history)

    print("=" * 72)
    print("FINAL RESPONSE")
    print("=" * 72)
    print(second.final_output)
    print()
    print(f"Final agent: {second.last_agent.name}")


if __name__ == "__main__":
    main()
