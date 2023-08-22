# Generated by Django 4.2.4 on 2023-08-22 05:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at "),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="Update at"),
                ),
                ("deleted_status", models.BooleanField(default=False)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("order_number", models.IntegerField(default=0)),
                (
                    "printSize",
                    models.IntegerField(choices=[(1, "A4"), (2, "A5")], default=1),
                ),
                (
                    "printColor",
                    models.IntegerField(
                        choices=[(1, "Черно-белый"), (2, "Цветной")], default=1
                    ),
                ),
                ("file", models.FileField(upload_to="uploads/%Y/%m/%d/")),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("page_number", models.IntegerField()),
                (
                    "order_status",
                    models.IntegerField(
                        choices=[
                            (1, "В создании"),
                            (2, "В подтверждении"),
                            (3, "Активный"),
                            (4, "Отменено"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="order_created_by",
                        to="clients.client",
                        verbose_name="Created by",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="order_updated_by",
                        to="clients.client",
                        verbose_name="Updated by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
            },
        ),
    ]