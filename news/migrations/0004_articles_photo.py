# Generated by Django 4.0.5 on 2022-07-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_articles_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
