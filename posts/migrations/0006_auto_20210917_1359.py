# Generated by Django 3.2.7 on 2021-09-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_instas_analysis_post_insta_analysis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='insta_analysis',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(default=''),
        ),
    ]