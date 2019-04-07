# Generated by Django 2.1.7 on 2019-04-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferCredits', '0003_auto_20190406_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfercredit',
            name='equivalentToCat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transfercredit',
            name='equivalentToDept',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='transfercredit',
            name='equivalentToID',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
