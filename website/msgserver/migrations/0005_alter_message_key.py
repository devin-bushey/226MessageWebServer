# Generated by Django 3.2.8 on 2021-10-26 19:34

from django.db import migrations, models
import msgserver.models


class Migration(migrations.Migration):

    dependencies = [
        ('msgserver', '0004_auto_20211026_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='key',
            field=models.CharField(max_length=8, validators=[msgserver.models.validate_key_alphanum, msgserver.models.validate_key_length, msgserver.models.validate_key_unique]),
        ),
    ]