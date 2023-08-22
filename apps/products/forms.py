from django import forms
from apps.products.models import (BookCover, PrintBindingTypes, Product, PrintSize, PrintColor)


class ProductUpdateForm(forms.ModelForm):
    printSize = forms.Field(
        widget=forms.Select(
            choices=PrintSize.choices, attrs={"class": "form-control"}
        ),
    )
    printColor = forms.Field(
        widget=forms.Select(
            choices=PrintColor.choices, attrs={"class": "form-control"}
        ),
    )
    printBindingType = forms.ModelChoiceField(
        queryset=PrintBindingTypes.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )
    # printBindingType = forms.Field(
    #     widget=forms.Select(
    #         choices=PrintBindingTypes.choices, attrs={"class": "form-control"}
    #     ),
    # )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"}), required=True
    )

    class Meta:
        model = Product
        fields = [
            "printSize",
            "printColor",
            "printBindingType",
            "price",
            # "photo",
        ]


class ProductCreateForm(forms.ModelForm):
    printSize = forms.Field(
        widget=forms.Select(
            choices=PrintSize.choices, attrs={"class": "form-control"}
        ),
    )
    printColor = forms.Field(
        widget=forms.Select(
            choices=PrintColor.choices, attrs={"class": "form-control"}
        ),
    )
    bookCover = forms.Field(
        widget=forms.Select(
            choices=BookCover.choices, attrs={"class": "form-control"}
        ),
    )

    printBindingType = forms.ModelChoiceField(
        queryset=PrintBindingTypes.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"}), required=True
    )

    # photo = forms.FileField(
    #     widget=forms.FileInput(attrs={"class": "form-control"}), required=True
    # )

    class Meta:
        model = Product
        fields = [
            "printSize",
            "printColor",
            "bookCover",
            "printBindingType",

            "price",
            # "photo",
        ]

    # widgets = {
    #     "photo": forms.FileInput(attrs={"class": "form-control"}),

    # }