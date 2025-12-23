from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Service, BlogPost
from .forms import ContactForm, GetProtectedForm


def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    context = {
        "services": services,
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def blog(request):
    blog_posts = BlogPost.objects.filter(is_published=True)
    paginator = Paginator(blog_posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "blog.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    recent_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:3]

    context = {
        "post": post,
        "recent_posts": recent_posts,
    }
    return render(request, "blog_detail.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thank you for contacting us! We will get back to you soon."
            )
            return redirect("contact")
    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, "contact.html", context)


def get_protected(request):
    if request.method == "POST":
        form = GetProtectedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your request has been submitted! Our team will contact you shortly.",
            )
            return redirect("get_protected")
    else:
        form = GetProtectedForm()

    context = {
        "form": form,
    }
    return render(request, "get_protected.html", context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    other_services = Service.objects.filter(is_active=True).exclude(id=service.id)[:3]

    context = {
        "service": service,
        "other_services": other_services,
    }
    return render(request, "service_detail.html", context)


def security_awareness(request):
    return render(request, "services/security_awareness.html")


def compliance_governance(request):
    return render(request, "services/compliance_governance.html")


def vulnerability_assessments(request):
    return render(request, "services/vulnerability_assessments.html")


def security_architecture(request):
    return render(request, "services/security_architecture.html")


def threat_intelligence(request):
    return render(request, "services/threat_intelligence.html")
