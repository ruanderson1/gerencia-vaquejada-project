# 🤠 Vaquejada Brasil - Guia Completo do Sistema

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Instalação e Setup](#instalação-e-setup)
3. [Credenciais de Teste](#credenciais-de-teste)
4. [Funcionalidades](#funcionalidades)
5. [Fluxos de Uso](#fluxos-de-uso)
6. [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
7. [Desenvolvimento](#desenvolvimento)
8. [Deploy em Produção](#deploy-em-produção)

---

## 🎯 Visão Geral

**Vaquejada Brasil** é uma plataforma de gerenciamento de eventos de vaquejada (rodeo brasileiro) com:

- 🎫 Sistema de ingressos online
- 💳 Pagamento via PIX com QR code
- 📊 Relatórios financeiros
- 📤 Exportação de dados (Excel/CSV)
- 👤 Autenticação de usuários
- 🔐 Painel administrativo

**Tech Stack:**

- Backend: Django 4.2 + Python 3.12
- Frontend: Bootstrap 5, HTML5
- Database: SQLite (dev) / PostgreSQL (prod)
- QR Code: `qrcode` library
- Excel: `openpyxl`

---

## 🚀 Instalação e Setup

### Pré-requisitos

- Python 3.12+
- pip
- PostgreSQL (opcional, para produção)

### Passos

```bash
# 1. Clonar/extrair o projeto
cd vaquejada

# 2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas configurações

# 5. Executar migrações
python manage.py migrate

# 6. Criar superusuário (admin)
python manage.py createsuperuser

# 7. Iniciar servidor
python manage.py runserver
```

**Acesso:**

- Sistema: http://localhost:8000
- Admin: http://localhost:8000/admin

---

## 👤 Credenciais de Teste

### Usuário Administrativo

```
Usuário: admin
Senha: admin123
```

### Usuário Regular

```
Usuário: teste
Senha: teste123
```

### Dados de Teste

- **Vaquejada**: "vaquejada novo dia" (04/12/2025, 14:00)
- **Categorias**:
  - Avançado (R$ 150)
  - Novato (R$ 100)
- **Ingresso de Teste**: Já criado para usuário `teste`

---

## ✨ Funcionalidades

### 1. **Autenticação**

- ✅ Cadastro de novo usuário
- ✅ Login/Logout
- ✅ Recuperação de senha (configurável)
- ✅ Verificação de email (configurável)

### 2. **Página Pública**

- ✅ Lista de vaquejadas disponíveis
- ✅ Busca por local
- ✅ Detalhes do evento (data, hora, local)
- ✅ Categorias com preços e vagas

### 3. **Ingressos - Vaqueiro**

- ✅ Gerar ingresso (criar participação)
- ✅ Preencher dados do cavalo e participantes
- ✅ Visualizar QR code PIX
- ✅ Upload de comprovante de pagamento
- ✅ Acompanhamento de status

### 4. **QR Code PIX**

- ✅ Geração automática ao criar ingresso
- ✅ Armazenamento em `media/qrcodes/`
- ✅ Exibição na tela do ingresso
- ✅ Dados do PIX: ID único do ingresso

### 5. **Comprovante de Pagamento**

- ✅ Upload de comprovante (JPG, PNG, PDF)
- ✅ Validação de tamanho (máx 5MB)
- ✅ Armazenamento em `media/comprovantes_pix/`
- ✅ Status: "Aberto" → "Aguardando" → "Pago"

### 6. **Admin - Confirmação de Pagamentos**

- ✅ Listar ingressos por evento
- ✅ Visualizar comprovantes
- ✅ Confirmar pagamentos manualmente
- ✅ Alterar status para "Pago"

### 7. **Admin - Relatórios**

- ✅ Resumo financeiro por categoria
- ✅ Total de ingressos (pagos vs pendentes)
- ✅ Receita total do evento
- ✅ Exibição em dashboard

### 8. **Exportação de Dados**

- ✅ Excel (.xlsx) com formatação
- ✅ CSV (.csv) para importação
- ✅ Inclui: Representação, Puxador, Esteiro, Cavalo, Status, Data
- ✅ Download automático

### 9. **Painel Admin**

- ✅ Dashboard com estatísticas
- ✅ Gerenciar vaquejadas (CRUD)
- ✅ Gerenciar categorias
- ✅ Confirmação de pagamentos
- ✅ Relatórios financeiros
- ✅ Exportação de dados

---

## 🔄 Fluxos de Uso

### Fluxo do Vaqueiro (Participante)

```
1. Cadastro
   └─> Ir em "Cadastro" (no menu)
   └─> Preencher nome de usuário, email, senha
   └─> Confirmar

2. Login
   └─> Ir em "Login"
   └─> Inserir credenciais
   └─> Entrar

3. Procurar Vaquejada
   └─> Ir em "Vaquejadas Disponíveis"
   └─> Visualizar lista ou buscar por local
   └─> Clicar em "Ver e Comprar"

4. Gerar Ingresso
   └─> Escolher categoria
   └─> Clicar em "Comprar Ingresso"
   └─> Preencher dados (cavalo, participantes)
   └─> Clicar em "Gerar"

5. Fazer Pagamento
   └─> Escanear QR code com celular
   └─> Fazer o PIX (para a chave do organizador)
   └─> Copiar comprovante

6. Enviar Comprovante
   └─> Clicar em "Enviar Comprovante"
   └─> Selecionar arquivo (JPG, PNG, PDF)
   └─> Clicar em "Enviar"
   └─> Aguardar confirmação do organizador

7. Acompanhar Status
   └─> Ir em "Meus Ingressos"
   └─> Visualizar status (Aberto → Aguardando → Pago)
```

### Fluxo do Admin (Organizador)

```
1. Login
   └─> Acessar como admin/admin123

2. Criar Vaquejada
   └─> Admin → Gerenciar Vaquejadas
   └─> Clicar em "Nova Vaquejada"
   └─> Preencher: Nome, Data, Hora, Local, Descrição
   └─> Salvar

3. Criar Categorias
   └─> Entrar em Django Admin (/admin)
   └─> Ir em "Categorias"
   └─> Clicar em "Adicionar"
   └─> Preencher: Nome, Valor, Quantidade de Ingressos
   └─> Salvar

4. Acompanhar Ingressos
   └─> Admin → Vaquejadas
   └─> Clicar em "Ingressos" (em uma vaquejada)
   └─> Visualizar lista com status

5. Confirmar Pagamentos
   └─> Na tabela de ingressos, clicar em "Ver" (comprovante)
   └─> Revisar o comprovante
   └─> Clicar em "Confirmar" (botão verde)

6. Gerar Relatório
   └─> Admin → Vaquejadas
   └─> Clicar em "Financeiro" (em uma vaquejada)
   └─> Visualizar receita por categoria
   └─> Total de ingressos pagos vs pendentes

7. Exportar Dados
   └─> Na lista de ingressos
   └─> Clicar em "Excel" ou "CSV"
   └─> Arquivo será baixado automaticamente
```

---

## 🗄️ Estrutura do Banco de Dados

### Modelo: Vaquejada

```python
{
    id: UUID (chave primária),
    nome: String (max 255),
    dia: Date,
    hora: Time,
    local: String (max 255),
    descricao: Text,
    status: Choice ('open', 'closed', 'cancelled'),
    imagem: ImageField,
    criado_em: DateTime,
    atualizado_em: DateTime
}
```

### Modelo: Categoria

```python
{
    id: UUID,
    vaquejada: ForeignKey → Vaquejada,
    nome: String (max 100),
    valor: Decimal (8,2),
    n_ingressos: Integer (default 50),
    criado_em: DateTime,
    atualizado_em: DateTime
}
```

### Modelo: Ingresso

```python
{
    id: UUID,
    categoria: ForeignKey → Categoria,
    user: ForeignKey → User,
    representacao: String,
    puxador: String,
    esteiro: String,
    cavalo_puxador: String,
    cavalo_esteiro: String,
    status: Choice ('open', 'closed', 'paid', 'cancelled'),
    qr_code: ImageField (auto-gerado),
    comprovante_pix: FileField,
    criado_em: DateTime,
    pago_em: DateTime (preenchido ao confirmar)
}
```

---

## 🛠️ Desenvolvimento

### URLs Principais

```
# Públicas
GET  /                                    → Home
GET  /vaquejadas/                         → Lista de vaquejadas
GET  /vaquejadas/<id>/                    → Detalhe da vaquejada

# Autenticação
GET  /register/                           → Formulário de cadastro
POST /register/                           → Processar cadastro
GET  /login/                              → Formulário de login
POST /login/                              → Processar login
GET  /logout/                             → Logout

# Vaqueiro
GET  /dashboard/                          → Painel do vaqueiro
GET  /meus-ingressos/                     → Meus ingressos
POST /gerar-ingresso/<categoria_id>/      → Criar ingresso
GET  /ingresso/<id>/                      → Detalhe do ingresso
GET  /ingresso/<id>/editar/               → Editar ingresso
POST /ingresso/<id>/editar/               → Salvar edição
POST /ingresso/<id>/comprovante/          → Upload comprovante

# Admin
GET  /admin/dashboard/                    → Painel admin
GET  /admin/vaquejadas/                   → Gerenciar vaquejadas
GET  /admin/vaquejada/nova/               → Nova vaquejada
POST /admin/vaquejada/nova/               → Salvar vaquejada
GET  /admin/vaquejada/<id>/ingressos/     → Ingressos por evento
GET  /admin/vaquejada/<id>/relatorio/     → Relatório financeiro
GET  /admin/vaquejada/<id>/exportar-excel/ → Download Excel
GET  /admin/vaquejada/<id>/exportar-csv/  → Download CSV
POST /admin/ingresso/<id>/confirmar-pagamento/ → Confirmar pagamento
```

### Configuração (.env)

```env
# Django
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (mudar para PostgreSQL em produção)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Email (para recuperação de senha)
EMAIL_BACKEND=console (dev) ou SMTP (prod)

# Chave PIX (para referência)
PIX_KEY=chave-pix@email.com
WHATSAPP_CONTACT=55991234567
```

---

## 📦 Deploy em Produção

### Checklist Pré-Deploy

- [ ] `DEBUG=False` no .env
- [ ] `ALLOWED_HOSTS` configurado corretamente
- [ ] `SECRET_KEY` gerado e seguro
- [ ] Banco de dados PostgreSQL (não SQLite)
- [ ] Variáveis de email configuradas
- [ ] HTTPS/SSL ativo
- [ ] Coleta de arquivos estáticos (`python manage.py collectstatic`)
- [ ] Backups configurados

### Exemplo: Heroku

```bash
# 1. Instalar Heroku CLI
# 2. Login
heroku login

# 3. Criar app
heroku create vaquejada-brasil

# 4. Adicionar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# 5. Configurar variáveis
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=sua-chave

# 6. Deploy
git push heroku main

# 7. Migrar banco
heroku run python manage.py migrate

# 8. Criar superuser
heroku run python manage.py createsuperuser
```

### Exemplo: AWS/DigitalOcean/Linode

Usar `gunicorn` + `nginx`:

```bash
# requirements.txt
gunicorn==21.2.0
psycopg2-binary==2.9.9

# Iniciar
gunicorn vaquejada_project.wsgi:application --bind 0.0.0.0:8000
```

---

## 📝 Notas Importantes

1. **Backup**: Regular backups do banco de dados e arquivos (QR codes, comprovantes)
2. **Segurança**: Nunca compartilhar `SECRET_KEY` ou credenciais
3. **Email**: Configurar SMTP real para notificações aos usuários
4. **PIX**: Substituir dados de teste pelos dados reais do organizador
5. **Idioma**: Sistema totalmente em Português (BR)

---

## 🤝 Suporte

Para erros ou dúvidas:

1. Verificar logs: `python manage.py runserver`
2. Consultar erro: `http://localhost:8000/admin/`
3. Restaurar dados: `python manage.py migrate --fake-initial`

---

**Desenvolvido com ❤️ para a comunidade de vaquejada!**
