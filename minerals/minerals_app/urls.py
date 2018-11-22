from django.urls import path


from . import views

urlpatterns = [
    path('details/<int:pk>', views.minerals_detail, name="detail"),
    path('', views.minerals_list, name="list")
]
