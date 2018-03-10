from django.template.defaultfilters import register
from shop.models import Catalog


@register.inclusion_tag('menu_horizontal.html')
def menu_block():
    roots = Catalog.objects.root_nodes()
    menu_tree = []
    for root in roots:
        menu_tree.append({
            'title': root.title,
            'code': root.code,
            'child': root.get_children()
        })

    return {'tree': menu_tree}


@register.inclusion_tag('menu_footer_catalog.html')
def menu_catalog_footer():
    roots = Catalog.objects.root_nodes()
    menu_tree = []
    for root in roots:
        menu_tree.append({
            'title': root.title,
            'code': root.code,
        })

    return {'tree': menu_tree}