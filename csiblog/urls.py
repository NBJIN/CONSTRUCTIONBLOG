from django.urls import path, include
from django.http import HttpResponse
from . import views
from .views import PostView, PostDetailView, PostAddView, PostUpdate, PostDelete
from .views import UserSignup, UserLoginView, UserLogoutView, CommentView
from .views import CommentAddView,  CommentUpdate 


urlpatterns = [
    path('signup/', UserSignup.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('', PostView.as_view(), name="postread"),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='postdetail'),
    path('create/<int:pk>', PostAddView.as_view(), name='postcreate'),
    path('update/<int:pk>', PostUpdate.as_view(), name='postupdate'),
    path('csiblog/postdelete/<int:pk>', PostDelete.as_view(), name='postdelete'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('Comment/', CommentView.as_view(), name='comment'),
    path('commentadd/<int:pk>', CommentAddView.as_view(), name='commentadd'),
    path('commentupdate/<int:pk>', CommentUpdate.as_view(), name='commentupdate'),
]

#     path('create/', PostAddView.as_view(), name='postcreate'),
#     path('update/', PostUpdate.as_view(), name='postupdate'),
