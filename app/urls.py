from django.urls import path
from app import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .forms import LoginForm, PasswordChange,PasswordReset,SetPassword
urlpatterns = [
    #path('', views.home),
    path('', views.ProductView.as_view(),name="home"),
    path('productdetail/<int:pk>', views.ProductDetail.as_view(), name='productdetail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('pluscart/', views.pluscart, name='pluscart'),
    path('minuscart/', views.minuscart, name='minuscart'),
    path('removecart/', views.removecart, name='removecart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('playstation/', views.playstation, name='playstation'),
    path('xbox/', views.xbox, name='xbox'),
    path('nintendo/', views.nintendo, name='nintendo'),
    path('pc/', views.pc, name='pc'),
    path('playstation/<slug:data>', views.playstation, name='playstation'),
    path('xbox/<slug:data>', views.xbox, name='xbox'),
    path('nintendo/<slug:data>', views.nintendo, name='nintendo'),
    path('pc/<slug:data>', views.pc, name='pc'),
    path('mobile/', views.mobile, name='mobile'),
    path('signup/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    #path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('customer/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm) , name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm) , name=''),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=PasswordChange,success_url='/passwordchanged/'),name='changepassword'),
    path('passwordchanged/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchanged.html'),name='passwordchanged'),
    path('forgotpassword/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=PasswordReset),name='password_reset'),
    path('forgotpassword/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('forgotpassword/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=SetPassword),name='password_reset_confirm'),
    path('forgotpassword/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('search/', views.search, name='search'),
    path('productdetail/<int:pk>/addreview/', views.AddReviewView.as_view(), name='addreview'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

