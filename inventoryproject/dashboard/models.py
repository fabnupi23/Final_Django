from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
CATEGORY =(
    ('Administrador', 'Administrador'),
    ('Estudiante', 'Estudiante'),
    ('Registro_Control', 'Registro_Control'),
    ('Credito_Cartera', 'Credito_Cartera'),
    ('Paz_Salvo', 'Paz_Salvo'),
    
)


class Product(models.Model):
    name=models.CharField(max_length=100, null=True, verbose_name='Nombre Usuario')
    category=models.CharField(max_length=20, choices=CATEGORY, null=True, verbose_name='Rol')
    cantidad= models.PositiveBigIntegerField(null=True)
    class Meta: 
        verbose_name_plural='Product'


    def __str__(self):
        return f'{self.name}'
    
    

    
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True, verbose_name='Usuarios')
    staff= models.ForeignKey(User,models.CASCADE,null=True, verbose_name='Personal')
    order_quantity=models.PositiveIntegerField(null=True, verbose_name='Documento')
    date=models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    def clean(self):
        if self.order_quantity > self.product.cantidad:
            raise ValidationError('El código debe tener maximo 10 digitos')
        self.product.cantidad -= self.order_quantity
        self.product.save()

    class Meta: 
        verbose_name_plural='Order'


    