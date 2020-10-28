# Generated by Django 3.1 on 2020-10-28 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20201024_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog_app.post')),
            ],
            options={
                'ordering': ('criado',),
            },
        ),
    ]