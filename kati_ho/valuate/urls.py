from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('signup/',views.signuppage,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('',views.homepage,name='home'),
    path('compare/',views.compare,name='compare'),
    path('valuate/',views.valuate,name='valuate'),
    path('sell/',views.sell_product,name='sell'),
    path('buy/',views.buy,name='buy'),
    path('recommend/',views.recommend,name='recommend'),
    path('logout/',views.logout,name='logout')
]

urlpatterns+=staticfiles_urlpatterns()