from django.urls import path
from .import views 

urlpatterns = [
    path("",views.home),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('UserRegister/',views.UserRegister,name='UserRegister'),
    path('UserLogin/',views.UserLogin,name='UserLogin'),
    path('userquery/',views.userquery,name='userquery'),
    path('insertquery/',views.insertquery,name='insertquery'),
    path('showquery/',views.showquery,name='showquery'),
    path('editpage/<int:pk>/',views.editPage,name='editpage'),
    path('update/<int:pk>/',views.updateData,name='update'),
    path('delete/<int:pk>/',views.deleteData,name='delete'),
    path('logout/',views.logout,name='home'), 

    # admin data path 
    path('adreg/',views.adreg,name='adreg'),
    path('adlog/',views.adlog,name='adlog'),
    path('AdminRegister/',views.AdminRegister,name='AdminRegister'),
    path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
    path('AdminQuery/',views.AdminQuery,name='AdminQuery'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),


]
