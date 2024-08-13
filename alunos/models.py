from django.db import models

class Aluno (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
