from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('delivery', views.DeliveryView.as_view(), name='delivery'),
    path('catalog', views.CatalogView.as_view(), name='catalog'),
    path('catalog/<str:section_code>', views.SectionView.as_view(), name='section'),
    path('info', views.InfoView.as_view(), name='info'),
    path('item', views.ItemView.as_view(), name='item'),
]
