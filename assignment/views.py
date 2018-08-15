from django.shortcuts import render,redirect,reverse,get_object_or_404,render_to_response
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from .models import Assignment,Questions,Assignment_answered_by,\
    Studymaterial,Blogsite,Blog_page,Assignmentlikecounter
from django.contrib.auth.models import User
from assignment.forms import QuestionForm,DocumentForm,Blog_site_Form,BlogForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    list_assignment=[]
    for useraccount in request.user.is_following.all():
        user=useraccount.user
        print(user)
        for assignment in user.assignment_set.all():
            list_assignment.append(assignment)
    return render(request,'assignment/index.html',{'list_assignment':list_assignment})

def view_list_assignment(request):
    assignment=Assignment.objects.all()
    paginator=Paginator(assignment,10)
    page=request.GET.get('page')
    assignment=paginator.get_page(page)
    user=request.user
    return render(request,'assignment/assignment_page.html',{'assignment':assignment,'user':user})

def view_list_my_assignment(request,pk=None):
    if pk:
        user=get_object_or_404(User,pk=pk)#User.objects.get(pk=pk)
    else:
        user = request.user
    studymaterial = Studymaterial.objects.all()
    args={'user':user,'studymaterial': studymaterial}
    return render(request,'assignment/my_assignment_page.html',args)


def AssignmentLikeToggle(request,id):
    assignment = get_object_or_404(Assignment, pk=id)  # Assignment.objects.get(pk=id)
    if hasattr(assignment, 'assignmentlikecounter'):
        assignment_like_list = assignment.assignmentlikecounter
    else:
        assignment_like_list = Assignmentlikecounter(assignment=assignment)
        assignment_like_list.save()
    user = request.user
    if user in assignment_like_list.user.all():
        assignment_like_list.user.remove(user)
    else:
        assignment_like_list.user.add(user)
    number_of_like = len(assignment_like_list.user.all())
    assignment_like_list.number_of_like = number_of_like
    assignment_like_list.save()
    return redirect(reverse('assignment:assignment', args=[id]))


class AssignmentUpdate(UpdateView):
    model = Assignment
    fields = ['title','discription']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('assignment:my_assignment_page')

class AssignmentCreate(CreateView):
    model = Assignment
    fields = ['title','discription']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class QuestionView(DetailView):
    template_name = 'assignment/question_paper.html'
    model = Assignment


def QuestionAdd(request,pk):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.assignment = get_object_or_404(Assignment,pk=pk)#Assignment.objects.get(pk=pk)
            question.save()
            return redirect(reverse('assignment:assignment', args=[pk]))

    else:
        form = QuestionForm
    return render(request,'assignment/add_question_form.html',{'form': form})

class QuestionUpdate(UpdateView):
    model = Questions
    fields = ['question','image','answer','option_a','option_b','option_c','option_d','positive_marks','negative_marks']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('assignment:my_assignment_page')

class QuestionDelete(DeleteView):
    model = Questions
    success_url = reverse_lazy('assignment:my_assignment_page')


def assignment_check(request,assignment_id):
    assignment=get_object_or_404(Assignment,pk=assignment_id)
    marks=0
    total_marks=0
    forloopcounter = 1
    answersting=''
    for question in assignment.questions_set.all():

        post_input='inlineRadioOptions'+str(forloopcounter)

        answersting=answersting+request.POST[post_input]

        if request.POST[post_input]=='z':
         forloopcounter = forloopcounter + 1
         total_marks=total_marks+question.positive_marks

        elif question.answer==request.POST[post_input]:
         marks=marks+question.positive_marks
         forloopcounter = forloopcounter+1
         total_marks = total_marks + question.positive_marks

        elif question.answer!= request.POST[post_input]:
         marks = marks - question.negative_marks
         total_marks = total_marks + question.positive_marks
         forloopcounter = forloopcounter+1

    print(answersting)
    print(marks)

    p = Assignment_answered_by(name_of_assignment=assignment.title,assignment_id=assignment.id,
                               name_of_teacher=assignment.user.first_name+" "+assignment.user.last_name,
                               assigner_username=assignment.user.username,
                               user=request.user,answer_string=answersting,
                               marks=marks,total_marks=total_marks)
    p.save()

    return redirect(reverse('assignment:assignment_page'))

def answersheet(request,ass_id, ans_id):
    assignment=get_object_or_404(Assignment,pk=ass_id)#Assignment.objects.get(pk=ass_id)
    assignment_answered_by=get_object_or_404(Assignment_answered_by,pk=ans_id)#Assignment_answered_by.objects.get(pk=ans_id)
    answer= assignment_answered_by.answer_string
    list1 = []
    for i in answer:
        list1.append(i)
    return render(request,'assignment/answersheetpage.html',{'assignment':assignment,'answer':list1})

def studymaterial_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            study_material=form.save(commit=False)
            study_material.user=request.user
            study_material.save()
            return redirect(reverse('assignment:my-studymaterial'))
    else:
        form = DocumentForm()
    return render(request, 'assignment/studymaterial_upload.html',{'form': form})

def add_blog_site(request):
    if request.method=='POST':
        form=Blog_site_Form(request.POST,request.FILES)
        if form.is_valid():
            blog_site=form.save(commit=False)
            blog_site.user = request.user
            blog_site.save()
            return redirect(reverse('assignment:blog_site_list'))
    else:
        form=Blog_site_Form()
    return render(request,'assignment/add_blog_site.html',{'form':form})

def blog_site_list(request,pk=None):
    if pk:
        user=get_object_or_404(User,pk=pk)#User.objects.get(pk=pk)
    else:
        user=request.user

    return render(request,'assignment/blog_site_list.html',{'user':user,})

def view_blog_site(request,pk):
    blog_site=get_object_or_404(Blogsite,pk=pk)#Blogsite.objects.get(pk=pk)
    blogs=blog_site.blog_page_set.all
    return render(request,'assignment/blog_site.html',{'blog_site':blog_site,'blogs':blogs})

def add_blog(request,pk):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.blog_site=get_object_or_404(Blogsite,pk=pk)#Blogsite.objects.get(pk=pk)
            blog.user = request.user
            blog.save()
            return redirect(reverse('assignment:blog_site',args=[pk]))
    else:
        form=BlogForm()
        return render(request,'assignment/add_blog.html',{'form': form,})

def blog(request,pk):
    blog=get_object_or_404(Blog_page,pk=pk)#Blog_page.objects.get(pk=pk)
    return render(request,'assignment/blog.html',{'blog':blog})

def result(request):
    result=request.user.assignment_answered_by_set.order_by('-submitted')
    return render(request,'assignment/result.html',{'result':result,})

def studymaterial(request):
    studymaterials=Studymaterial.objects.all()
    return render(request,'assignment/studymaterial.html',{'studymaterial':studymaterials})

def my_studymaterial(request):
    user=request.user
    studymaterials=user.studymaterial_set.all()
    return render(request,'assignment/studymaterial.html',{'studymaterial':studymaterials})


################
# new search view
################
class SearchView(ListView):
    template_name = 'assignment/searchresult.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            assignment_results= Assignment.objects.search(query)
            studymaterial_results= Studymaterial.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                assignment_results,
                studymaterial_results,

            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        return Assignment.objects.none() # just an empty queryset as default

