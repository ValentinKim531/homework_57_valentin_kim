# Generated by Django 4.1.6 on 2023-03-01 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
            options={
                'verbose_name': 'Проблема',
                'verbose_name_plural': 'Проблемы',
            },
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип', 'verbose_name_plural': 'Типы'},
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Статус'),
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='issues', to='webapp.status', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='issues', to='webapp.type', verbose_name='Тип'),
        ),
    ]
