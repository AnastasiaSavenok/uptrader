from django import template
from menus.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    active_url = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return ''

    def render_menu(menu_item):
        children = menu_item.children.all()
        is_active = active_url.startswith(menu_item.url)

        html = f'<li class="{"active" if is_active else ""}">'
        html += f'<a href="{menu_item.url}">{menu_item.name}</a>'

        if children:
            html += '<ul>'
            for child in children:
                html += render_menu(child)
            html += '</ul>'

        html += '</li>'
        return html

    return render_menu(menu)
