# Generated by Django 4.1.6 on 2023-02-02 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0002_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(max_length=20)),
                ('salary', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_field', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('contact', models.IntegerField()),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Birthday',
        ),
        migrations.DeleteModel(
            name='Identity',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.AddField(
            model_name='gender',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FIRSTAPPLICATION.person'),
        ),
        migrations.AddField(
            model_name='employee',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FIRSTAPPLICATION.person'),
        ),
    ]
