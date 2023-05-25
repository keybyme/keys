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
