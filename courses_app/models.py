from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self,post_data):
        errors = {}

        if len(post_data['name'])<5:
            errors['name'] = "Course name must be at least 5 characters"

        if len(post_data['description'])<15:
            errors['description'] = "Course description must be at least 15 characters"

        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()