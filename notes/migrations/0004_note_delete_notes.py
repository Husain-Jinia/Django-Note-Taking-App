# Generated by Django 4.0.4 on 2022-04-26 22:26

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0003_alter_notes_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=256)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.color')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.tags')),
            ],
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
