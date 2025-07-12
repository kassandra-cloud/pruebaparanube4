from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings  

class Post(models.Model):
    title = models.CharField(max_length=200)
    
    # Cambia la referencia de author a settings.AUTH_USER_MODEL
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class CustomUser(AbstractUser):
    ROLES = (
        ('familiar', 'Familiar'),
        ('usuario', 'Usuario'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLES)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
 

class Historial(models.Model):
    diagnostico = models.TextField(max_length=75)
    alergias = models.TextField(max_length=75)
    afecciones = models.TextField(max_length=75)
    medicamento = models.TextField(max_length=75)

   

class Planificacion(models.Model):
    destino = models.TextField(max_length=75)
    tiempodeviaje = models.TextField(max_length=75)
    ruta = models.TextField(max_length=75)
    descripcion = models.TextField(max_length=75)

    # Agrega un campo ForeignKey a CustomUser
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='planificaciones'
    )


class Sesiones(models.Model):
    id_sesiones = models.AutoField(primary_key=True)
    fechaInicio = models.DateField()
    horaInicio = models.CharField(max_length=10)
    fechaCierre = models.DateField()
    horaCierre = models.CharField(max_length=10)
    dispositivoInicio = models.CharField(max_length=50)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class OpcionesVoz(models.Model):
    id_opciones_voz = models.AutoField(primary_key=True)
    nombreVoz = models.CharField(max_length=50)
    idioma = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Alertas(models.Model):
    id_alertas = models.AutoField(primary_key=True)
    fechaAlerta = models.DateField()
    horaAlerta = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)
    tipoAlerta = models.CharField(max_length=50)
    ubicacionAlerta = models.CharField(max_length=50)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class SeguimientoTiempoReal(models.Model):
    id_seguimiento_tiempo_real = models.AutoField(primary_key=True)
    latitudActual = models.CharField(max_length=20)
    longitudActual = models.CharField(max_length=20)
    fecharegistro = models.DateField()
    horaregistro = models.CharField(max_length=10)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class RegistroActividades(models.Model):
    id_registro_actividades = models.AutoField(primary_key=True)
    fechaActual = models.DateField()
    horaActividad = models.CharField(max_length=10)
    descripcion = models.TextField()
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class ContactoEmergencia(models.Model):
    id_contacto_emergencia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    parentesco = models.CharField(max_length=50)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CambioContraseña(models.Model):
    id_cambio_contraseña = models.AutoField(primary_key=True)
    fechaCambio = models.DateField()
    horaCambio = models.CharField(max_length=10)
    contraseñaAnterior = models.CharField(max_length=50)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class PreferenciaUsuario(models.Model):
    id_preferencias = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=20)
    volumen = models.IntegerField()
    velocidadLectura = models.IntegerField()
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Destino(models.Model):
    id_destino = models.AutoField(primary_key=True)
    nombreDestino = models.CharField(max_length=50)
    latitudInicial = models.CharField(max_length=20)
    longitudInicial = models.CharField(max_length=20)
    latitudDestino = models.CharField(max_length=20)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class DestinosFrecuentes(models.Model):
    id_destinos_frecuentes = models.AutoField(primary_key=True)
    iddestino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Ruta(models.Model):
    id_ruta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=20)
    horaInicio = models.CharField(max_length=10)
    detalleRuta = models.TextField()
    iddestino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class HistorialRuta(models.Model):
    id_historial_ruta = models.AutoField(primary_key=True)
    fechaInicio = models.DateField()
    horaInicio = models.CharField(max_length=10)
    fechaTermino = models.DateField()
    horaTermino = models.CharField(max_length=10)
    estado = models.CharField(max_length=20)
    idruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    iddestino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class UsuarioEliminado(models.Model):
    # Copia todos los campos del modelo CustomUser
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254)
    # Otros campos que puedas tener en CustomUser
    role = models.CharField(max_length=10, choices=CustomUser.ROLES)
class HistorialUsuario(models.Model):
    id_historial_usuario = models.AutoField(primary_key=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    username_anterior = models.CharField(max_length=150)
    email_anterior = models.EmailField(max_length=254)
    role_anterior = models.CharField(max_length=10)
    
    
    # Relación con el usuario original
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='historial')

   