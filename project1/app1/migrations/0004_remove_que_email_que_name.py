# Generated by Django 4.1.2 on 2022-11-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_que_name_que_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='que',
            name='email',
        ),
        migrations.AddField(
            model_name='que',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
