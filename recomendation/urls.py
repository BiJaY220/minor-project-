from django.urls import path 
from . import views
appname ='myapp'
urlpatterns = [ path('',views.start),
               path('myview/',views.myview,name='myview'),
               path('run/',views.start)
]