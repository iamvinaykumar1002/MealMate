from django.urls import path,include
from . import views

app_name = 'delivery'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('signin/', views.sign_in, name = 'sign_in'),
    path('signup/', views.sign_up, name = 'sign_up'),
    path('handle_signin/', views.handle_signin, name = 'handle_signin'),
    path('handle_signup/', views.handle_signup, name = 'handle_signup'),
    path('add_res/', views.add_res, name = 'add_res'),
    path('display_res/', views.display_res, name = 'display_res'),
    path('view_menu/<int:id>', views.view_menu, name = 'view_menu'),
    path('add_menu/<int:id>', views.add_menu, name = 'add_menu'),
    path('delete_menu/<int:id>', views.delete_menu, name = 'delete_menu'),

    path('cusdisplay_res/<str:username>/', views.cusdisplay_res, name = 'cusdisplay_res'),
    path('cusview_menu/<int:id>/<str:username>/', views.cusview_menu, name = 'cusview_menu'),
    path('restaurants/<int:id>/update/', views.update_restaurant, name='update_restaurant'),
    path('restaurants/<int:id>/delete/', views.delete_restaurant, name='delete_restaurant'),
    path('show_cart/<str:username>/',views.show_cart,name = "show_cart"),
]