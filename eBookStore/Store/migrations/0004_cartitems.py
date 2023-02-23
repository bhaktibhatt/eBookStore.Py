# Generated by Django 4.1.7 on 2023-02-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_rename_cvr_url_ebook_cover_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
    ]
