from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('get-protected/', views.get_protected, name='get_protected'),
    
    # Services
    path('security-awareness/', views.security_awareness, name='security_awareness'),
    path('compliance-and-governance/', views.compliance_governance, name='compliance_governance'),
    path('vulnerability-assessments/', views.vulnerability_assessments, name='vulnerability_assessments'),
    path('security-architecture/', views.security_architecture, name='security_architecture'),
    path('threat-intelligence/', views.threat_intelligence, name='threat_intelligence'),
]