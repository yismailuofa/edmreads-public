# Generated by Django 3.1.3 on 2021-01-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authour',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='dsc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
