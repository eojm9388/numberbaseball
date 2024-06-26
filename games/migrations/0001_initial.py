# Generated by Django 4.2.11 on 2024-04-17 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Player2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Expect2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expect', models.CharField(max_length=4)),
                ('status', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.player2')),
            ],
        ),
        migrations.CreateModel(
            name='Expect1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expect', models.CharField(max_length=4)),
                ('status', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.player1')),
            ],
        ),
    ]
