from . import views
from django.urls import include, path

urlpatterns = [
    path('' , views.home , name = 'home'),
    
    path('signup' , views.signup , name='signup'),
    path('signin' , views.signin , name='signin'),
    path('signout' , views.signout , name='signout'),
    
    path('addcontact' , views.addcontact , name ='addcontact')
    
    
    # path('contacts' , views.contactslist , name='contactslist'),
    # path('<str:>' , ),
    # path('addcontact', views.addcontact , name='addcontact'),
    # path('updatecontact')
    

]