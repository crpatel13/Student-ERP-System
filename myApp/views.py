from django.shortcuts import render

# Create your views here.
# Import necessary classes
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from myApp.forms import TopicForm, InterestForm
from myApp.models import Author, Book, Course, Topic
from django.shortcuts import get_object_or_404

# Create your views here.
# def index(request):
#     courselist = Course.objects.all() [:10]
#     authorlist = Author.objects.all().order_by('-birthdate') [:5]
#     response = HttpResponse()
#     heading1 = '<p>' + 'List of courses: ' + '</p>'
#     response.write(heading1)
#     for course in courselist:
#         para = '<p>' + str(course) + ' ' + str(course.course_no)+ '</p>'
#         response.write(para)
#
#     heading2 = '<br> <p>' + 'List of Authors: ' + '</p>'
#     response.write(heading2)
#     for author in authorlist:
#         aut = '<p>' + str(author) + '</p>'
#         response.write(aut)
#
#     return response
#
#
# def about(request):
#     response = HttpResponse()
#     heading3 = '<p>' + 'This is a Course Listing App' + '</p>'
#     response.write(heading3)
#
#     return response
#
#
# def detail(request, title):
#     response = HttpResponse()
#     course = get_object_or_404(Course, title=title)
#     response.write('<p>' + 'Detail of course number' + '</p>' + title)
#     response.write('<p>' + 'Title:' + str(course.title) + '</p>')
#     response.write('<p>' + 'Textbook:' + str(course.textbook) + '</p>')
#     return response

def about(request):
    response = HttpResponse()
    return render(request,'myApp/about0.html')
    response.write('This is a Course Listing APP.')
    #return render(request, 'myapp/about0.html')
    return response

def detail(request,course_no):
    response = HttpResponse()
    course = get_object_or_404(Course, course_no=course_no)
    response.write('<p>' + 'Detail of course number' + '</p>' + course_no)
    response.write('<p>' + 'Title:' + course.title + '</p>')
    response.write('<p>' + 'Textbook:' + str(course.textbook) + '</p>')
    return render(request, 'myApp/detail.html',{ 'course_no':course_no,'Title':course.title,'Textbook':course.textbook})

def index(request):
        courselist = Course.objects.all().order_by('title')[:10]
        return render(request, 'myApp/index.html', {'courselist': courselist})


def topics(request):
    topiclist = Topic.objects.all()[:10]
    return render(request, 'myApp/topics.html',{'topiclist':   topiclist})


def addtopic(request):
    #topiclist = Topic.objects.all()[:10]
    #return render(request, 'myApp/topic.html',{'topiclist':   topiclist})
    response = HttpResponse()
    # response.write('<p>' + 'You can add a new topic here' + '</p>')
    # return response
    topiclist = Topic.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.num_responses = 1
            topic.save()
            return HttpResponseRedirect(reverse('myApp:topics'))
    else:
        form = TopicForm()
    return render(request, 'myApp/addtopic.html', {'form': form, 'topiclist': topiclist})


def topicdetail(request,topic_id):
    topiclist=get_object_or_404(Topic, pk=topic_id)
    if request.method=='POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['interested']=="1":
                topiclist.num_responses += 1
                avg_age=topiclist.avg_age
                entered_age=form.cleaned_data['age']
                avg_age = (int(avg_age) + int(entered_age))/2
                topiclist.avg_age=avg_age
                topiclist.save()
            return HttpResponseRedirect(reverse('myApp:topics'))
    else:
        form=InterestForm()
    return render(request, 'myApp/topicdetail.html', {'form':form, 'topiclist':topiclist})
