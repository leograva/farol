# Generated by Django 4.2.1 on 2023-08-16 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farol', '0006_alter_aplicação_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicação',
            name='status',
            field=models.CharField(choices=[('Fora do ar', 'Fora do ar'), ('Em funcionamento', 'Em funcionamento')], max_length=20),
        ),
    ]
