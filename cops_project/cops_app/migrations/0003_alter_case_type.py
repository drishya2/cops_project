# Generated by Django 4.2.6 on 2024-01-18 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cops_app', '0002_alter_case_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='type',
            field=models.CharField(blank=True, choices=[('m', 'murder'), ('k', 'kidnapping'), ('d', 'damaging property'), ('r', 'rape'), ('p', 'physical or mental abuse'), ('t', 'theft'), ('o', 'others')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]