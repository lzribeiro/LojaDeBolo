# Generated by Django 5.0.6 on 2024-06-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_pedido_cpf_pedido_nome_cliente_pedido_numero_cartao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
