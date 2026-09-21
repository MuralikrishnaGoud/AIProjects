import json
from agents.decorators import tool
from services import get_incident,get_service,search_logs,search_kb,execute_action
@tool
def get_incident_details(incident_id: str) -> str:
    """Retrieve the authoritative incident record."""
    return json.dumps(get_incident(incident_id),indent=2)
@tool
def get_service_health(service_name: str) -> str:
    """Retrieve current health metrics for a demo service."""
    return json.dumps(get_service(service_name),indent=2)
@tool
def search_service_logs(service_name: str, keyword: str='') -> str:
    """Search recent demo logs for a service."""
    return json.dumps(search_logs(service_name,keyword),indent=2)
@tool
def search_incident_knowledge_base(query: str) -> str:
    """Search the local incident-resolution knowledge base."""
    return json.dumps(search_kb(query),indent=2)
@tool
def execute_simulated_remediation(incident_id: str, action: str, approval_token: str) -> str:
    """Execute a safe simulated action. approval_token must be exactly APPROVED_BY_USER."""
    return json.dumps(execute_action(incident_id,action,approval_token),indent=2)
