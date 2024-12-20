# Generated by Django 5.0.4 on 2024-11-16 06:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='client_name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
