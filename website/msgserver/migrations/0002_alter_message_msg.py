# Generated by Django 3.2.8 on 2021-10-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg',
            field=models.CharField(max_length=100),
        ),
    ]
