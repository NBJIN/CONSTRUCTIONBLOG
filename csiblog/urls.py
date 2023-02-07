from django.urls import path, include
from django.http import HttpResponse
from . import views
from .views import PostView, PostDetailView, PostAddView, PostUpdate, PostDelete


urlpatterns = [

    path('', PostView.as_view(), name="postread"),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='postdetail'),
    path('create/<int:pk>', PostAddView.as_view(), name='postcreate'),
    path('update/<int:pk>', PostUpdate.as_view(), name='postupdate'),
    path('csiblog/postdelete/<int:pk>', PostDelete.as_view(), name='postdelete'),
#     path('create/', PostAddView.as_view(), name='postcreate'),
#     path('update/', PostUpdate.as_view(), name='postupdate'),
]
