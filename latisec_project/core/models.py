from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="FontAwesome icon class")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField(max_length=300)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_responded = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"


class GetProtectedRequest(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic Protection'),
        ('advanced', 'Advanced Protection'),
        ('enterprise', 'Enterprise Protection'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    employees = models.IntegerField(help_text="Number of employees")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company} - {self.plan}"