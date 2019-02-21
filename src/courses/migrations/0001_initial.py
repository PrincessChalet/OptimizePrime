# Generated by Django 2.1.7 on 2019-02-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.PositiveSmallIntegerField()),
                ('courseDept', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=30)),
                ('prereqCount', models.PositiveSmallIntegerField()),
                ('category', models.CharField(max_length=30)),
                ('hours', models.PositiveSmallIntegerField()),
                ('semester', models.CharField(choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Both', 'Both')], default='Both', max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]