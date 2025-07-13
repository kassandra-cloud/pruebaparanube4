from django.contrib import admin
from .models import Post, Planificacion,Historial,CustomUser

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Planificacion)
admin.site.register(Historial)