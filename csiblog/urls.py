from django.urls import path
from .views import PostView, PostDetailView


urlpatterns = [

    path('', PostView.as_view(), name="postread"),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='postdetail'),
]
