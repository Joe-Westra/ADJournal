# Generated by Django 2.0.7 on 2018-07-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0003_auto_20180715_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='nightlystat',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
