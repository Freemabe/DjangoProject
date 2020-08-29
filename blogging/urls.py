from django.urls import path
from blogging.views import stub_view, detail_view, list_view, add_model
from blogging.feeds import LatestEntriesFeed

app_name = 'blogging'
urlpatterns = [
    path('', list_view, name="blog_index"),
    path('create', add_model, name="create_post"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('latest/feed', LatestEntriesFeed(), name='feed'),
]