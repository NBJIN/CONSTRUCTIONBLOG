from django.urls import path, include
from django.http import HttpResponse
from . import views
from .views import (
    PostView,
    PostDetailView,
    PostAddView,
    PostUpdate,
    PostDelete
)
from .views import UserSignup, UserLoginView, UserLogoutView, CommentView
from .views import CommentAddView,  CommentUpdate, CommentDelete


urlpatterns = [
    path('signup/', UserSignup.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('', PostView.as_view(), name="postread"),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='postdetail'),
    path('create/<int:pk>', PostAddView.as_view(), name='postcreate'),
    path('update/<int:pk>', PostUpdate.as_view(), name='postupdate'),
    path('postdelete/<int:pk>', PostDelete.as_view(), name='postdelete'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('postdetail/<int:pk>/commentadd/', CommentAddView, name='commentadd'),
    path('commentupdate/<int:pk>', CommentUpdate, name='commentupdate'),
    path('commentdelete/<int:pk>', CommentDelete, name='commentdelete'),
]
