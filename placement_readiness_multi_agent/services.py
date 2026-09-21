import json
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent
DATA_DIR=BASE_DIR/'data'; OUTPUT_DIR=BASE_DIR/'outputs'; OUTPUT_DIR.mkdir(exist_ok=True)
def _load(name):
    return json.loads((DATA_DIR/name).read_text(encoding='utf-8'))
def get_student(student_id):
    for s in _load('students.json'):
        if s['student_id'].lower()==student_id.lower(): return s
    raise ValueError(f'Unknown student_id: {student_id}')
def get_role(role_name):
    roles=_load('roles.json')
    for r in roles:
        if r['role'].lower()==role_name.lower(): return r
    raise ValueError('Unknown role. Available: '+', '.join(x['role'] for x in roles))
def calculate_gap(student_id, role_name):
    s=get_student(student_id); r=get_role(role_name); owned={x.lower() for x in s['skills']}
    req=r['required_skills']; pref=r.get('preferred_skills',[])
    return {'student_id':student_id,'student_name':s['name'],'target_role':r['role'],
      'required_match_percent':round(100*sum(x.lower() in owned for x in req)/max(len(req),1),1),
      'matched_required':[x for x in req if x.lower() in owned],
      'missing_required':[x for x in req if x.lower() not in owned],
      'matched_preferred':[x for x in pref if x.lower() in owned],
      'missing_preferred':[x for x in pref if x.lower() not in owned]}
def get_resources(skill):
    rows=_load('learning_resources.json'); q=skill.lower()
    exact=[x for x in rows if x['skill'].lower()==q]
    return exact or [x for x in rows if q in x['skill'].lower() or x['skill'].lower() in q]
def get_project_ideas(role_name): return get_role(role_name).get('portfolio_projects',[])
def save_markdown_report(filename, content):
    safe=filename.strip(); safe=safe if safe.endswith('.md') else safe+'.md'
    if not all(ch.isalnum() or ch in '._-' for ch in safe): raise ValueError('Unsafe filename')
    path=OUTPUT_DIR/safe; path.write_text(content,encoding='utf-8'); return str(path)
