# Generated by Django 4.2.10 on 2024-03-01 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Japa', '0014_alter_nytmad_beskrivelse'),
    ]

    operations = [
        migrations.CreateModel(
            name='NyBestilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leveringsadresse', models.TextField()),
                ('Leveringsadresse_type', models.CharField(blank=True, choices=[('house', 'House'), ('apartment', 'Apartment'), ('office', 'Office'), ('other', 'Other')], max_length=20, null=True)),
                ('Dørnummer', models.CharField(blank=True, max_length=10, null=True)),
                ('Leveringsgebyr', models.FloatField()),
                ('Total_pris', models.FloatField()),
                ('Leverings_tid', models.DateTimeField()),
                ('Bestillings_tid', models.DateTimeField(auto_now_add=True)),
                ('Leveret', models.BooleanField(default=False)),
                ('Afhentet', models.BooleanField(default=False)),
                ('Annulleret', models.BooleanField(default=False)),
                ('Kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Mad', models.ManyToManyField(to='Japa.nytmad')),
                ('Restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Japa.nyrestaurant')),
            ],
        ),
    ]
