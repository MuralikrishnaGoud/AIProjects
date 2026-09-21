import json
from agents.decorators import tool
from services import get_student,get_role,calculate_gap,get_resources,get_project_ideas,save_markdown_report
@tool
def get_student_profile(student_id: str) -> str:
    """Retrieve the authoritative demo student profile."""
    return json.dumps(get_student(student_id),indent=2)
@tool
def get_target_role_requirements(role_name: str) -> str:
    """Retrieve required and preferred skills for a target role."""
    return json.dumps(get_role(role_name),indent=2)
@tool
def calculate_skill_gap(student_id: str, role_name: str) -> str:
    """Deterministically compare a student's skills with a target role."""
    return json.dumps(calculate_gap(student_id,role_name),indent=2)
@tool
def find_learning_resources(skill: str) -> str:
    """Find curated learning resources for one skill."""
    return json.dumps(get_resources(skill),indent=2)
@tool
def find_portfolio_projects(role_name: str) -> str:
    """Return curated portfolio projects for a role."""
    return json.dumps(get_project_ideas(role_name),indent=2)
@tool
def save_report(filename: str, markdown_content: str) -> str:
    """Save the final report as Markdown when explicitly requested."""
    return save_markdown_report(filename,markdown_content)
