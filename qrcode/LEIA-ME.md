# QR Code — Link na bio

Todos apontam para `https://farmaciabemestarsobral.com/compreaqui/`.

| Arquivo | Onde usar |
| --- | --- |
| `qrcode-compreaqui-pb.png` | Impressão em preto e branco: cupom fiscal, sacola, carimbo |
| `qrcode-compreaqui-pb.svg` | O mesmo, para gráfica (vetor, amplia sem perder qualidade) |
| `qrcode-compreaqui-azul.png` | Adesivo ou cartaz colorido, sem a cruz no meio |
| `qrcode-compreaqui-azul.svg` | O mesmo, em vetor |
| `qrcode-compreaqui-marca.png` | Versão com a cruz da farmácia no centro — balcão, vitrine |

Na dúvida, use o **preto e branco**: é o que lê melhor em impressão barata,
com pouca tinta ou em papel de baixa qualidade.

## Regras para não quebrar a leitura

- **Tamanho mínimo impresso: 2,5 cm** de lado. Abaixo disso a leitura falha em
  celular mais antigo.
- **Mantenha a margem branca** em volta (já está embutida nos arquivos). Não
  corte rente ao desenho.
- **Não estique**: ao redimensionar, segure Shift para manter quadrado.
- **Não inverta as cores** (fundo escuro com código claro): muitos leitores
  não reconhecem.

## Verificação feita

Os três arquivos foram decodificados com sucesso em tamanho original, reduzidos
a 400, 240, 160 e 120px, e com desfoque + ruído simulando foto de celular.
Nível de correção de erro **H** (30%), que é o que permite a cruz no centro
sem comprometer a leitura.

## Regerar

O script está em `qrcode/gerar.py`. Rode `python3 qrcode/gerar.py` a partir da
raiz do repositório (precisa de `segno` e `pillow`).
