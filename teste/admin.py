from django.contrib import admin

from .models import Cargo, Funcionario

admin.site.register(Funcionario)
admin.site.register(Cargo)
