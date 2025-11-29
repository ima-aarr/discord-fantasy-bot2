import os, aiohttp
from config import DEEPSEEK_API_KEY, DEEPSEEK_MODEL, DEEPSEEK_BASE, BOT_OWNER_ID
LLM_PROXY_URL = os.getenv('LLM_PROXY_URL')
async def call_llm(system: str, user: str, model: str = None, timeout: int = 30):
    model = model or DEEPSEEK_MODEL
    if LLM_PROXY_URL:
        async with aiohttp.ClientSession() as s:
            async with s.post(LLM_PROXY_URL + '/chat', json={'system':system,'user':user,'model':model}) as r:
                r.raise_for_status(); j=await r.json(); return j.get('result')
    if not DEEPSEEK_API_KEY:
        raise RuntimeError('DEEPSEEK_API_KEY not set')
    headers={'Authorization':f'Bearer {DEEPSEEK_API_KEY}','Content-Type':'application/json'}
    url = DEEPSEEK_BASE.rstrip('/') + '/chat/completions'
    async with aiohttp.ClientSession() as s:
        async with s.post(url, headers=headers, json={'model':model,'messages':[{'role':'system','content':system},{'role':'user','content':user}],'temperature':0.8}) as r:
            r.raise_for_status(); data=await r.json()
            if isinstance(data, dict) and 'choices' in data and data['choices']:
                return data['choices'][0]['message']['content']
            return str(data)
