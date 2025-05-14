from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import settings
from . import views

urlpatterns = [
    path('', views.landing_page,name='landing_page'),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name="login"),
    path('register/', views.register_user, name="register"),
    path('get_districts_register/', views.get_districts, name='get_districts_register'),
    path('grid_shop/', views.grid_shop, name='grid_shop'),
    path('logout/', views.logout_view, name='logout'),
    path('single_product/', views.single_product, name='single_product'),


    ]+ static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static') + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = "AgriGear Exchange"
admin.site.site_header = "AgriGear Exchange"
admin.site.index_title = "AgriGear Exchange"