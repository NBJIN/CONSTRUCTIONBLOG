from django.urls import path
from .views import PostList


urlpatterns = [

    path("postread", PostList.as_view(), name="postread"),
]
