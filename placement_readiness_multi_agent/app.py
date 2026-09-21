from agents import Runner
from config import require_api_key
from agents_app import placement_manager

DEFAULT_REQUEST = (
    "Analyze STU-001 for the AI Engineer role. Use the profile analyst, roadmap coach, "
    "and reviewer. Create a practical 30-day plan with two portfolio projects. "
    "Save the final report as rohan_ai_engineer_plan.md."
)


def main() -> None:
    require_api_key()
    print("=" * 72)
    print("PLACEMENT READINESS MULTI-AGENT")
    print("=" * 72)
    print("Default demo request:")
    print(DEFAULT_REQUEST)
    print()

    user_input = input("Press Enter for default, or type your own request:\n> ").strip()
    request = user_input or DEFAULT_REQUEST

    print("\nRunning agent workflow...\n")
    result = Runner.run_sync(placement_manager, request)

    print("=" * 72)
    print("FINAL RESPONSE")
    print("=" * 72)
    print(result.final_output)
    print()
    print(f"Final agent: {result.last_agent.name}")


if __name__ == "__main__":
    main()
