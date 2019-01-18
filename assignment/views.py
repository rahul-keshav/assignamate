from django.shortcuts import render,redirect,reverse,get_object_or_404,render_to_response
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from .models import Assignment,Questions,Assignment_answered_by, \
    Booklet,Workbook,Workbook_page,Assignmentlikecounter,Interests
from django.contrib.auth.models import User
from assignment.forms import QuestionForm,DocumentForm,Workbook_Form,Workbook_page_Form,AssignmentForm,Interest_form
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from itertools import chain
from accounts.models import UserAccount
from .filters import AssignmentFilter
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'assignment/home.html',)

def index(request):
    if request.user.is_authenticated:
        dictionary2 = {}
        for interest in request.user.interests_set.all():
            list_of_assignment=list(Assignment.objects.intrests(interest))
            dictionary2[interest]=list_of_assignment
        intrests = request.user.interests_set.all()
        for useraccount in request.user.is_following.all():
            user=useraccount.user
            name=user.username
            list_assignment=user.assignment_set.all()
            dictionary2[name]=list_assignment
        return render(request,'assignment/index.html',{'intrests':intrests,'dictionary2':dictionary2})
    else:
        list_jee = Assignment.objects.jee_main().order_by('-created')
        list_jee_adv = Assignment.objects.jee_adv().order_by('-created')
        list_ssc = Assignment.objects.ssc().order_by('-created')
        dictionary = {'JEE-Mains':list_jee,'JEE-Adv':list_jee_adv,'SSC':list_ssc}
        return render(request, 'assignment/index2.html', {'dictionary':dictionary})

def add_interest(request):
    if request.method=='POST':
        form=Interest_form(request.POST)
        if form.is_valid():
            intrest=form.save(commit=False)
            intrest.user=request.user
            intrest.save()
            return redirect(reverse('assignment:index'))
    else:
        form=Interest_form
    return render(request,'assignment/add_intrest_form.html',{'form': form})

class InterestDelete(DeleteView):
    model = Interests
    success_url = reverse_lazy('assignment:index')


def index_jee_main(request):
    heading='Jee-Main'
    list = Assignment.objects.jee_main().order_by('-created')
    return render(request, 'assignment/index_exam.html', {'heading':heading,'list': list})


def index_jee_adv(request):
    heading='Jee-Adv'
    list = Assignment.objects.jee_adv().order_by('-created')
    return render(request, 'assignment/index_exam.html', {'heading':heading,'list': list})


def index_ssc(request):
    heading = 'SSC'
    list = Assignment.objects.ssc().order_by('-created')
    return render(request, 'assignment/index_exam.html', {'heading':heading,'list': list})


def index_others(request):
    heading = 'Others'
    list = Assignment.objects.others().order_by('-created')
    return render(request, 'assignment/index_exam.html', {'heading':heading,'list': list})




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
    assignment=user.assignment_set.all()
    paginator = Paginator(assignment, 30)
    page = request.GET.get('page')
    assignment = paginator.get_page(page)
    return render(request,'assignment/my_assignment_page.html',{'assignment':assignment})


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


class AssignmentDelete(DeleteView):
    model = Assignment
    success_url = reverse_lazy('assignment:my_assignment_page')


def assignmentCreate(request):
    if request.method=='POST':
        form=AssignmentForm(request.POST)
        if form.is_valid():
            assignment=form.save(commit=False)
            assignment.user=request.user
            assignment.slug=slugify(assignment.title)
            assignment.save()
            slug="%s %s"%(assignment.title,assignment.id)
            assignment.slug=slugify(slug)
            assignment.save()
            return redirect(reverse('assignment:my_assignment_page'))
    else:
        form=AssignmentForm
    return render(request,'assignment/assignment_form.html',{'form': form})

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


def show_submission(request,pk):
    assignment = get_object_or_404(Assignment,pk=pk)
    submissions=Assignment_answered_by.objects.show_submission(pk).order_by('-marks')
    return render(request, 'assignment/show_submission.html', {'submissions': submissions,'assignment':assignment})



class QuestionView(DetailView):
    template_name = 'assignment/question_paper.html'
    model = Assignment


def assignment_preview(request,slug):
    assignment = get_object_or_404(Assignment, slug=slug)
    return render(request, 'assignment/assignment_preview.html', {'assignment': assignment})


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
    marks = 0
    total_marks=0
    forloopcounter = 1
    answersting =''
    for question in assignment.questions_set.all():

        post_input='inlineRadioOptions'+str(forloopcounter)

        answersting=answersting+request.POST[post_input]

        if request.POST[post_input]=='z':
         forloopcounter = forloopcounter + 1
         total_marks = total_marks+question.positive_marks

        elif question.answer==request.POST[post_input]:
         marks=marks+question.positive_marks
         forloopcounter = forloopcounter+1
         total_marks = total_marks + question.positive_marks

        elif question.answer!= request.POST[post_input]:
         marks = marks - question.negative_marks
         total_marks = total_marks + question.positive_marks
         forloopcounter = forloopcounter+1
    # print(answersting)
    # print(marks)
    if request.user.is_authenticated:
        p = Assignment_answered_by(name_of_assignment=assignment.title,assignment_id=assignment.id,
                                   name_of_teacher=assignment.user.first_name+" "+assignment.user.last_name,
                                   assigner_username=assignment.user.username,
                                   user=request.user,answer_string=answersting,
                                   marks=marks,total_marks=total_marks)
        p.save()
        return redirect(reverse('assignment:assignment_page'))
    else:
        return render(request,'assignment/result_not_logged_in.html',{'name_of_assignment':assignment.title,'assignment_id':assignment.id,
                                                                      'name_of_teacher':assignment.user.first_name+" "+assignment.user.last_name,
                                                                      'marks':marks,'total_marks':total_marks})

def answersheet(request,ass_id, ans_id):
    assignment=get_object_or_404(Assignment,pk=ass_id)#Assignment.objects.get(pk=ass_id)
    assignment_answered_by=get_object_or_404(Assignment_answered_by,pk=ans_id)#Assignment_answered_by.objects.get(pk=ans_id)
    answer= assignment_answered_by.answer_string
    list1 = []
    for i in answer:
        list1.append(i)
    return render(request,'assignment/answersheetpage.html', {'assignment':assignment,'answer':list1})


def add_workbook(request):
    if request.method=='POST':
        form=Workbook_Form(request.POST,request.FILES)
        if form.is_valid():
            workbook=form.save(commit=False)
            workbook.user = request.user
            workbook.slug=slugify(workbook.name)
            workbook.save()
            slug="%s %s"%(workbook.name,workbook.id)
            workbook.slug=slugify(slug)
            workbook.save()
            return redirect(reverse('assignment:workbook_list'))
    else:
        form=Workbook_Form()
    return render(request,'assignment/add_workbook.html',{'form':form})

def view_workbook_list(request,pk=None):
    if pk:
        user=get_object_or_404(User,pk=pk)#User.objects.get(pk=pk)
    else:
        user = request.user
    return render(request,'assignment/workbook_list.html',{'user':user,})

def view_workbook(request,slug):
    workbook=get_object_or_404(Workbook,slug=slug)#workbook.objects.get(pk=pk)
    workbook_pages=workbook.workbook_page_set.all
    user=workbook.user
    return render(request,'assignment/workbook.html',{'workbook':workbook,'workbook_pages':workbook_pages,'user':user})

def add_workbook_page(request,pk):
    if request.method == 'POST':
        form = Workbook_page_Form(request.POST,request.FILES)
        if form.is_valid():
            page=form.save(commit=False)
            page.workbook=get_object_or_404(Workbook,pk=pk)#workbook.objects.get(pk=pk)
            page.user = request.user
            page.slug=slugify(page.title)
            page.save()
            slug="%s %s"%(page.title,page.id)
            slug=slugify(slug)
            page.slug=slug
            page.save()
            return redirect(reverse('assignment:workbook_page',args=[slug]))
        else:
            messages.warning(request, "please correct the error below")
    else:
        form=Workbook_page_Form()
        return render(request,'assignment/add_workbook_page.html',{'form': form,})

def view_workbook_page(request,slug):
    page=get_object_or_404(Workbook_page,slug=slug)#workbook_page.objects.get(pk=pk)
    return render(request,'assignment/workbook_page.html',{'page':page})

def result(request):
    result=request.user.assignment_answered_by_set.order_by('-submitted')
    return render(request,'assignment/result.html',{'result':result,})


def index_booklet(request):
    list_booklet = []
    for useraccount in request.user.is_following.all():
        user=useraccount.user
        # print(user)
        for booklet in user.booklet_set.all():
            list_booklet.append(booklet)

    return render(request,'assignment/booklet.html',{'booklet':list_booklet})


def booklet(request):
    booklet = Booklet.objects.all()
    paginator = Paginator(booklet, 30)
    page = request.GET.get('page')
    booklet = paginator.get_page(page)
    return render(request,'assignment/booklet.html',{'booklet':booklet})

def booklet_preview(request,slug):
    booklet=get_object_or_404(Booklet,slug=slug)
    return render(request, 'assignment/booklet_preview.html',{'booklet':booklet})

def booklet_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            booklet=form.save(commit=False)
            booklet.user=request.user
            booklet.slug=slugify(booklet.name)
            booklet.save()
            slug = "%s %s %s"%(booklet.name,booklet.author,booklet.id)
            booklet.slug = slugify(slug)
            booklet.save()
            return redirect(reverse('assignment:my-booklet'))
    else:
        form = DocumentForm()
    return render(request, 'assignment/booklet_upload.html', {'form': form})


def my_booklet(request,pk=None):
    if pk:
        user = get_object_or_404(User,pk=pk)#User.objects.get(pk=pk)
    else:
        user = request.user
    booklet=user.booklet_set.all()
    paginator = Paginator(booklet, 30)
    page = request.GET.get('page')
    booklet = paginator.get_page(page)
    return render(request,'assignment/booklet.html',{'booklet':booklet})

class BookletUpdate(UpdateView):
    model = Booklet
    fields = ['name','subject','discription','link','image']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('assignment:my-booklet')


class BookletDelete(DeleteView):
    model = Booklet
    success_url = reverse_lazy('assignment:my-booklet')

################
# filter
###############

def filter_search(request):
    assignment_list = Assignment.objects.all()
    assignment_filter = AssignmentFilter(request.GET, queryset=assignment_list)
    return render(request,'assignment/user_list.html', {'filter': assignment_filter})

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
            booklet_results= Booklet.objects.search(query)
            useraccount_results=UserAccount.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                assignment_results,
                booklet_results,
                useraccount_results

            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        return Assignment.objects.none() # just an empty queryset as default

