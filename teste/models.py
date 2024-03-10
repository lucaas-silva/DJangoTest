from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateTimeField("Data de nascimento")

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cargo_nome = models.CharField(max_length=200)

    def __str__(self):
        return self.cargo_nome
