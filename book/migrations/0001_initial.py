# Generated by Django 4.1 on 2022-11-02 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('author_name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('Type_of_Book', models.CharField(choices=[('non-fiction', 'Non-Fiction'), ('edited', 'Edited'), ('reference', 'Reference'), ('fiction', 'Fiction')], max_length=20)),
            ],
        ),
    ]