# Generated by Django 2.0.7 on 2018-11-30 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_ask'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_test', models.CharField(max_length=25)),
                ('ask', models.CharField(max_length=50)),
                ('answer_1', models.TextField()),
                ('answer_2', models.TextField()),
                ('answer_3', models.TextField()),
                ('answer_4', models.TextField()),
                ('answer_5', models.TextField()),
                ('answer_6', models.TextField()),
            ],
        ),
    ]
