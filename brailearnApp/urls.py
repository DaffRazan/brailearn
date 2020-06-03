from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('word', views.word, name='word'),
    path('tips', views.tips, name='tips'),
    path('forum', views.forum, name='forum'),
    path('newdiscuss', views.newdiscuss, name='newdiscuss'),
    path('addnewdiscuss', views.addnewdiscuss, name='addnewdiscuss'),
]
