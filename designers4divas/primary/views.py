from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm, ContactForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from trebtheweb.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, BadHeaderError
from . import forms
from trebtheweb import settings

# Create your views here.

# Create your views here.
class StoryView(TemplateView):
    template_name = 'main/story.html'

class BaseView(TemplateView):
    template_name = 'main/base.html'

class ContactView(TemplateView):
    template_name = 'main/contact.html'

class MainView(TemplateView):
    template_name = 'main/home.html'

class InstagramView(TemplateView):
    template_name = 'main/instagram.html'

class EventsView(TemplateView):
    template_name = 'main/events.html'


# Temporary Product pages

class ProductOneView(TemplateView):
    template_name = 'primary/product1.html'

class ProductTwoView(TemplateView):
    template_name = 'primary/product2.html'

class ProductThreeView(TemplateView):
    template_name = 'primary/product3.html'

class ProductFourView(TemplateView):
    template_name = 'primary/product4.html'

class ProductFiveView(TemplateView):
    template_name = 'primary/product5.html'

class ProductSixView(TemplateView):
    template_name = 'primary/product6.html'

class ProductSevenView(TemplateView):
    template_name = 'primary/product7.html'

class ProductEightView(TemplateView):
    template_name = 'primary/product8.html'

class ProductNineView(TemplateView):
    template_name = 'primary/product9.html'



class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'primary/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'primary/post_detail.html'

    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('primary:post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'primary/post_draft_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

# Contact Form


def contact(request):
    form_class = ContactForm

    return render(request, 'contact.html', {
        'form': form_class,
    })
#
# def subscribe(request):
#     sub = forms.Subscribe()
#     form = Subscribe(request.POST)
#         if form.is_valid():
#             sub = forms.Subscribe(request.POST)
#             subject = form.cleaned_data['Subject']
#             email = form.cleaned_data['Email']
#             message = form.cleaned_data['Message']
#             recepient = EMAIL_HOST_USER
#             try:
#                 send_mail(subject, message, email, EMAIL_HOST_USER, [recepient], fail_silently = False)
#
#


# def subscribe(request):
#     sub = forms.Subscribe()
#     if request.method == 'POST':
#         sub = forms.Subscribe(request.POST)
#         set = settings
#         subject = ['Subject']
#         email = ['Email']
#         message = ['Message']
#         recepient = EMAIL_HOST_USER
#         send_mail(subject, message, EMAIL_HOST_USER, email, [recepient])
#     return render(request, 'primary/email.html', {'form':sub})




#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('primary:post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('primary:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'primary/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('primary:post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('primary:post_detail', pk=post_pk)
