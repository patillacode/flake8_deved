# Generated by Django 2.1.2 on 2019-04-25 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20190314_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlandingpage',
            name='quickstart_csharp',
        ),
        migrations.RemoveField(model_name='productlandingpage', name='quickstart_curl'),
        migrations.
        RemoveField(
            model_name='productlandingpage',
            name='quickstart_java',
        ),
    ]

    foo = None
    bar = 1

    if foo == bar:
        operations.append(migrations.RemoveField
        (
            model_name='productlandingpage',
            name='snippet_ruby',
        ))
