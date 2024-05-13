# Generated by Django 5.0.6 on 2024-05-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Estudiante', 'Estudiante'), ('Registro_Control', 'Registro_Control'), ('Credito_Cartera', 'Credito_Cartera'), ('Paz_Salvo', 'Paz_Salvo')], max_length=20, null=True, verbose_name='Rol'),
        ),
    ]
