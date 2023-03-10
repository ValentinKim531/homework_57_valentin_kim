# Generated by Django 4.1.6 on 2023-03-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_issue_deleted_at_issue_is_deleted_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-created_at'], 'verbose_name': 'Проблема', 'verbose_name_plural': 'Проблемы'},
        ),
        migrations.RemoveField(
            model_name='issue',
            name='type',
        ),
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.ManyToManyField(related_name='issues', to='webapp.type', verbose_name='Тип'),
        ),
    ]
