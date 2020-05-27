from django import forms
from primary.models import Post, Comment, Contact
from django.core.files.images import get_image_dimensions


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','image','price','description','additional_information',)

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'price':forms.TextInput(attrs={'class':'textinputclass'}),
            'description':forms.Textarea(attrs={'class':'editable large-editor-textarea postcontent'}),
            'additional_information':forms.Textarea(attrs={'class':'editable large-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('contact_name','contact_email','contact_subject','contact_message',)

        widgets = {
            'contact_name':forms.TextInput(attrs={'class':'textinputclass'}),
            'contact_message':forms.Textarea(attrs={'class':'editable large-editor-textarea postcontent'})
        }
