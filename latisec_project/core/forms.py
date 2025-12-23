from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import ContactSubmission, GetProtectedRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ["name", "email", "company", "phone", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="form-group col-md-6 mb-3"),
                Column("email", css_class="form-group col-md-6 mb-3"),
            ),
            Row(
                Column("company", css_class="form-group col-md-6 mb-3"),
                Column("phone", css_class="form-group col-md-6 mb-3"),
            ),
            Field("message", css_class="form-group mb-3"),
            Submit("submit", "Send Message", css_class="btn btn-primary btn-lg"),
        )


class GetProtectedForm(forms.ModelForm):
    class Meta:
        model = GetProtectedRequest
        fields = ["name", "email", "company", "phone", "plan", "employees", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="form-group col-md-6 mb-3"),
                Column("email", css_class="form-group col-md-6 mb-3"),
            ),
            Row(
                Column("company", css_class="form-group col-md-6 mb-3"),
                Column("phone", css_class="form-group col-md-6 mb-3"),
            ),
            Row(
                Column("plan", css_class="form-group col-md-6 mb-3"),
                Column("employees", css_class="form-group col-md-6 mb-3"),
            ),
            Field("message", css_class="form-group mb-3"),
            Submit(
                "submit", "Request Protection Plan", css_class="btn btn-primary btn-lg"
            ),
        )
