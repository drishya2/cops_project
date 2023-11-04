# Generated by Django 4.2.6 on 2023-11-03 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cops_app', '0004_my_user_type_delete_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='police',
            old_name='cases',
            new_name='no_cases',
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('police', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cops_app.police')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cops_app.my_user')),
            ],
        ),
    ]