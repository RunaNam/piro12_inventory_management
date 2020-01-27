# Generated by Django 2.2.9 on 2020-01-24 09:40

from django.db import migrations, models
import piro.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('price', models.PositiveIntegerField()),
                ('desc', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to=piro.utils.uuid_upload_to)),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
    ]
