from django.urls import path
from .views import BlogPageView,insertar2Planificacion,mostrarPlanificaciones,insertarHistorial, mostrarHistorial,mostrarPlanificaciones2
from .views import mostrarHistorial2
from blog import views
urlpatterns=[
    path("blog/",BlogPageView.as_view(),name="blog"),
    path('insertar2/', insertar2Planificacion, name='insertar2Planificacion'),
    path('mostrar/', mostrarPlanificaciones, name='mostrarPlanificaciones'),
    path('insertar', insertarHistorial, name='insertarHistorial'),
    path('mostrar2/', mostrarHistorial, name='mostrarHistorial'),
    path('mostrar3/', mostrarPlanificaciones2, name='mostrarPlanificaciones2'),
    path('mostrar4/', mostrarHistorial2, name='mostrarHistorial2'),
    

]