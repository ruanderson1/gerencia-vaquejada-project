#!/bin/bash

# Script de Teste - Vaquejada Brasil

echo "=========================================="
echo " TESTE DO SISTEMA - VAQUEJADA BRASIL"
echo "=========================================="
echo ""

# URL base

URL="http://127.0.0.1:8000"

echo "1️⃣ Testando página inicial..."
echo " 🔗 $URL/"
echo ""

echo "2️⃣ Testando listagem de vaquejadas (público)..."
echo " 🔗 $URL/vaquejadas/"
echo ""

echo "3️⃣ Testando login..."
echo " 📧 Usuário: teste"
echo " 🔐 Senha: teste123"
echo " 🔗 $URL/login/"
echo ""

echo "4️⃣ Após login, testar dashboard..."
echo " 🔗 $URL/dashboard/"
echo ""

echo "5️⃣ Testar visualizar ingressos..."
echo " 🔗 $URL/meus-ingressos/"
echo ""

echo "6️⃣ Testar editar ingresso (preencher dados)..."
echo " 🔗 $URL/ingresso/<id>/editar/"
echo ""

echo "7️⃣ Testar admin..."
echo " 👤 Usuário: admin"
echo " 🔐 Senha: admin123"
echo " 🔗 $URL/admin/"
echo ""

echo "8️⃣ Criar nova vaquejada no admin"
echo " ✏️ Nome, Data, Hora, Local"
echo ""

echo "9️⃣ Criar categorias para a vaquejada"
echo " ✏️ Nome, Valor, Quantidade de Ingressos"
echo ""

echo "=========================================="
echo " DADOS DE TESTE DISPONÍVEIS"
echo "=========================================="
echo ""
echo "Vaquejada criada: 'vaquejada novo dia'"
echo "Categorias: 'avançado' e 'novato'"
echo "Usuário teste: teste / teste123"
echo "Usuário admin: admin / admin123"
echo ""
echo "✅ Sistema está pronto para testes!"
echo ""
