# Generated by Django 5.1.3 on 2024-11-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_image_alter_instructor_total_learners'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='total_enrollment',
            field=models.IntegerField(default=0),
        ),
    ]
