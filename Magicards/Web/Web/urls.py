from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('inicio/', include('apps.Usuario.urls')),
    path('admin/', admin.site.urls),
    path('productos/', include('apps.Producto.urls')),
    path('registro/', include('apps.Registro.urls')),
    path('usuario/', include('apps.Usuario.urls')),
    path('reset/password', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name='registration/password_reset_email.html'), name="password_reset"),   
    path('reset/password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('reset/password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/password_reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
   

    # Login and Logout
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('comics/', TemplateView.as_view(template_name='comics.html'), name='comics'),
    path('figuras/', TemplateView.as_view(template_name='figuras.html'), name='figuras'),
    path('mangas/', TemplateView.as_view(template_name='mangas.html'), name='mangas'),
]
