"""Empacota um projeto HyperFrames (pasta edit/), TRANCA com a senha e sobe pro repo PUBLICO.
Uso: python empacotar_hf.py <pasta edit> <nome>
Depois: gh workflow run render-hyperframes.yml -R JPSS1000/render-publico -f trabalho=<nome>
"""
import os, subprocess, sys, zipfile
AQUI = os.path.dirname(os.path.abspath(__file__))
P, NOME = sys.argv[1], sys.argv[2]
GH = r'C:\Program Files\GitHub CLI\gh.exe'
OPENSSL = r'E:\MaquinaEdicao\programas\Git\ucrt64\bin\openssl.exe'
REPO = 'JPSS1000/render-publico'
FORA = {'.hyperframes', 'renders', 'node_modules', '__pycache__', 'renders-trechos'}
SENHA = open(os.path.join(AQUI, '.senha'), encoding='utf8').read().strip()
pac = os.path.join(AQUI, 'pacotes'); os.makedirs(pac, exist_ok=True)
z = os.path.join(pac, f'{NOME}.zip'); b = os.path.join(pac, 'pacote.bin')
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as f:
    for raiz, dirs, arqs in os.walk(P):
        dirs[:] = [d for d in dirs if d not in FORA]
        for a in arqs:
            if a.endswith('.py') or a.endswith('.mp4') and raiz == P: continue
            c = os.path.join(raiz, a); f.write(c, os.path.relpath(c, P))
print('pacote', round(os.path.getsize(z) / 1e6, 1), 'MB')
env = dict(os.environ, SENHA=SENHA)
subprocess.run([OPENSSL, 'enc', '-aes-256-cbc', '-pbkdf2', '-iter', '200000', '-salt', '-pass', 'env:SENHA',
                '-in', z, '-out', b], check=True, env=env)
os.remove(z)
tag = f'trabalho-{NOME}'
subprocess.run([GH, 'release', 'delete', tag, '-R', REPO, '-y', '--cleanup-tag'], capture_output=True)
subprocess.run([GH, 'release', 'create', tag, '-R', REPO, '-t', tag, '-n', 'pacote trancado', b], check=True)
os.remove(b)
print('subiu trancado:', tag)
