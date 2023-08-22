from django.contrib import auth, messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import (TemplateView)

from apps.products.models import Product, PrintColor, PrintBindingTypes, PrintSize, BookCover
from utils.helpers import is_ajax


# Create your views here.


def login_request(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST.get("username"), password=request.POST.get("password")
        )

        if user is not None:
            # auth.login(request, user)
            return redirect("accounts:admin_dashboard")
        else:
            messages.error(request, "Неправильное имя пользователя или пароль")
            return redirect("accounts:login")

    if request.user.is_authenticated:
        return redirect("accounts:admin_dashboard")

    return render(request, "accounts/login.html")


def logout(request):
    auth.logout(request)
    return redirect("accounts:main_page")


class MainDashboard(TemplateView):
    template_name = "dashboard/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["print_size"] = PrintSize.choices
        context["print_color"] = PrintColor.choices
        context["print_cover"] = BookCover.choices
        context["binding_types"] = PrintBindingTypes.objects.all()
        return context


mainpage = MainDashboard.as_view()


class AdminDashboard(TemplateView):
    template_name = "base.html"


admin_dashboard = AdminDashboard.as_view()


class InitialCalculationView(TemplateView):
    model = Product

    def post(self, request, *args, **kwargs):
        if is_ajax(request):

            product_list = Product.productListByUser.by_creator(request.user.id)
            page_amount = int(request.POST.get('page_amount'))
            page_size = int(request.POST.get('page_size'))
            color = int(request.POST.get('color'))
            cover = int(request.POST.get('cover'))
            binding = PrintBindingTypes.objects.get(id=int(request.POST.get('binding')))
            cost = 0
            for product in product_list:
                if product.printSize == page_size and product.printColor == color and product.bookCover == cover and product.printBindingType == binding:
                    cost = page_amount * product.price

            return JsonResponse(
                {"success": True, "data": cost}
            )
        return JsonResponse({"success": False, "data": None})


initial_calculation = InitialCalculationView.as_view()
