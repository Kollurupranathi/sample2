# Generated by Django 4.1.2 on 2022-11-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_que_email_que_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='que',
            name='name',
        ),
        migrations.AddField(
            model_name='que',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
