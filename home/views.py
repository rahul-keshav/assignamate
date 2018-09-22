from django.views.generic import TemplateView
from home.forms import HomeForm,Assignment_discussion_form,Assignment_discussion_reply_form
from django.shortcuts import render,redirect,reverse,get_object_or_404
from home.models import Post,Assignment_discussion
from assignment.models import Assignment
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def notifications(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            form = HomeForm(request.POST,)
            args={'form':form}
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('home:home')
            else:
                messages.warning(request, 'Please correct the error below.')
        else:
            posts = Post.objects.all().order_by('-date')
            users = User.objects.exclude(id=request.user.id)
            form=HomeForm
            args={'form':form,'posts':posts,'users':users}
        return render(request,'home/home.html',args)
    else:
        if request.method == 'POST':
            form = HomeForm(request.POST,)
            args={'form':form}
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('home:home')
            else:
                messages.warning(request, 'Please correct the error below.')
        else:
            posts = Post.objects.all().order_by('-date')
            users = User.objects.exclude(id=request.user.id)
            form=HomeForm
            args={'form':form,'posts':posts,'users':users}
        return render(request,'home/home.html',args)




class My_post(TemplateView):
    template_name = 'home/home.html'
    def get(self,request,pk=None):
        if pk:
            user=get_object_or_404(User,pk=pk)#User.objects.get(pk=pk)
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


def assignment_discussion(request,pk):
    if request.method == 'POST':
        form = Assignment_discussion_form(request.POST,)
        args={'form':form}
        if form.is_valid():
            comment = form.save(commit=False)
            comment.assignment=get_object_or_404(Assignment,pk=pk)#Assignment.objects.get(pk=pk)
            comment.user = request.user
            comment.save()
            return redirect(reverse('home:assignment-discussion',args=[pk]))
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        assignment = get_object_or_404(Assignment,pk=pk)#Assignment.objects.get(pk=pk)
        comments=assignment.assignment_discussion_set.all()
        form=Assignment_discussion_form
        args={'form':form,'comments':comments,}
    return render(request,'home/assignment_discussion.html',args)

def assignment_discussion_reply(request,pk):
    if request.method== 'POST':
        form =Assignment_discussion_reply_form(request.POST,)
        args = {'form': form}
        if form.is_valid() :
            reply=form.save(commit=False)
            reply.assignment_discussion=get_object_or_404(Assignment_discussion,pk=pk)#Assignment_discussion.objects.get(pk=pk)
            reply.user=request.user
            reply.save()
            return redirect('home:home')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form=Assignment_discussion_reply_form
        args={'form':form}
    return render(request,'home/assignment_discussion_reply.html',args)















