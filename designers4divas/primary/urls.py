from django.urls import path, include
from primary import views
from django.conf import settings
from django.conf.urls.static import static


# Template Tagging
app_name = 'primary'

urlpatterns = [
# Base and Main Page
    path('base/',views.BaseView.as_view(),name='base'),
    path('',views.MainView.as_view(extra_context={
        "instagram_profile_name": "designers4divas"})),
    path('home/',views.MainView.as_view(extra_context={
        "instagram_profile_name": "designers4divas"}), name='home'),
    path('index/',views.MainView.as_view(extra_context={
        "instagram_profile_name": "designers4divas"}), name='index'),
# Instagram
    path('instagram/',views.InstagramView.as_view(extra_context={
        "instagram_profile_name": "designers4divas"
    }), name='instagram'),

# Shop home
    path('shop/',views.PostListView.as_view(),name='post_list'),
# Events
    path('events/',views.EventsView.as_view(),name='events'),
# Contact
    path('contact/',views.ContactView.as_view(),name='contact'),
# about
    path('story/',views.StoryView.as_view(),name='story'),

# products
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
# temporary product pages
    path('product1/',views.ProductOneView.as_view(),name='product1'),
    path('product2/',views.ProductTwoView.as_view(),name='product2'),
    path('product3/',views.ProductThreeView.as_view(),name='product3'),
    path('product4/',views.ProductFourView.as_view(),name='product4'),
    path('product5/',views.ProductFiveView.as_view(),name='product5'),
    path('product6/',views.ProductSixView.as_view(),name='product6'),
    path('product7/',views.ProductSevenView.as_view(),name='product7'),
    path('product8/',views.ProductEightView.as_view(),name='product8'),
    path('product9/',views.ProductNineView.as_view(),name='product9'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
