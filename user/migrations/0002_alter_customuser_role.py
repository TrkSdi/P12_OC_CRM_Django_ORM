# Generated by Django 4.2 on 2023-04-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('Gestion', 'Gestion'), ('Vente', 'Vente'), ('Support', 'Support')], max_length=10, null=True),
        ),
    ]
