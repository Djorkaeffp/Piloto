# forms.py
from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome Completo',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome completo'
        })
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail'
        })
    )

    telefone = forms.CharField(
        max_length=15,
        label='Telefone / WhatsApp',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(99) 99999-9999'
        })
    )

    ASSUNTOS = [
        ('suporte', 'Suporte Técnico'),
        ('comercial', 'Comercial'),
        ('reclamacao', 'Reclamação'),
        ('parceria', 'Parceria'),
        ('financeiro', 'Financeiro'),
    ]

    assunto = forms.ChoiceField(
        choices=ASSUNTOS,
        label='Assunto',
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Escreva sua mensagem',
            'rows': 4
        })
    )


class ProdutoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome do Produto',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: Impressora'
        })
    )

    preco = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Preço',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 600.00'
        })
    )
