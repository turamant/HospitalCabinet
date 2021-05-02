# Generated by Django 3.2 on 2021-04-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_auto_20210429_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentpacient',
            old_name='doctor',
            new_name='pacient',
        ),
        migrations.AddField(
            model_name='documentpacient',
            name='title',
            field=models.CharField(default='kiss', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='photodoctor',
            name='title',
            field=models.CharField(default='kiss', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='documentpacient',
            name='url',
            field=models.SlugField(max_length=200),
        ),
    ]