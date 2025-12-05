from django.urls import path
from . import views

urlpatterns = [
    # Home e autenticação
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard do vaqueiro
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Vaquejadas públicas
    path('vaquejadas/', views.vaquejadas_list, name='vaquejadas_list'),
    path('vaquejadas/<uuid:vaquejada_id>/', views.vaquejada_detail, name='vaquejada_detail'),
    
    # Ingressos/Senhas
    path('categoria/<uuid:categoria_id>/mapa-senhas/', views.mapa_senhas, name='mapa_senhas'),
    path('gerar-ingresso/<uuid:categoria_id>/<int:numero_senha>/', views.gerar_ingresso, name='gerar_ingresso'),
    path('meus-ingressos/', views.meus_ingressos, name='meus_ingressos'),
    path('ingresso/<uuid:ingresso_id>/', views.ingresso_detail, name='ingresso_detail'),
    path('ingresso/<uuid:ingresso_id>/editar/', views.ingresso_edit, name='ingresso_edit'),
    path('ingresso/<uuid:ingresso_id>/comprovante/', views.enviar_comprovante_pix, name='enviar_comprovante_pix'),
    
    # Admin - Confirmação de pagamentos
    path('admin/ingresso/<uuid:ingresso_id>/confirmar-pagamento/', views.admin_confirmar_pagamento, name='admin_confirmar_pagamento'),
    
    # Admin
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/vaquejadas/', views.admin_vaquejadas, name='admin_vaquejadas'),
    path('admin/vaquejada/nova/', views.admin_vaquejada_edit, name='admin_vaquejada_new'),
    path('admin/vaquejada/<uuid:vaquejada_id>/editar/', views.admin_vaquejada_edit, name='admin_vaquejada_edit'),
    path('admin/vaquejada/<uuid:vaquejada_id>/ingressos/', views.admin_ingressos, name='admin_ingressos'),
    path('admin/vaquejada/<uuid:vaquejada_id>/relatorio/', views.admin_relatorio, name='admin_relatorio'),
    
    # Exportação
    path('admin/vaquejada/<uuid:vaquejada_id>/exportar-excel/', views.exportar_excel, name='exportar_excel'),
    path('admin/vaquejada/<uuid:vaquejada_id>/exportar-csv/', views.exportar_csv, name='exportar_csv'),
]
