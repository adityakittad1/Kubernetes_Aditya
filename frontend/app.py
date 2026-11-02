from flask import Flask, jsonify, render_template_string
import os, urllib.request, json
app = Flask(__name__)
BACKEND_URL = os.getenv('BACKEND_URL', 'http://backend:3000')
PAGE = '''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Kubernetes Demo</title><style>body{font:16px system-ui;background:#f4f7fb;color:#182230;margin:0}.wrap{max-width:760px;margin:12vh auto;padding:32px;background:white;border-radius:18px;box-shadow:0 12px 40px #18334b18}h1{color:#176b87}.status{padding:16px;background:#eaf7f2;border-radius:10px;margin-top:24px}code{background:#f0f2f5;padding:3px 6px;border-radius:4px}</style></head><body><main class="wrap"><h1>Flask + Express on Kubernetes</h1><p>This page is served by the Flask frontend. It requests live data from the Express backend.</p><div class="status" id="status">Contacting backend…</div><p>Frontend endpoint: <code>/</code> · Health endpoint: <code>/healthz</code></p></main><script>fetch('/api/status').then(r=>r.json()).then(d=>{document.getElementById('status').textContent=`Backend: ${d.message} (service: ${d.service})`}).catch(()=>{document.getElementById('status').textContent='Backend is currently unavailable.'})</script></body></html>'''
@app.get('/')
def index(): return render_template_string(PAGE)
@app.get('/healthz')
def health(): return jsonify(status='ok', service='frontend')
@app.get('/api/status')
def backend_status():
    try:
        with urllib.request.urlopen(BACKEND_URL + '/api/status', timeout=3) as response:
            return (response.read(), response.status, {'Content-Type':'application/json'})
    except Exception as exc:
        return jsonify(error='backend unavailable', detail=str(exc)), 503
if __name__ == '__main__': app.run(host='0.0.0.0', port=int(os.getenv('PORT','5000')))
