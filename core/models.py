from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
import uuid


class Vaquejada(models.Model):
    """Modelo para Vaquejada - Eventos"""
    OPEN = 'open'
    CLOSED = 'closed'
    CANCELLED = 'cancelled'
    
    STATUS_CHOICES = [
        (OPEN, 'Aberta'),
        (CLOSED, 'Fechada'),
        (CANCELLED, 'Cancelada'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255, verbose_name='Nome da Vaquejada')
    dia = models.DateField(verbose_name='Data do Evento', default=timezone.now)
    hora = models.TimeField(verbose_name='Hora do Evento', default='14:00')
    local = models.CharField(max_length=255, verbose_name='Local/Rancho')
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=OPEN)
    imagem = models.ImageField(upload_to='vaquejadas/', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Vaquejada'
        verbose_name_plural = 'Vaquejadas'
        ordering = ['-dia', '-hora']
    
    def __str__(self):
        return f"{self.nome} - {self.dia.strftime('%d/%m/%Y')}"


class Categoria(models.Model):
    """Categorias de inscrição em cada vaquejada"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vaquejada = models.ForeignKey(Vaquejada, on_delete=models.CASCADE, related_name='categorias', verbose_name='Vaquejada')
    nome = models.CharField(max_length=100, verbose_name='Nome da Categoria')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    n_ingressos = models.IntegerField(verbose_name='Quantidade de Ingressos', default=50)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        unique_together = ('vaquejada', 'nome')
        ordering = ['vaquejada', 'nome']
    
    def __str__(self):
        return f"{self.vaquejada.nome} - {self.nome}"
    
    def ingressos_disponiveis(self):
        """Retorna quantidade de ingressos disponíveis"""
        vendidos = Ingresso.objects.filter(
            categoria=self, 
            status__in=['open', 'closed', 'paid']
        ).count()
        return max(0, self.n_ingressos - vendidos)


class Ingresso(models.Model):
    """Modelo para Ingresso/Senha - Inscrição do vaqueiro"""
    OPEN = 'open'
    CLOSED = 'closed'
    PAID = 'paid'
    CANCELLED = 'cancelled'
    
    STATUS_CHOICES = [
        (OPEN, 'Aberto'),
        (CLOSED, 'Fechado'),
        (PAID, 'Pago'),
        (CANCELLED, 'Cancelado'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='ingressos', verbose_name='Categoria')
    numero_senha = models.IntegerField(verbose_name='Número da Senha', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingressos', verbose_name='Usuário')
    representacao = models.CharField(max_length=255, verbose_name='Representação')
    puxador = models.CharField(max_length=255, verbose_name='Puxador')
    esteiro = models.CharField(max_length=255, verbose_name='Esteiro')
    cavalo_puxador = models.CharField(max_length=255, verbose_name='Cavalo do Puxador')
    cavalo_esteiro = models.CharField(max_length=255, verbose_name='Cavalo do Esteiro')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=OPEN, verbose_name='Status')
    qr_code = models.ImageField(upload_to='qrcodes/', null=True, blank=True, verbose_name='QR Code PIX')
    comprovante_pix = models.FileField(upload_to='comprovantes_pix/', null=True, blank=True, verbose_name='Comprovante PIX')
    
    criado_em = models.DateTimeField(auto_now_add=True)
    pago_em = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'
        ordering = ['-criado_em']
        unique_together = ('categoria', 'numero_senha')
    
    def __str__(self):
        return f"Senha {self.numero_senha} - {self.representacao} - {self.categoria.nome}"
    
    def gerar_qr_code(self):
        """Gera QR Code para PIX
        
        ATENÇÃO: Este QR code contém apenas o ID do ingresso.
        Para pagamentos reais, você deve:
        1. Integrar com um gateway (Mercado Pago, Asaas, etc)
        2. Ou gerar payload PIX válido com chave PIX do organizador
        
        Exemplo de payload PIX real:
        - Requer: chave PIX, nome do recebedor, cidade, valor
        - Formato: EMV (padrão Banco Central)
        """
        # TEMPORÁRIO: QR code apenas com ID do ingresso
        # TODO: Substituir por integração real de pagamento
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Dados temporários - apenas para demonstração
        dados_qr = f"SENHA-{self.numero_senha}-{self.categoria.nome}-VALOR-{self.categoria.valor}"
        qr.add_data(dados_qr)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        
        self.qr_code.save(f'qrcode_{self.id}.png', File(buffer), save=False)
    
    @staticmethod
    def senhas_disponiveis(categoria):
        """Retorna lista de números de senhas disponíveis para uma categoria"""
        senhas_ocupadas = Ingresso.objects.filter(
            categoria=categoria,
            status__in=['open', 'closed', 'paid']
        ).values_list('numero_senha', flat=True)
        
        todas_senhas = list(range(1, categoria.n_ingressos + 1))
        return [s for s in todas_senhas if s not in senhas_ocupadas]


# Sinais para gerar QR Code automaticamente
@receiver(post_save, sender=Ingresso)
def gerar_qr_code_ingresso(sender, instance, created, **kwargs):
    """Gera QR Code quando um ingresso é criado"""
    if created and not instance.qr_code:
        instance.gerar_qr_code()
        instance.save(update_fields=['qr_code'])
