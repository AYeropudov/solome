from django.urls import path, re_path

from cms.views import IndexView
from cms.views import ProductsView
from cms.views import ProductsAddView
from cms.views import ProductsEditView
from cms.views import ProductsCopyView
from cms.views import TreeView, Attributes, ModalAttribute
from cms.views import TreeView, CatalogsModals
from cms.views import Tags, ModalTags, TaggingProducts

urlpatterns = [
    path('', IndexView.as_view(), name='cms.index'),

    path('products/', ProductsView.as_view(), name='cms.product.list'),
    path('products/add', ProductsAddView.as_view(), name='cms.product.add'),
    path('products/edit/<int:product_id>', ProductsEditView.as_view(), name='cms.product.edit'),
    path('products/copy/<int:product_id>', ProductsCopyView.as_view(), name='cms.product.copy'),

    path('catalog/<int:cat_id>', TreeView.as_view(), name='cms.tree'),
    path('catalog/', TreeView.as_view(), name='cms.tree'),
    path('catalog/m/<str:type_modal>', CatalogsModals.as_view(), name='cms.tree.modal'),

    re_path(r'^attributes/((?P<attr_id>\w+)/)?$', Attributes.as_view(), name='cms.attributes'),
    re_path(r'^modals/attributes/((?P<attr_id>\w+)/)?$', ModalAttribute.as_view(), name='cms.attributes.modal'),

    re_path(r'^tags/((?P<tag_id>\w+)/)?$', Tags.as_view(), name='cms.tags'),
    re_path(r'^modals/tags/((?P<tag_id>\w+)/)?$', ModalTags.as_view(), name='cms.tags.modal'),

    path('products/tagging/', TaggingProducts.as_view(), name='cms.product.tagging')
]
