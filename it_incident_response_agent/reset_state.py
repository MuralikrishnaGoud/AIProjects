import json
from pathlib import Path
B=Path(__file__).resolve().parent/'data'
def main():
    baseline=json.loads((B/'services_baseline.json').read_text(encoding='utf-8')); (B/'services.json').write_text(json.dumps(baseline,indent=2),encoding='utf-8'); print('Demo service state reset: PASSED')
if __name__=='__main__': main()
