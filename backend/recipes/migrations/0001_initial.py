# Generated by Django 4.1.3 on 2022-11-06 21:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=128, verbose_name="Название ингридиента"
                    ),
                ),
                (
                    "measurement_unit",
                    models.CharField(max_length=16, verbose_name="Единицы измерения"),
                ),
            ],
            options={
                "verbose_name": "Ингридиент",
                "verbose_name_plural": "Ингридиенты",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Название рецепта"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="recipes/images", verbose_name="Изображение рецепта"
                    ),
                ),
                ("text", models.TextField(verbose_name="Описание рецепта")),
                (
                    "cooking_time",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=1,
                                message="Время приготовления должно быть больше 1 минуты",
                            )
                        ],
                        verbose_name="Время приготовления в минутах",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор рецепта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=32, unique=True, verbose_name="Название тега"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=32, unique=True, verbose_name="Slug тега"
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"),
                                "Введите корректный цветовой hex-код (например, #49B64E)",
                            )
                        ],
                        verbose_name="Цвет тега",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="RecipeIngredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=1, message="Количество должно быть больше 1"
                            )
                        ],
                        verbose_name="Количество",
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes_ingredients",
                        to="recipes.ingredient",
                        verbose_name="Ингридиент",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes_ingredients",
                        to="recipes.recipe",
                        verbose_name="Рецепт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт и ингридиент",
                "verbose_name_plural": "Рецепты и ингридиенты",
                "ordering": ["-id"],
            },
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                through="recipes.RecipeIngredient",
                to="recipes.ingredient",
                verbose_name="Ингредиенты рецепта",
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(to="recipes.tag", verbose_name="Теги рецепта"),
        ),
        migrations.AddConstraint(
            model_name="ingredient",
            constraint=models.UniqueConstraint(
                fields=("name", "measurement_unit"), name="unique ingredient"
            ),
        ),
        migrations.AddConstraint(
            model_name="recipeingredient",
            constraint=models.UniqueConstraint(
                fields=("recipe", "ingredient"), name="unique recipe ingredient"
            ),
        ),
    ]
