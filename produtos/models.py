from django.db import models

# Create your models here.
# products/models.py
from django.db import models
from django.conf import settings # Vamos usar isso para ligar ao usuário

class Product(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='produtos' # Mudado para 'produtos' para consistência
    )
    
    # O "Porquê": O nome do produto, obrigatório (max_length=100).
    name = models.CharField(max_length=100)
    
    # O "Porquê": Uma descrição. blank=True, null=True significa que este campo é opcional.
    description = models.TextField(blank=True, null=True)
    
    # O "Porquê": Um campo Sim/Não para o seu requisito de certificação.
    is_certified = models.BooleanField(default=False)
    
    # O "Porquê": Guarda quando o produto foi criado. auto_now_add=True faz isso automaticamente.
    created_at = models.DateTimeField(auto_now_add=True)
    
    # O "Porquê": Guarda quando foi atualizado. auto_now=True atualiza automaticamente.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # O "Porquê": Para dar um nome legível ao produto no painel admin.
        return self.name