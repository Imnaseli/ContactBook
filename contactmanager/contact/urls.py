from . import views
from django.urls import include, path

urlpatterns = [
    path('' , views.home , name = 'home'),
    
    path('signup' , views.signup , name='signup'),
    path('signin' , views.signin , name='signin'),
    path('signout' , views.signout , name='signout'),
    
    path('addcontact' , views.addcontact , name ='addcontact'),
    
    path('goback', views.goback , name='goback'),
    path('contactpage/<int:contact_id>' , views.contactpage , name='contactpage'),  
    path('delete<int:contact_id>' , views.deletecontact , name='deletecontact')  
    
    
    # path('contacts' , views.contactslist , name='contactslist'),
    # path('<str:>' , ),

    # path('updatecontact')
    

]