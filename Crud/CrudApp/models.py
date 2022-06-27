from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    Name = models.TextField(max_length=45, null=False, verbose_name="Nombre")
    Lastname = models.TextField(max_length=45, null=False, verbose_name="Apellido")
    Cedula = models.BigIntegerField(null=True, verbose_name="Cédula", validators=[MaxValueValidator(9999999999)])
    Birthday = models.DateField(null=True, verbose_name="Fecha de Nacimiento")
    Email = models.EmailField(null=False, verbose_name="Email")
    Cellphone = models.BigIntegerField(null=True, verbose_name="Número de teléfono", validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    
    def __str__(self):
        regs = "Empleado: " + self.Name + " " + self.Lastname
        return regs