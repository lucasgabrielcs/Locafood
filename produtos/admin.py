# produtos/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista de produtos no admin
    list_display = ('name', 'owner', 'is_certified', 'created_at')

    # Campos que podem ser pesquisados
    search_fields = ('name',)

    # Campos pelos quais a lista pode ser filtrada
    list_filter = ('is_certified', 'created_at')

    # Campos que são apenas para leitura no formulário de edição/criação
    readonly_fields = ('created_at', 'updated_at')

    # Excluímos o campo 'owner' do formulário de CRIAÇÃO/EDIÇÃO,
    # porque ele será preenchido automaticamente pelo 'save_model'.
    exclude = ('owner',) # <--- ESTA É A LINHA CHAVE!

    # Este método é chamado quando você clica em "Salvar" no admin
    def save_model(self, request, obj, form, change):
        # Se o objeto é novo (ainda não tem uma chave primária),
        # defina o proprietário como o usuário que está logado
        if not obj.pk:
            obj.owner = request.user
        # Chame o método save_model original para salvar o objeto no banco de dados
        super().save_model(request, obj, form, change)