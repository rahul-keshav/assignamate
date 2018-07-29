from django import forms

from .models import Assignment,Questions,Studymaterial,Blogsite,Blog_page

from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    question=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control' ,
            'placeholder': 'Write a question...'
        }
    ))

    option_a = forms.CharField(widget=forms.TextInput(
       attrs={
           'class': 'form-control',
           'placeholder': 'Write your answer...'
       }
    ))


    option_b = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your answer...'
        }
    ))

    option_c = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your answer...'
        }
    ))

    option_d = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your answer...'
        }
    ))
    CHOICES = (('a', 'Option a'), ('b', 'Option b'),('c', 'Option c'), ('d', 'Option d'),)
    answer = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)

    # answer = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Write your answer...'
    #     }
    # ))
    positive_marks=forms.CharField(widget=forms.TextInput(
        attrs = {
        'class': 'form-control',
        'placeholder': 'Marks...'
        }
    )
    )
    negative_marks = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Marks...'
        }
    )
    )

    hint = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your hint...'
        }
    ))

    tags = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your tags...'
        }
    ))

    class Meta:
        model = Questions
        fields = ('question','option_a','option_b','option_c','option_d','answer','positive_marks','negative_marks','hint','tags',)





class DocumentForm(forms.ModelForm):
    class Meta:
        model = Studymaterial
        fields = ('name', 'subject','discription', 'document', )


class BlogForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your title...'
        }
    ))
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your text...'
        }
    ))
    class Meta:
        model=Blog_page
        fields=('title','text','image')

class Blog_site_Form(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your title...'
        }
    ))

    quotes = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your title...'
        }
    ))

    discription = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your text...'
        }
    ))

    class Meta:
        model=Blogsite
        fields=('name','quotes','discription','background_image')







