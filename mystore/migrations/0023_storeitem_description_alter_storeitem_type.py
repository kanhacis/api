# Generated by Django 4.0.3 on 2024-03-28 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0022_alter_storeitem_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='storeitem',
            name='type',
            field=models.CharField(blank=True, choices=[('School Book', 'School Book'), ('Syllabus Book', 'Syllabus Book'), ('College Book', 'College Book'), ('Notes', 'Notes'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
