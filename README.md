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

## Publicar

Suba a raiz do repositório em qualquer host estático (Netlify, Cloudflare Pages,
Vercel, GitHub Pages). O arquivo `_headers` já configura cache e cabeçalhos de
segurança em Netlify/Cloudflare Pages.
