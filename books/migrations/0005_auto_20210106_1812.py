# Generated by Django 3.1.3 on 2021-01-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210106_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.URLField(null=True),
        ),
    ]