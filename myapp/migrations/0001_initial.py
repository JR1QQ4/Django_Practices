# Generated by Django 3.2.12 on 2022-04-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
