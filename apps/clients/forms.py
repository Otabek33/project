from django import forms
from apps.clients.models import Client


class ClientCreateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    userId = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )

    photo = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control"}), required=True
    )

    class Meta:
        model = Client
        fields = [
            "username",
            "first_name",
            "last_name",
            "userId",
            "photo",
            "phone",
        ]

    widgets = {
        "photo": forms.FileInput(attrs={"class": "form-control"}),

    }


class ClientUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    userId = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=True
    )

    class Meta:
        model = Client
        fields = [
            "username",
            "first_name",
            "last_name",
            "userId",
            "photo",
            "phone",
        ]

    widgets = {
        "photo": forms.FileInput(attrs={"class": "form-control"}),

    }