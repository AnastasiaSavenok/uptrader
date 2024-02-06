from django.urls import path

from menus.views import MenuView

app_name = 'menu_app'

urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
]
