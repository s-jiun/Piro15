# Generated by Django 3.2.5 on 2021-07-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20210721_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='devtools',
            field=models.CharField(choices=[('django', 'django')], max_length=50, null=True),
        ),
    ]
