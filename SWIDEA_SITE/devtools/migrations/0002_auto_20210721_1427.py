# Generated by Django 3.2.5 on 2021-07-21 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devtools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devtool',
            old_name='tool_desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='devtool',
            old_name='type',
            new_name='kind',
        ),
        migrations.RenameField(
            model_name='devtool',
            old_name='tool_name',
            new_name='name',
        ),
    ]
