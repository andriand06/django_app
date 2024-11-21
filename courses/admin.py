from django.contrib import admin
from .models import Course, Instructor, Lesson
# Register your models here.

# Create a class to add lessons to the course detail view
# Inline class Allow you to include related model instances in the same page/form as the parent model, instead of switching between different forms or screens.
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    # Fields to display in the detail view
    fields = ['pub_date', 'name', 'image', 'description']
    # Add a list of lessons to the detail view
    inlines = [LessonInline]
    # Fields to display in the list view
    list_display = ['name', 'pub_date']
    # Add a filter fields to the list view
    list_filter = ['pub_date']
    # Add a search fields to the list view
    search_fields = ['name']

class InstructorAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    # we can add parent model field as a field in the child model
    fields = ['first_name', 'last_name', 'dob','full_time']
    list_display = ['first_name', 'last_name', 'full_time']
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)