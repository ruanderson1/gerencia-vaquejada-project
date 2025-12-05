#!/bin/bash
# Script para inicializar Git e fazer upload para GitHub

cd "c:\Users\Ruanderson\OneDrive\Documentos\Estagios\CortechX\vaquejada"

# Inicializar repositório
git init

# Adicionar arquivo .gitignore
git add .gitignore

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "🚀 Projeto Vaquejada Brasil - Sistema completo com mapa de senhas, PIX e admin customizado"

# Exibir instruções para upload
echo ""
echo "================================================================"
echo "✅ Repositório Git inicializado com sucesso!"
echo "================================================================"
echo ""
echo "Próximos passos para fazer upload no GitHub:"
echo ""
echo "1. Crie um novo repositório em https://github.com/new"
echo "   - Nome: vaquejada-brasil"
echo "   - Descrição: Sistema de gerenciamento de vaquejadas com PIX e QR Code"
echo "   - Não adicione README, .gitignore ou license (já temos)"
echo ""
echo "2. Execute os comandos abaixo:"
echo ""
echo "   git branch -M main"
echo "   git remote add origin https://github.com/SEU_USUARIO/vaquejada-brasil.git"
echo "   git push -u origin main"
echo ""
echo "================================================================"
echo ""
echo "Resumo dos arquivos commited:"
git log --oneline -1
echo ""
echo "Total de arquivos:"
git ls-files | wc -l
echo ""
