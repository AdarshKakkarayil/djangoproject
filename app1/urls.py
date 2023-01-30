from django.urls import path
from . import views 
app_name='app1'
urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('uploadimage',views.uploadimage,name='uploadimage'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logout',views.logout,name='logout'),
    path('showimage',views.showimage,name='showimage'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('update/<int:id>',views.update,name='update'),
     

]