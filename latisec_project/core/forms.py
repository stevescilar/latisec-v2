from django import forms
from .models import ContactSubmission, GetProtectedRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'company', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com',
                'required': True
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name (Optional)'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 123-4567'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Tell us about your security needs...',
                'required': True
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'company': 'Company',
            'phone': 'Phone Number',
            'message': 'Message',
        }


class GetProtectedForm(forms.ModelForm):
    class Meta:
        model = GetProtectedRequest
        fields = ['name', 'email', 'company', 'phone', 'plan', 'employees', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com',
                'required': True
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 123-4567',
                'required': True
            }),
            'plan': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'employees': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 50',
                'min': '1',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Any specific security concerns or requirements?'
            }),
        }