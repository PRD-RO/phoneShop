"""
URL configuration for PhonePro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mobile import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.LandPage,name='landpage'),
    path('admin/', admin.site.urls),
    path('welcome/',views.Welcom),
    path('getdata/',views.GetData),
    path('sendata/<str:name>/',views.datasend),
    path('add/<int:d1>/<int:d2>',views.Add),
    path('aboutus/',views.AbouUs,name='aboutus'),
    path('blog/',views.blog,name='blog'),
    path('phonemenue/',views.phonemenue,name='phone'),
    path("invoice/<int:order_id>/",views.invoice,name="invoice"),
    path('details/',views.details,name='detailes'),
    path('add_to_cart/',views.addToCart,name='AddToCart'),
    path('checkout/',views.checkout,name='checkout'),
    path('authlogin/',views.authLogin,name='authLogin'),
    path('authregister/',views.authRegister,name='authRegister'),
    path('logout/',views.authLogout,name='authLogout'),
    path('account/',views.Account,name='account'),
]
if settings.DEBUG:
 urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 