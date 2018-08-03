# Generated by Django 2.0.7 on 2018-07-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20180715_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nightlystat',
            name='mood',
        ),
        migrations.AddField(
            model_name='nightlystat',
            name='mood_sleep',
            field=models.CharField(choices=[('upset', 'Upset'), ('irrit', 'Irritated'), ('sombe', 'Somber'), ('distr', 'Distracted'), ('nuetr', 'Nuetral'), ('happy', 'Happy'), ('posit', 'Positive'), ('joyfu', 'Joyful'), ('elate', 'Elated'), ('bliss', 'Blissful'), ('maxim', 'Top of the World')], default='neutr', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nightlystat',
            name='mood_wake',
            field=models.CharField(choices=[('upset', 'Upset'), ('irrit', 'Irritated'), ('sombe', 'Somber'), ('distr', 'Distracted'), ('nuetr', 'Nuetral'), ('happy', 'Happy'), ('posit', 'Positive'), ('joyfu', 'Joyful'), ('elate', 'Elated'), ('bliss', 'Blissful'), ('maxim', 'Top of the World')], default='neutr', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nightlystat',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]