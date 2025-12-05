# 📝 INSTRUÇÕES PARA ADICIONAR LOGO

## ⚠️ AÇÃO NECESSÁRIA

O arquivo `Parque kelezão.pdf` é um PDF e precisa ser convertido para imagem (PNG ou JPG).

## 🔧 COMO CONVERTER:

### Opção 1: Online (Mais Fácil)
1. Acesse: https://www.ilovepdf.com/pt/pdf_para_jpg
2. Faça upload do arquivo: `c:\Users\Ruanderson\Downloads\Parque kelezão.pdf`
3. Baixe a imagem convertida
4. Renomeie para `logo.png`
5. Copie para: `c:\Users\Ruanderson\OneDrive\Documentos\Estagios\CortechX\vaquejada\static\images\logo.png`

### Opção 2: Printscreen
1. Abra o PDF
2. Dê zoom no logo
3. Pressione `Print Screen`
4. Abra o Paint (Windows + R → `mspaint`)
5. Cole (Ctrl + V)
6. Recorte apenas o logo
7. Salve como PNG: `c:\Users\Ruanderson\OneDrive\Documentos\Estagios\CortechX\vaquejada\static\images\logo.png`

### Opção 3: Photoshop/GIMP
1. Abra o PDF no Photoshop ou GIMP
2. Exporte como PNG
3. Salve em: `c:\Users\Ruanderson\OneDrive\Documentos\Estagios\CortechX\vaquejada\static\images\logo.png`

---

## ✅ APÓS CONVERTER

1. Coloque a imagem em: `static/images/logo.png`
2. Reinicie o servidor Django
3. Acesse http://localhost:8000
4. O logo aparecerá no topo da página

---

## 🎨 O QUE FOI CONFIGURADO

- ✅ Template `base.html` atualizado para usar logo
- ✅ Fallback (ícone de cavalo) se logo não existir
- ✅ Nome mudado de "Vaquejada Brasil" para "Parque Kelezão"
- ✅ Logo no navbar com 40px de altura
- ✅ Responsivo para mobile

---

## 📂 ESTRUTURA DE ARQUIVOS

```
vaquejada/
├── static/
│   └── images/
│       └── logo.png  ← COLOQUE O LOGO AQUI
├── templates/
│   └── core/
│       └── base.html (já configurado)
```

---

## 🚨 IMPORTANTE

O logo aparecerá em **TODAS as páginas** do sistema:
- Home
- Lista de vaquejadas
- Detalhes
- Mapa de senhas
- Dashboard
- Área admin

Tamanho recomendado: **200x200px** ou **400x400px** (será redimensionado para 40px de altura)
