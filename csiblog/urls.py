from django.urls import path, include
from django.http import HttpResponse
from . import views
from .views import (
    PostView,
    PostDetailView,
    PostAddView,
    PostUpdate,
    PostDelete,
    CommentAddView,
    CommentDelete
)
from .views import UserSignup, UserLoginView, UserLogoutView, CommentView
from .views import CommentAddView, CommentDelete, PostlikesView


urlpatterns = [
    path('signup/', UserSignup.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('', views.PostView.as_view(), name="postread"),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='postdetail'),
    path('create/', views.PostAddView.as_view(), name='postcreate'),
    path('create/<int:pk>', PostAddView.as_view(), name='postcreate'),
    path('postdetail/<int:pk>/commentadd/', CommentAddView.as_view(), name='commentadd'),
    
    path('postdetail/<int:pk>/commentdelete/', views.CommentDelete.as_view(), name='commentdelete'),
    path('update/<int:pk>', PostUpdate.as_view(), name='postupdate'),
    path('postdelete/<int:pk>', PostDelete.as_view(), name='postdelete'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
  

    path('likes/<int:pk>', PostlikesView, name='post_like'),
]

