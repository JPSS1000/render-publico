"""Sobe arquivos TRANCADOS pro Colab (Whisper ou rembg). Uso:
  python empacotar_colab.py <nome> <arquivo ou pasta> [mais...]
Depois o Jonathan abre o caderno colab.ipynb no Colab, escreve o <nome> e roda. O resultado baixa sozinho
na pasta Downloads do PC (colab-<nome>.zip).
"""
import os, subprocess, sys, zipfile
AQUI = os.path.dirname(os.path.abspath(__file__))
GH = r'C:\Program Files\GitHub CLI\gh.exe'
OPENSSL = r'E:\MaquinaEdicao\programas\Git\ucrt64\bin\openssl.exe'
REPO = 'JPSS1000/render-publico'
NOME, ITENS = sys.argv[1], sys.argv[2:]
pac = os.path.join(AQUI, 'pacotes'); os.makedirs(pac, exist_ok=True)
z = os.path.join(pac, f'colab-{NOME}.zip'); b = os.path.join(pac, 'pacote.bin')
with zipfile.ZipFile(z, 'w', zipfile.ZIP_STORED) as f:
    for it in ITENS:
        if os.path.isdir(it):
            for raiz, _, arqs in os.walk(it):
                for a in arqs:
                    c = os.path.join(raiz, a); f.write(c, os.path.relpath(c, it))
        else:
            f.write(it, os.path.basename(it))
env = dict(os.environ, SENHA=open(os.path.join(AQUI, '.senha'), encoding='utf8').read().strip())
subprocess.run([OPENSSL, 'enc', '-aes-256-cbc', '-pbkdf2', '-iter', '200000', '-salt', '-pass', 'env:SENHA',
                '-in', z, '-out', b], check=True, env=env)
os.remove(z)
tag = f'colab-{NOME}'
subprocess.run([GH, 'release', 'delete', tag, '-R', REPO, '-y', '--cleanup-tag'], capture_output=True)
subprocess.run([GH, 'release', 'create', tag, '-R', REPO, '-t', tag, '-n', 'entrada trancada', b], check=True)
os.remove(b)
print('subiu:', tag)
