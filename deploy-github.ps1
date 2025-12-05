# Script PowerShell para inicializar Git e fazer upload para GitHub

$projectPath = "c:\Users\Ruanderson\OneDrive\Documentos\Estagios\CortechX\vaquejada"
Set-Location $projectPath

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Inicializando repositorio Git..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Inicializar repositório
git init

# Configurar usuário (se ainda não estiver configurado)
git config user.name "Ruanderson"
git config user.email "ruanderson@cortechx.com"

# Adicionar todos os arquivos
Write-Host "Adicionando arquivos ao repositorio..." -ForegroundColor Yellow
git add .

# Primeiro commit
Write-Host "Realizando primeiro commit..." -ForegroundColor Yellow
git commit -m "Projeto Vaquejada Brasil - Sistema completo com mapa de senhas, PIX e admin customizado"

# Exibir informações
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Repositorio Git inicializado com sucesso!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

Write-Host "Resumo:" -ForegroundColor Cyan
Write-Host "   Projeto: Vaquejada Brasil" -ForegroundColor White
Write-Host "   Localizacao: $projectPath" -ForegroundColor White
Write-Host ""

Write-Host "Status do repositorio:" -ForegroundColor Cyan
git log --oneline -1
Write-Host ""

Write-Host "========================================" -ForegroundColor Green
Write-Host "Proximos passos para upload no GitHub:" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "1. Crie um novo repositorio em:" -ForegroundColor Yellow
Write-Host "   https://github.com/new" -ForegroundColor White
Write-Host ""
Write-Host "   - Nome: vaquejada-brasil" -ForegroundColor Gray
Write-Host "   - Descricao: Sistema de gerenciamento de vaquejadas com PIX" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Execute estes comandos:" -ForegroundColor Yellow
Write-Host ""
Write-Host "   git branch -M main" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/SEU_USUARIO/vaquejada-brasil.git" -ForegroundColor White
Write-Host "   git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
