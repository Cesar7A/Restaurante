# Generated by Django 4.2.7 on 2024-12-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_pedido_cantidad_pedido_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
