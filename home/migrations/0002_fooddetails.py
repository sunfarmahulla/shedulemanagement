# Generated by Django 2.2 on 2019-04-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=50000)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
