# Generated by Django 3.2.9 on 2021-12-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
