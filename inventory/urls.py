from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('new/', views.inventory_new, name='inventory_new'),
    path('<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('<int:pk>/edit/', views.inventory_edit, name='inventory_edit'),
    path('<int:pk>/delete/', views.inventory_delete, name='inventory_delete'),
    path('<int:pk>/plus/', views.num_plus, name='num_plus'),
    path('<int:pk>/minus/', views.num_minus, name='num_minus'),

    path('client/', views.client_list, name='client_list'),
    path('client/<int:pk>/', views.client_detail, name='client_detail'),
    path('client/new/', views.client_new, name='client_new'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client_delete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
