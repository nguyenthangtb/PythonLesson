# Generated by Django 2.2.7 on 2020-02-19 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('Description', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('passcode', models.CharField(max_length=255)),
                ('devices', models.IntegerField(default=0)),
                ('organization', models.IntegerField(default=0)),
            ],
        ),
    ]