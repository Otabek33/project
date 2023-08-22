from django.urls import reverse
from datetime import datetime
from django.db import models
from apps.accounts.models import CustomUser, Company
from django.utils.translation import gettext_lazy as _
import uuid


class PrintSize(models.IntegerChoices):
    SIZE_A4 = 1, _("A4")
    SIZE_A5 = 2, _("A5")


class PrintColor(models.IntegerChoices):
    BLACK = 1, _("Черно-белый")
    COLORFUL = 2, _("Цветной")


class BookCover(models.IntegerChoices):
    PERFECT_COVER = 1, _("Мягкий")
    HARD_COVER = 2, _("Твердый")
    PLASTIC_COVER = 3, _("Пластиковый ")


# class PageQuality(models.IntegerChoices):
#     GAZET = 1,_("газетная")
#     OFSET =2,_("офсетная")
#     MELOVAN =3,_("мелованная")
#     KRAFT=4,_("крафт")


class ProductManager(models.Manager):
    """nimadur"""

    def by_creator(self, user):
        return super().get_queryset().filter(deleted_status=False, created_by=user).order_by('-created_at')

    def by_id(self, id):
        return super().get_queryset().get(pk=id)


class PrintBindingTypes(models.Model):
    name = models.CharField(_("name"), max_length=150, blank=True)
    photo = models.FileField(upload_to="binding/%Y/%m/%d/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип переплета печати"
        verbose_name_plural = "Типы переплета печати"


# Create your models here.
class Product(models.Model):
    """nimadur"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    printSize = models.IntegerField(
        choices=PrintSize.choices,
        default=PrintSize.SIZE_A4,
    )
    bookCover = models.IntegerField(
        choices=BookCover.choices,
        default=BookCover.PERFECT_COVER,
    )

    printColor = models.IntegerField(
        choices=PrintColor.choices,
        default=PrintColor.BLACK,
    )
    printBindingType = models.ForeignKey(PrintBindingTypes,
                                         on_delete=models.CASCADE,
                                         blank=True,
                                         null=True,
                                         related_name="printBindingTypes", )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                related_name="company", )

    productListByUser = ProductManager()

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="_created_by",
    )
    created_at = models.DateTimeField(default=datetime.now)
    updated_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="_updated_by",
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Size - {self.get_printSize_display()} \n; Color - {self.get_printColor_display()} ; Binding  - {self.printBindingType.name} ; Price  - {str(self.price)};"

    def get_absolute_url(self):
        return reverse("products:product_list")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"