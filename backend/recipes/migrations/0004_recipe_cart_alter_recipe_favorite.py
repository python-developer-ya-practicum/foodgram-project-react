# Generated by Django 4.1.3 on 2022-11-07 04:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0003_recipe_favorite"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="cart",
            field=models.ManyToManyField(
                related_name="carts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="В корзине у пользователей",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="favorite",
            field=models.ManyToManyField(
                related_name="favorites",
                to=settings.AUTH_USER_MODEL,
                verbose_name="В избранном у пользователей",
            ),
        ),
    ]