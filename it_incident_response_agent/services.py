import json
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent; DATA_DIR=BASE_DIR/'data'
def _load(name): return json.loads((DATA_DIR/name).read_text(encoding='utf-8'))
def _write(name,value): (DATA_DIR/name).write_text(json.dumps(value,indent=2),encoding='utf-8')
def get_incident(incident_id):
    for x in _load('incidents.json'):
        if x['incident_id'].lower()==incident_id.lower(): return x
    raise ValueError(f'Unknown incident_id: {incident_id}')
def get_service(service_name):
    for x in _load('services.json'):
        if x['service'].lower()==service_name.lower(): return x
    raise ValueError(f'Unknown service: {service_name}')
def search_logs(service_name,keyword=''):
    rows=[x for x in _load('logs.json') if x['service'].lower()==service_name.lower()]
    if keyword.strip():
        q=keyword.lower(); rows=[x for x in rows if q in x['message'].lower() or q in x['level'].lower()]
    return rows[-10:]
def search_kb(query):
    terms=[x for x in query.lower().replace('-',' ').split() if len(x)>2]; scored=[]
    for item in _load('knowledge_base.json'):
        text=' '.join([item['title'],item['symptoms'],item['resolution']]).lower(); score=sum(t in text for t in terms)
        if score: scored.append((score,item))
    scored.sort(key=lambda x:x[0],reverse=True); return [x[1] for x in scored[:5]]
ALLOWED_ACTIONS={'restart_api','clear_cache','rotate_connection_pool'}
def execute_action(incident_id,action,approval_token):
    if approval_token!='APPROVED_BY_USER': return {'status':'REJECTED','reason':'Human approval token missing.'}
    if action not in ALLOWED_ACTIONS: return {'status':'REJECTED','reason':f'Unsupported action: {action}'}
    inc=get_incident(incident_id); expected=inc['recommended_demo_action']
    if action!=expected: return {'status':'REJECTED','reason':f"Controlled demo allows '{expected}' for this incident."}
    services=_load('services.json'); target=next(x for x in services if x['service']==inc['service'])
    target['status']='healthy'; target['latency_ms']=target['normal_latency_ms']; target['error_rate_percent']=0.2; target['last_action']=action; _write('services.json',services)
    return {'status':'EXECUTED','incident_id':incident_id,'service':inc['service'],'action':action,'new_service_status':'healthy'}
