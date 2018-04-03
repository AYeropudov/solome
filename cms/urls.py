from django.urls import path

from cms.views import IndexView
from cms.views import ProductsView
from cms.views import ProductsAddView
from cms.views import ProductsEditView
from cms.views import TreeView, CatalogsModals


urlpatterns = [
    path('', IndexView.as_view(), name='cms.index'),
    path('products/', ProductsView.as_view(), name='cms.product.list'),
    path('products/add', ProductsAddView.as_view(), name='cms.product.add'),
    path('products/edit/<int:product_id>', ProductsEditView.as_view(), name='cms.product.edit'),
    path('catalog/<int:cat_id>', TreeView.as_view(), name='cms.tree'),
    # path('catalog/', TreeView.as_view(), name='cms.tree.put'),
    path('catalog/m/<str:type_modal>', CatalogsModals.as_view(), name='cms.tree.modal'),
]
