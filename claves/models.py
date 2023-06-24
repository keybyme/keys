from django.db import models

class Categoria(models.Model):
    desc=models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table="categoria"
    def __str__(self):
        return self.desc

class Item(models.Model):
    url=models.CharField(max_length=150, null=True, blank=True)
    username=models.CharField(max_length=30, null=True, blank=True)
    password=models.CharField(max_length=30, null=True, blank=True)
    categoria=models.ForeignKey('Categoria', on_delete=models.DO_NOTHING)
    remarks=models.CharField(max_length=50, null=True, blank=True)  
    class Meta:
        db_table="item"
    def __str__(self):
        return f"{self.url} {self.username} {self.password} {self.categoria} {self.remarks}"        

class Catpeople(models.Model):
    catp=models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        db_table="catpeople"
    def __str__(self):
        return self.catp
    
class Contacto(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    address=models.CharField(max_length=100, null=True, blank=True)
    phone=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    catpeople=models.ForeignKey('Catpeople', on_delete=models.DO_NOTHING)

    class Meta:
        db_table="contacto" 
        def __str__(self):
            return f"{self.name} {self.address} {self.phone} {self.email} {self.catpeople}"       
        
class Qrcode(models.Model):
    link=models.ImageField(upload_to='images/', null=True, blank=True)        
    class Meta:
        db_table="qrcode"
    def __str__(self):
        return f"{self.link}"


class Photo(models.Model): 
    ph_link = models.ImageField(upload_to='images/',null=True, blank=True) 
    
    class Meta:
        managed = True
        db_table = 'photos'
    def __str__(self) -> str:
        return f"{self.ph_link}"