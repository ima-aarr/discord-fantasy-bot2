from aiohttp import web
import os, aiohttp
DEEPSEEK_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_BASE = os.getenv('DEEPSEEK_BASE','https://api.deepseek.com/v1')
async def chat(req):
    body=await req.json(); system=body.get('system',''); user=body.get('user',''); model=body.get('model','deepseek-chat')
    if not DEEPSEEK_KEY: return web.json_response({'error':'DEEPSEEK_KEY not set'}, status=500)
    headers={'Authorization':f'Bearer {DEEPSEEK_KEY}','Content-Type':'application/json'}
    async with aiohttp.ClientSession() as s:
        async with s.post(DEEPSEEK_BASE.rstrip('/') + '/chat/completions', headers=headers, json={'model':model,'messages':[{'role':'system','content':system},{'role':'user','content':user}], 'temperature':0.8}) as r:
            r.raise_for_status(); data=await r.json(); return web.json_response({'result': data.get('choices',[{}])[0].get('message',{}).get('content','')})
app=web.Application(); app.router.add_post('/chat', chat)
if __name__=='__main__': web.run_app(app, port=int(os.getenv('PORT','11434')))
