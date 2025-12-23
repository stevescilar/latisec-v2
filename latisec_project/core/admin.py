from django.contrib import admin
from .models import Service, BlogPost, ContactSubmission, GetProtectedRequest


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'is_published']
    list_filter = ['is_published', 'published_date']
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'created_at', 'is_responded']
    list_filter = ['is_responded', 'created_at']
    search_fields = ['name', 'email', 'company', 'message']
    date_hierarchy = 'created_at'


@admin.register(GetProtectedRequest)
class GetProtectedRequestAdmin(admin.ModelAdmin):
    list_display = ['company', 'name', 'email', 'plan', 'employees', 'created_at', 'is_contacted']
    list_filter = ['plan', 'is_contacted', 'created_at']
    search_fields = ['company', 'name', 'email']
    date_hierarchy = 'created_at'