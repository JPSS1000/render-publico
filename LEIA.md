# render-publico (repo PÚBLICO, minutos grátis)
Mesmo render HyperFrames do render-nuvem, mas num repo público (Actions sem cota). Tudo que sobe ou sai fica TRANCADO (AES-256). A senha está em `.senha`, que NÃO vai pro git, e no segredo `SENHA` do repo. Quem olhar de fora vê só o código e arquivos .bin embaralhados.

1. `python E:\Automacao\render-publico\empacotar_hf.py <pasta edit> <nome>`
2. `gh workflow run render-hyperframes.yml -R JPSS1000/render-publico -f trabalho=<nome>` (padrão 20 blocos, pode usar mais)
3. `gh run list -R JPSS1000/render-publico -L 3` pra pegar o id
4. `python E:\Automacao\render-publico\baixar.py <id> <nome> <saida.mp4>`
   Se o juntar falhar: `... <id> <nome> <pasta> --blocos` e junta com ffmpeg concat.

Nunca colocar arquivo destrancado no repo, nem dar print/echo da senha no workflow.

## Colab (Whisper / rembg com GPU) — precisa do Jonathan clicar
1. `python empacotar_colab.py <nome> <arquivos ou pasta>` (sobe trancado como release colab-<nome>)
2. Jonathan abre https://colab.research.google.com/github/JPSS1000/render-publico/blob/main/colab.ipynb, põe NOME e MODO, Executar tudo.
3. Baixa `colab-<nome>.zip` na pasta Downloads: `<arquivo>.palavras.json` (palavra/ini/fim) e `.txt` no Whisper; `.png` sem fundo no rembg.
