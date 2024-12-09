from django.db import models

# Create your models here.

class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripción",null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")

    def __str__(self):
        fila = f"{self.nombre} - {self.descripcion} - ${str(self.precio)}"
        return fila
    
    def delete(self, using=None, keep_parents=False):
        # Elimina el archivo de imagen del sistema de archivos
        if self.imagen:
            self.imagen.storage.delete(self.imagen.name)
        # Llama al método delete del superclase
        super().delete(using=using, keep_parents=keep_parents)