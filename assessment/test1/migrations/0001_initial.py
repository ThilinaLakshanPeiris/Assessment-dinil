# Generated by Django 4.2.3 on 2023-09-14 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Answers', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_Areas',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Class', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Subject', models.CharField(max_length=255)),
                ('Subject_score', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('Summary_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Sydney_Participant', models.CharField(max_length=255)),
                ('Syndey_Percentile', models.CharField(max_length=255)),
                ('Correct_answer_percentage_per_class', models.CharField(max_length=255)),
                ('Correct_Answer', models.CharField(max_length=255)),
                ('Participant', models.CharField(max_length=255)),
                ('Student_score', models.CharField(max_length=255)),
                ('Category_Id', models.CharField(max_length=255)),
                ('Year_level_name', models.CharField(max_length=255)),
                ('Correct_answer_Id', models.CharField(max_length=255)),
                ('Answer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Answers_id', to='test1.answers')),
                ('Assessment_Areas_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assessment_Areas_id', to='test1.assessment_areas')),
                ('Award_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Awards_id', to='test1.awards')),
                ('Class_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Class_id', to='test1.class')),
                ('School_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_id', to='test1.school')),
                ('Student_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_id', to='test1.student')),
                ('Subject_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subject_id', to='test1.subject')),
            ],
        ),
    ]