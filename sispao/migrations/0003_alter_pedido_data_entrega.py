# Generated by Django 4.2.7 on 2023-11-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sispao', '0002_alter_pedido_id_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_entrega',
            field=models.DateTimeField(null=True),
        ),
    ]