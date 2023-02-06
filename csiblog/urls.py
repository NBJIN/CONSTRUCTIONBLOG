from django.urls import path
from . import views
from .views import PostView, PostDetailView, PostAddView


urlpatterns = [

    path('', PostView.as_view(), name="postread"),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='postdetail'),
    path('create/<int:pk>', PostAddView.as_view(), name='postcreate'),
]

# class PostAddView(CreateView):
#     model = Post
#     template_name = "postcreate.html"
#     success_url = reverse_lazy('postread.html')
