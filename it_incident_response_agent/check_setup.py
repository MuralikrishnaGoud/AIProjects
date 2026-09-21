from openai import OpenAI
from config import require_api_key,OPENAI_MODEL
def main():
    require_api_key(); r=OpenAI().responses.create(model=OPENAI_MODEL,input='Return exactly: OpenAI API connectivity PASSED'); print(r.output_text); print('Model:',OPENAI_MODEL)
if __name__=='__main__': main()
