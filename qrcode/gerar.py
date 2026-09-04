# Gera os QR codes da página de link na bio.
# Rode a partir da pasta qrcode/:  python3 gerar.py
import segno
from PIL import Image, ImageDraw

URL = "https://farmaciabemestarsobral.com/compreaqui/"
AZUL = "#032EFF"          # azul exato do logo da farmácia

# error='h' -> 30% de redundância: sobra margem para o logo no centro
qr = segno.make(URL, error='h')
print("versão do QR:", qr.version, "| correção de erro:", qr.error)

# 1. Preto e branco, o mais confiável para impressão
qr.save("qrcode-compreaqui-pb.png", scale=20, border=4, dark="#000000", light="#FFFFFF")
qr.save("qrcode-compreaqui-pb.svg", scale=20, border=4, dark="#000000", light="#FFFFFF")

# 2. Azul da marca, sem logo
qr.save("qrcode-compreaqui-azul.png", scale=20, border=4, dark=AZUL, light="#FFFFFF")
qr.save("qrcode-compreaqui-azul.svg", scale=20, border=4, dark=AZUL, light="#FFFFFF")

# 3. Azul com a cruz da farmácia no centro
base = Image.open("qrcode-compreaqui-azul.png").convert("RGBA")
W, H = base.size

lado = int(W * 0.22)                       # 22% da largura: dentro da folga do nível H
cx, cy = W // 2, H // 2
r = lado // 2

# placa branca com cantos arredondados, para o leitor não confundir com módulos
placa = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
ImageDraw.Draw(placa).rounded_rectangle([0, 0, lado - 1, lado - 1], radius=int(lado * 0.18),
                                        fill="#FFFFFF")
# cruz azul dentro da placa
d = ImageDraw.Draw(placa)
b = int(lado * 0.20)                        # espessura do braço
m = int(lado * 0.22)                        # margem interna
d.rounded_rectangle([lado // 2 - b // 2, m, lado // 2 + b // 2, lado - m],
                    radius=int(b * 0.25), fill=AZUL)
d.rounded_rectangle([m, lado // 2 - b // 2, lado - m, lado // 2 + b // 2],
                    radius=int(b * 0.25), fill=AZUL)

base.alpha_composite(placa, (cx - r, cy - r))
base.convert("RGB").save("qrcode-compreaqui-marca.png", optimize=True)
print("gerados 5 arquivos")
