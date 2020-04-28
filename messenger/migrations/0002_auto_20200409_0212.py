# Generated by Django 2.2 on 2020-04-09 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_description'),
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='sending_user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='recieving_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='r_messages', to='login.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='sending_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='s_messages', to='login.User'),
            preserve_default=False,
        ),
    ]