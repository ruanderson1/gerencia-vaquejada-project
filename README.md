# 🐴 Vaquejada Brasil - Plataforma de Inscrições

Uma plataforma web completa para gerenciamento de inscrições em vaquejadas, com pagamento via PIX, geração de QR codes e painel administrativo.

## ✨ Funcionalidades

### Para Vaqueiros (Usuários)

- ✅ Cadastro simples e login
- ✅ Visualizar lista pública de vaquejadas
- ✅ Ver detalhes de cada evento
- ✅ Gerar senhas com QR Code PIX
- ✅ Visualizar QR Code para pagamento
- ✅ Enviar comprovante de pagamento
- ✅ Preencher dados de inscrição
- ✅ Dashboard pessoal com histórico de senhas

### Para Administradores

- ✅ Painel de controle administrativo
- ✅ CRUD completo de vaquejadas
- ✅ Cadastro de categorias por evento
- ✅ Visualizar todas as inscrições
- ✅ Gerenciar status de pagamentos
- ✅ Relatório financeiro por vaquejada
- ✅ Exportação para Excel e CSV
- ✅ Acesso ao Django Admin

## 🛠️ Stack Tecnológico

- **Backend**: Django 4.2 (Python)
- **Banco de Dados**: SQLite (dev) / PostgreSQL (produção)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Geração de QR Code**: qrcode + PIL
- **Exportação**: openpyxl (Excel), csv (CSV)

## 🚀 Instalação Rápida

```powershell
# 1. Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar migrações
python manage.py migrate

# 4. Criar superuser
python manage.py createsuperuser
# ou use: admin / admin123

# 5. Iniciar servidor
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000**

## 📖 Como Usar

### Para Vaqueiros

1. Cadastre-se → Login → Encontre vaquejada → Gere senha → Pague PIX → Preencha dados → Confirme

### Para Admin

1. Login com credenciais de superuser
2. Acesse: **http://127.0.0.1:8000/admin/**
3. Crie vaquejadas e categorias
4. Visualize inscrições e confirme pagamentos
5. Exporte relatórios

## 🗂️ Modelos

- **Vaquejada**: Eventos de vaquejada
- **Categoria**: Duplas/categorias com vagas e preço
- **Senha**: Inscrição gerada com QR Code PIX
- **Inscricao**: Dados completos do participante
- **Pagamento**: Status do pagamento via PIX

## 🔧 Configuração Avançada

### Usar PostgreSQL

Edite `.env`:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=vaquejada_db
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

Execute: `python manage.py migrate`

## 📱 URLs Principais

- `/` - Home
- `/register/` - Cadastro
- `/login/` - Login
- `/vaquejadas/` - Lista vaquejadas
- `/dashboard/` - Meu dashboard
- `/minhas-senhas/` - Minhas senhas
- `/admin/` - Painel administrativo

## 📞 Contato

WhatsApp: https://wa.me/55{{ WHATSAPP_CONTACT }}

---

**Desenvolvido com ❤️ para vaqueiros do Brasil**

Banco de dados: PostgreSQL (configure em `.env`).
