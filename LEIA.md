# render-publico (repo PÚBLICO, minutos grátis)
Mesmo render HyperFrames do render-nuvem, mas num repo público (Actions sem cota). Tudo que sobe ou sai fica TRANCADO (AES-256). A senha está em `.senha`, que NÃO vai pro git, e no segredo `SENHA` do repo. Quem olhar de fora vê só o código e arquivos .bin embaralhados.

1. `python E:\Automacao\render-publico\empacotar_hf.py <pasta edit> <nome>`
2. `gh workflow run render-hyperframes.yml -R JPSS1000/render-publico -f trabalho=<nome>` (padrão 20 blocos, pode usar mais)
3. `gh run list -R JPSS1000/render-publico -L 3` pra pegar o id
4. `python E:\Automacao\render-publico\baixar.py <id> <nome> <saida.mp4>`
   Se o juntar falhar: `... <id> <nome> <pasta> --blocos` e junta com ffmpeg concat.

Nunca colocar arquivo destrancado no repo, nem dar print/echo da senha no workflow.
