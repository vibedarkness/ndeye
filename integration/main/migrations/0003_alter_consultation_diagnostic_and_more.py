# Generated by Django 4.2.2 on 2023-06-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_medecin_email_alter_medecin_genre_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultation",
            name="diagnostic",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="dosage",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="intitule",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="departement",
            name="nom",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="medecin",
            name="nom",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="medecin",
            name="prenom",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="medicament",
            name="nom",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="patient",
            name="adresse",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="patient",
            name="nom",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="patient",
            name="photo",
            field=models.ImageField(max_length=200, upload_to=""),
        ),
        migrations.AlterField(
            model_name="patient",
            name="prenom",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="service",
            name="nom",
            field=models.CharField(max_length=100),
        ),
    ]
