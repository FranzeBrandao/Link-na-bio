# Farmácia Bem Estar — Link na bio

Página estática usada como link na bio do Instagram da **Farmácia Bem Estar** (Sobral/CE).

## Estrutura

```
index.html                              página (única)
assets/styles.css                       folha de estilo
assets/fonts/*.woff2                    fontes self-hosted (Schibsted Grotesk + IBM Plex Mono)
images/logo-bem-estar.png               logo com cantos transparentes, otimizado
images/logo-farmacia-bem-estar.png      logo original (fundo branco) — mantido como backup
favicon.png, robots.txt, _headers
farmacia-bem-estar-site-fundo-branco.zip   build anterior, guardado como referência
```

Sem build, sem dependências, sem JavaScript: é HTML + CSS puros.

## Links da página

| Botão | Destino |
| --- | --- |
| WhatsApp — Sinhá Sabóia (Bem Estar I) | `https://wa.me/5588997306141` |
| WhatsApp — Renato Parente (Bem Estar II) | `https://wa.me/558897172304` |
| Site da Farmácia Bem Estar | `https://farmaciabemestarsobral.com/` |

Para trocar um número ou um texto, edite apenas o `index.html`.

## Rodar localmente

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

## Publicar na Hostinger (o que está em uso)

A página fica em `https://farmaciabemestarsobral.com/compreaqui/`, numa subpasta
do site principal. O pacote pronto para subir é o `compreaqui.zip`.

1. hPanel -> **Arquivos** -> **Gerenciador de Arquivos**
2. Entre em `public_html` e crie a pasta `compreaqui`
3. Dentro dela, envie o `compreaqui.zip` e use **Extrair**
4. Apague o zip depois de extrair

O `index.html` tem que ficar em `public_html/compreaqui/index.html` — se ele cair
um nível mais fundo, a página abre sem estilo.

O `.htaccess` incluído vale só para essa pasta (cache, compressão, cabeçalhos de
segurança e a barra final em `/compreaqui`). Ele não interfere no site principal:
como `compreaqui` é uma pasta real, as regras de reescrita do site — inclusive as
do WordPress — não capturam esses endereços.

Para regerar o pacote depois de mudar algo:

```bash
rm -rf dist compreaqui.zip && mkdir dist
cp -r index.html .htaccess favicon.png assets images dist/
rm -f dist/images/logo-farmacia-bem-estar.png
(cd dist && zip -qr ../compreaqui.zip .) && rm -rf dist
```

Em outro host estático (Netlify, Cloudflare Pages, Vercel, GitHub Pages) basta
subir a raiz do repositório; nesses o `.htaccess` é ignorado e vale o `_headers`.
