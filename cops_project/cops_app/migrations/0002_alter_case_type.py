# Generated by Django 4.2.6 on 2024-01-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cops_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='type',
            field=models.CharField(blank=True, choices=[('murder', 'murder'), ('kidnapping', 'kidnapping'), ('damaging property', 'damaging property'), ('rape', 'rape'), ('physical or mental abuse', 'physical or mental abuse'), ('theft', 'theft'), ('others', 'others')], max_length=50, null=True),
        ),
    ]