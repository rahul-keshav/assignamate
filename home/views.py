from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render,redirect
from home.models import Post
from django.contrib.auth.models import User

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form=HomeForm()
        posts=Post.objects.all().order_by('-date')
        users=User.objects.exclude(id=request.user.id)
        args={ 'form':form,'posts':posts,'users':users }

        return render(request,self.template_name,args )

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

class My_post(TemplateView):
    template_name = 'home/home.html'
    def get(self,request,pk=None):
        if pk:
            user=User.objects.get(pk=pk)
        else:
            user=request.user
        form=HomeForm()
        posts=user.post_set.all().order_by('-date')
        users=User.objects.exclude(id=request.user.id)
        args={ 'form':form,'posts':posts,'users':users }
        return render(request,self.template_name,args )

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)












