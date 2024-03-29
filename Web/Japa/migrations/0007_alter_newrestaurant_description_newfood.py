# Generated by Django 4.2.9 on 2024-02-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Japa', '0006_remove_newrestaurant_foodtype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newrestaurant',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='NewFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.BinaryField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('categories', models.ManyToManyField(to='Japa.newcategory')),
            ],
        ),
    ]
