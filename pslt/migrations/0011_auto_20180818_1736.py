# Generated by Django 2.0.6 on 2018-08-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pslt', '0010_document_page_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='short_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
