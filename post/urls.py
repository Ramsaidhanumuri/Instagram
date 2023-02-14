from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('newpost/', views.NewPost, name='newpost'),
    path('<uuid:post_id>/', views.PostDetails, name='post-details'),
    path('tag/<slug:tag_slug>', views.tags, name='tags'),
    path('<uuid:post_id>/<int:code>/like', views.like, name='like'),
    path('<uuid:post_id>/<int:code>/favourite', views.favourite, name='favourite'),

]