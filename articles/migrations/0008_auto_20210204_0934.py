# Generated by Django 3.1.4 on 2021-02-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20210204_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='noimage2.png', upload_to=''),
        ),
    ]
