# Generated by Django 5.0.6 on 2024-06-25 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.produto')),
            ],
        ),
    ]
