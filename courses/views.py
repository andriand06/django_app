from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from .models import Course
from django.conf import settings
from django.http import Http404

# Create your views here.
def index(request):
    context = {}
    if request.method == 'GET':
        # get the top 10 courses with the highest enrollment
        courses = Course.objects.order_by('-total_enrollment')[:10]
        context['courses'] = courses
        context['MEDIA_URL'] = '/static'+ settings.MEDIA_URL
        return render(request, 'courses/course_list.html', context)
    
    
def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
               "</html>".format(today)
    return HttpResponse(content=template)

def enroll(request, course_id):
    if request.method == 'POST':
        # First try to read the course object
        # If could be found, raise a 404 exception
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()
        # always return an HttpResponseRedirect after successfully dealing with POST data.
        # We using reverse() to get the URL of the index view
        return HttpResponseRedirect(reverse(viewname='courses:course_details', args=(course.id,)))
    else:
        return HttpResponse("Invalid request")
    
def course_details(request, course_id):
    context = {}
    if request.method == 'GET':
        try:
            course = Course.objects.get(pk=course_id)
            context['course'] = course
            return render(request, 'courses/course_detail.html', context)
        except Course.DoesNotExist:
            raise Http404("Course does not exist")