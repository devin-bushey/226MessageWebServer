# Generated by Django 3.2.8 on 2021-10-26 19:29

from django.db import migrations, models
import msgserver.models


class Migration(migrations.Migration):

    dependencies = [
        ('msgserver', '0003_alter_message_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='key',
            field=models.IntegerField(validators=[msgserver.models.validate_key_alphanum, msgserver.models.validate_key_length, msgserver.models.validate_key_unique]),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg',
            field=models.TextField(validators=[msgserver.models.validate_msg_length]),
        ),
    ]
