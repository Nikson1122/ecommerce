from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,  MypasswordChangeForm
from .views import CustomLogoutView
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),

    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('accounts/login', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class= MypasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),

   path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),

    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
