#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaquejada_project.settings')
django.setup()

from core.models import Ingresso, Categoria, Vaquejada
from django.contrib.auth.models import User

vaquejada = Vaquejada.objects.first()
if vaquejada:
    categoria = vaquejada.categorias.first()
    if categoria:
        user = User.objects.filter(username='teste').first()
        if user:
            Ingresso.objects.filter(user=user, categoria=categoria).delete()
            
            ingresso = Ingresso.objects.create(
                categoria=categoria,
                user=user,
                representacao='Teste QR',
                puxador='João',
                esteiro='Pedro',
                cavalo_puxador='Cavalo 1',
                cavalo_esteiro='Cavalo 2',
            )
            
            print('='*50)
            print('INGRESSO CRIADO COM SUCESSO!')
            print('='*50)
            print(f'ID: {ingresso.id}')
            print(f'Representação: {ingresso.representacao}')
            print(f'QR Code: {ingresso.qr_code.name if ingresso.qr_code else "NÃO GERADO"}')
            print('='*50)
