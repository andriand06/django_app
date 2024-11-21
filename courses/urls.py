from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'courses'
# We are defining the URL patterns for the courses app and linking them to the views
# Also, we are serving the media and static files in development
# settings variables comes from settings.py file
urlpatterns = [
    # Create a path object defining the URL pattern to the index view
    path(route='', view=views.index, name='index'),
    path(route='date', view=views.get_date, name='date'),
    path(route='course/<int:course_id>/enroll', view=views.enroll, name='enroll'),
    path(route='course/<int:course_id>', view=views.course_details, name='course_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)