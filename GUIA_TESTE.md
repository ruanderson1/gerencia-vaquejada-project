# 🎪 Guia de Teste - Vaquejada Brasil

## ✅ Sistema Pronto para Teste!

**URL:** http://127.0.0.1:8000

---

## 📝 Dados de Teste Disponíveis

### Usuários

- **Admin**: `admin` / `admin123`
- **Usuário Teste**: `teste` / `teste123`

### Vaquejada

- **Nome**: "vaquejada novo dia"
- **Data**: 04/12/2025
- **Hora**: 14:00
- **Local**: [Local da vaquejada]
- **Categorias**:
  - avançado (R$ 150,00) - 50 vagas
  - novato (R$ 100,00) - 50 vagas

### Ingresso Criado (Teste)

- **Usuário**: teste
- **Categoria**: avançado
- **Representação**: Vaqueiros do Vale
- **Puxador**: João Silva
- **Esteiro**: Pedro Santos
- **Cavalo Puxador**: Trovador
- **Cavalo Esteiro**: Relâmpago

---

## 🧪 Teste 1: Fluxo Público (Sem Login)

### Passo 1: Página Inicial

1. Acesse: http://127.0.0.1:8000/
2. Você verá cards com informações sobre o sistema
3. Botões: "Criar Conta" e "Fazer Login"

**Resultado esperado**: ✅ Página carrega corretamente com vaquejadas em cards

### Passo 2: Listar Vaquejadas

1. Clique em "Ver Vaquejadas" ou acesse: http://127.0.0.1:8000/vaquejadas/
2. Veja a lista de vaquejadas disponíveis
3. Cada card mostra: data, hora, local, descrição

**Resultado esperado**: ✅ Lista com a vaquejada "vaquejada novo dia"

### Passo 3: Detalhe da Vaquejada

1. Clique em "Ver e Comprar" em qualquer vaquejada
2. Veja informações completas
3. Categorias disponíveis com valores e vagas
4. Botão "Comprar Ingresso" aparece (mas pede login)

**Resultado esperado**: ✅ Categorias visíveis com botões de compra

---

## 👤 Teste 2: Cadastro e Login

### Passo 1: Cadastro Novo

1. Acesse: http://127.0.0.1:8000/register/
2. Preencha:
   - Usuário: seu_username
   - E-mail: seu@email.com
   - Senha: sua_senha123
   - Confirmar: sua_senha123
3. Clique em "Criar Conta"

**Resultado esperado**: ✅ Usuário criado e redirecionado para login

### Passo 2: Login

1. Acesse: http://127.0.0.1:8000/login/
2. Use credenciais:
   - Usuário: `teste` ou seu novo usuário
   - Senha: `teste123` ou sua nova senha
3. Clique em "Entrar"

**Resultado esperado**: ✅ Login bem-sucedido, redirecionado para dashboard

### Passo 3: Dashboard

1. Você verá:
   - Estatísticas: Total de Ingressos, Pagos, Pendentes
   - Botão "Novo Ingresso"
   - Tabela com seus ingressos

**Resultado esperado**: ✅ Dashboard mostra 1 ingresso (o que foi criado para teste)

---

## 🎫 Teste 3: Fluxo de Ingresso

### Passo 1: Meus Ingressos

1. No dashboard, clique em "Meus Ingressos" ou acesse: http://127.0.0.1:8000/meus-ingressos/
2. Veja os ingressos em cards
3. Status mostrado (Pendente/Pago/Cancelado)

**Resultado esperado**: ✅ 1 ingresso listado com status "Pendente"

### Passo 2: Detalhe do Ingresso

1. Clique em "Ver Detalhes"
2. Você vê:
   - Informações da vaquejada e categoria
   - Seus dados (representação, puxador, etc)
   - QR Code PIX (se gerado)
   - Opção de enviar comprovante

**Resultado esperado**: ✅ Todos os dados do ingresso visíveis

### Passo 3: Editar Ingresso

1. Clique em "Preencher Dados" ou "Editar Dados"
2. Preencha:
   - Representação: sua_representacao
   - Puxador: seu_nome
   - Esteiro: outro_nome
   - Cavalo Puxador: nome_cavalo_1
   - Cavalo Esteiro: nome_cavalo_2
3. Clique em "Salvar Informações"

**Resultado esperado**: ✅ Dados salvos e voltam para detalhe

---

## 🛠️ Teste 4: Admin

### Passo 1: Admin Login

1. Acesse: http://127.0.0.1:8000/admin/
2. Use: `admin` / `admin123`

**Resultado esperado**: ✅ Acesso ao painel admin

### Passo 2: Gerenciar Vaquejadas

1. Clique em "Vaquejadas"
2. Veja a vaquejada criada
3. Clique em editar ou criar nova

**Resultado esperado**: ✅ Lista de vaquejadas funciona

### Passo 3: Gerenciar Categorias

1. Clique em "Categorias"
2. Veja as 2 categorias criadas
3. Verifique valores e quantidades

**Resultado esperado**: ✅ Categorias listadas corretamente

### Passo 4: Gerenciar Ingressos

1. Clique em "Ingressos"
2. Veja o ingresso do usuário teste
3. Informações completas do ingresso

**Resultado esperado**: ✅ Ingresso listado com todos os dados

---

## 🎯 Teste 5: Criar Novo Ingresso (Passo a Passo)

### Como Usuário Logado:

1. No dashboard, clique "Novo Ingresso"
2. Vá para "Ver Vaquejadas"
3. Escolha uma vaquejada
4. Clique em "Ver e Comprar"
5. Selecione uma categoria com vagas disponíveis
6. Clique em "Comprar Ingresso"

**Resultado esperado**: ✅ Novo ingresso criado, redireciona para preenchimento

### Preencher Informações:

1. Preencha todos os 5 campos obrigatórios
2. Clique em "Salvar Informações"
3. Volta para detalhes do ingresso

**Resultado esperado**: ✅ Dados salvos com sucesso

---

## 🐛 Checklist de Testes

- [ ] Homepage carrega sem erros
- [ ] Listagem de vaquejadas funciona
- [ ] Detalhe de vaquejada mostra categorias
- [ ] Cadastro de novo usuário funciona
- [ ] Login funciona com credenciais corretas
- [ ] Dashboard mostra estatísticas corretas
- [ ] Meus Ingressos lista os ingressos
- [ ] Detalhe do ingresso mostra todos os dados
- [ ] Editar ingresso salva dados corretamente
- [ ] Admin acessa e mostra dados
- [ ] Criar novo ingresso funciona
- [ ] Layout é responsivo no mobile

---

## 📞 Próximas Funcionalidades

- [ ] Gerar QR Code PIX automaticamente
- [ ] Upload de comprovante de pagamento
- [ ] Relatório financeiro no admin
- [ ] Exportação para Excel/CSV
- [ ] Notificações por email
- [ ] Dashboard do organizador

---

## 🔗 URLs Úteis

| Página         | URL                                   |
| -------------- | ------------------------------------- |
| Home           | http://127.0.0.1:8000/                |
| Vaquejadas     | http://127.0.0.1:8000/vaquejadas/     |
| Meus Ingressos | http://127.0.0.1:8000/meus-ingressos/ |
| Dashboard      | http://127.0.0.1:8000/dashboard/      |
| Login          | http://127.0.0.1:8000/login/          |
| Cadastro       | http://127.0.0.1:8000/register/       |
| Admin          | http://127.0.0.1:8000/admin/          |

---

**✅ Pronto para testar!** Qualquer erro ou sugestão, avise! 🚀
