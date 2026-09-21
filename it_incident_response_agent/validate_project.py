import json
from pathlib import Path
B=Path(__file__).resolve().parent
def load(n): return json.loads((B/'data'/n).read_text(encoding='utf-8'))
def main():
    i=load('incidents.json'); s=load('services.json'); l=load('logs.json'); k=load('knowledge_base.json')
    assert any(x['incident_id']=='INC-1001' for x in i); assert any(x['service']=='student-portal-api' for x in s); assert len(l)>=4; assert len(k)>=3
    print('Project data validation: PASSED'); print(f'Incidents: {len(i)} | Services: {len(s)} | Logs: {len(l)} | KB: {len(k)}')
if __name__=='__main__': main()
