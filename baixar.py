"""Baixa o video (ou os blocos) de um run do repo PUBLICO e destranca.
Uso: python baixar.py <run_id> <nome> <saida.mp4>          -> video final
     python baixar.py <run_id> <nome> <pasta> --blocos      -> so os blocos (se o juntar falhou)
"""
import glob, os, subprocess, sys, tempfile
AQUI = os.path.dirname(os.path.abspath(__file__))
GH = r'C:\Program Files\GitHub CLI\gh.exe'
OPENSSL = r'E:\MaquinaEdicao\programas\Git\ucrt64\bin\openssl.exe'
REPO = 'JPSS1000/render-publico'
RUN, NOME, SAIDA = sys.argv[1:4]
env = dict(os.environ, SENHA=open(os.path.join(AQUI, '.senha'), encoding='utf8').read().strip())
def abre(src, dst):
    subprocess.run([OPENSSL, 'enc', '-d', '-aes-256-cbc', '-pbkdf2', '-iter', '200000', '-pass', 'env:SENHA',
                    '-in', src, '-out', dst], check=True, env=env)
tmp = tempfile.mkdtemp()
if '--blocos' in sys.argv:
    subprocess.run([GH, 'run', 'download', RUN, '-R', REPO, '-p', 'bloco-*', '-D', tmp], check=True)
    os.makedirs(SAIDA, exist_ok=True)
    for f in glob.glob(os.path.join(tmp, '*', '*.bin')):
        abre(f, os.path.join(SAIDA, os.path.basename(f)[:-4] + '.mp4'))
    print('blocos em', SAIDA)
else:
    subprocess.run([GH, 'run', 'download', RUN, '-R', REPO, '-n', f'video-{NOME}', '-D', tmp], check=True)
    abre(os.path.join(tmp, 'video.bin'), SAIDA)
    print('video:', SAIDA, round(os.path.getsize(SAIDA) / 1e6, 1), 'MB')
