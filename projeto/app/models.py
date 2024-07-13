from django.db import models
# utilizar {{ }} para imprimir o dado 
# utilizar {% %} para executar um comando 

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    tipo = models.CharField(max_length=255)
    

