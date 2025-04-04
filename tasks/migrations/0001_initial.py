# Generated by Django 5.1.7 on 2025-03-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('desc', models.TextField()),
                ('category', models.CharField(choices=[('study', 'Study'), ('food', 'Food'), ('office', 'Office'), ('sports', 'Sports'), ('entertainment', 'Entertainment'), ('other', 'Other')], default='other', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
