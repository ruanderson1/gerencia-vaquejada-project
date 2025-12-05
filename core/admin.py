from django.contrib import admin
from django.utils.html import format_html
from .models import Vaquejada, Categoria, Ingresso


@admin.register(Vaquejada)
class VaquejadaAdmin(admin.ModelAdmin):
    list_display = ('nome_display', 'dia_display', 'hora', 'local', 'status_badge', 'categorias_count')
    list_filter = ('status', 'dia')
    search_fields = ('nome', 'local')
    date_hierarchy = 'dia'
    
    fieldsets = (
        ('🎯 Informações Principais', {
            'fields': ('nome', 'dia', 'hora', 'local'),
            'description': 'Dados básicos do evento'
        }),
        ('📝 Descrição', {
            'fields': ('descricao',)
        }),
        ('🖼️ Imagem do Evento', {
            'fields': ('imagem',)
        }),
        ('⚙️ Status', {
            'fields': ('status',)
        }),
    )
    
    def nome_display(self, obj):
        return f"🎪 {obj.nome}"
    nome_display.short_description = 'Vaquejada'
    
    def dia_display(self, obj):
        return obj.dia.strftime('%d/%m/%Y')
    dia_display.short_description = 'Data'
    
    def status_badge(self, obj):
        colors = {'open': '#28a745', 'closed': '#ffc107', 'cancelled': '#dc3545'}
        labels = {'open': 'Aberta', 'closed': 'Fechada', 'cancelled': 'Cancelada'}
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold;">{}</span>',
            colors.get(obj.status, '#6c757d'),
            labels.get(obj.status, obj.status)
        )
    status_badge.short_description = 'Status'
    
    def categorias_count(self, obj):
        count = obj.categorias.count()
        return f"📂 {count} categoria{'s' if count != 1 else ''}"
    categorias_count.short_description = 'Categorias'


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_display', 'vaquejada', 'valor_display', 'senhas_status')
    list_filter = ('vaquejada',)
    search_fields = ('nome', 'vaquejada__nome')
    readonly_fields = ('criado_em', 'atualizado_em', 'ingressos_disponiveis_display')
    
    fieldsets = (
        ('🎪 Vaquejada', {
            'fields': ('vaquejada',)
        }),
        ('📋 Categoria', {
            'fields': ('nome',)
        }),
        ('💰 Valor', {
            'fields': ('valor',)
        }),
        ('🎫 Senhas', {
            'fields': ('n_ingressos', 'ingressos_disponiveis_display')
        }),
        ('📅 Datas', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    def nome_display(self, obj):
        return f"📂 {obj.nome}"
    nome_display.short_description = 'Categoria'
    
    def valor_display(self, obj):
        return f"R$ {obj.valor}"
    valor_display.short_description = 'Valor'
    
    def ingressos_disponiveis_display(self, obj):
        disponivel = obj.ingressos_disponiveis()
        color = '#28a745' if disponivel > 0 else '#dc3545'
        return format_html(
            '<strong style="color: {}; font-size: 1.2em;">{} de {}</strong>',
            color,
            disponivel,
            obj.n_ingressos
        )
    ingressos_disponiveis_display.short_description = 'Senhas Disponíveis'
    
    def senhas_status(self, obj):
        disponivel = obj.ingressos_disponiveis()
        vendidas = obj.n_ingressos - disponivel
        return format_html(
            '<div style="font-size: 0.9em;"><span style="color: #28a745;">✓ {} disp.</span> | <span style="color: #dc3545;">✗ {} vend.</span></div>',
            disponivel,
            vendidas
        )
    senhas_status.short_description = 'Status'


@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_display = ('numero_senha_display', 'usuario_display', 'categoria_display', 'representacao', 'status_badge', 'criado_em')
    list_filter = ('status', 'categoria__vaquejada', 'categoria', 'criado_em')
    search_fields = ('representacao', 'puxador', 'esteiro', 'numero_senha', 'user__username')
    readonly_fields = ('id', 'criado_em', 'qr_code_display')
    
    fieldsets = (
        ('🎫 Informações da Senha', {
            'fields': ('id', 'numero_senha', 'categoria', 'user', 'status')
        }),
        ('👤 Dados do Vaqueiro', {
            'fields': ('representacao', 'puxador', 'esteiro')
        }),
        ('🐴 Cavalaria', {
            'fields': ('cavalo_puxador', 'cavalo_esteiro')
        }),
        ('🔐 QR Code PIX', {
            'fields': ('qr_code_display',)
        }),
        ('📄 Comprovante de Pagamento', {
            'fields': ('comprovante_pix', 'pago_em')
        }),
        ('📅 Datas', {
            'fields': ('criado_em',),
            'classes': ('collapse',)
        }),
    )
    
    def numero_senha_display(self, obj):
        return format_html(
            '<strong style="background-color: #ffc107; padding: 5px 10px; border-radius: 5px; font-size: 1.1em;">#{}</strong>',
            obj.numero_senha
        )
    numero_senha_display.short_description = 'Senha'
    
    def usuario_display(self, obj):
        return format_html(
            '<strong>👤 {}</strong>',
            obj.user.username
        )
    usuario_display.short_description = 'Usuário'
    
    def categoria_display(self, obj):
        return format_html(
            '<strong>📂 {}</strong><br><small>{}</small>',
            obj.categoria.nome,
            obj.categoria.vaquejada.nome
        )
    categoria_display.short_description = 'Categoria'
    
    def status_badge(self, obj):
        colors = {'open': '#ffc107', 'closed': '#dc3545', 'paid': '#28a745', 'cancelled': '#6c757d'}
        labels = {'open': 'Aberto', 'closed': 'Fechado', 'paid': 'Pago', 'cancelled': 'Cancelado'}
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold;">{}</span>',
            colors.get(obj.status, '#6c757d'),
            labels.get(obj.status, obj.status)
        )
    status_badge.short_description = 'Status'
    
    def qr_code_display(self, obj):
        if obj.qr_code:
            return format_html(
                '<img src="{}" style="max-width: 200px; height: auto; border: 2px solid #ddd; padding: 5px; border-radius: 5px;">',
                obj.qr_code.url
            )
        return format_html('<span style="color: #999;">Sem QR Code</span>')
    qr_code_display.short_description = 'QR Code PIX'
