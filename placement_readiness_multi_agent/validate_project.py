import json
from pathlib import Path
B=Path(__file__).resolve().parent
def load(n): return json.loads((B/'data'/n).read_text(encoding='utf-8'))
def main():
    s=load('students.json'); r=load('roles.json'); x=load('learning_resources.json')
    assert any(i['student_id']=='STU-001' for i in s); assert any(i['role']=='AI Engineer' for i in r); assert len(x)>=5
    print('Project data validation: PASSED'); print(f'Students: {len(s)} | Roles: {len(r)} | Resources: {len(x)}')
if __name__=='__main__': main()
