from django.db import models

# Create your models here.
class School(models.Model):
  ID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255)

  def __str__(self):
             # this code shows the outpot in the admin panel
     return '{} {}'.format(self.ID,self.Name)

class Class(models.Model):
  ID = models.AutoField(primary_key=True)
  Class = models.CharField(max_length=50)

  def __str__(self):
              # this code shows the outpot in the admin panel
        return '{} {}'.format(self.ID,self.Class)


class Assessment_Areas(models.Model):
  ID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255)

  def __str__(self):
              # this code shows the outpot in the admin panel
        return '{} {}'.format(self.ID,self.Name)

class Student(models.Model):
  ID = models.AutoField(primary_key=True)
  Fullname = models.CharField(max_length=255)

  def __str__(self):
              # this code shows the outpot in the admin panel
        return '{} {}'.format(self.ID,self.Fullname)

class Answers(models.Model):
  ID = models.AutoField(primary_key=True)
  Answers = models.CharField(max_length=255)

  def __str__(self):
              # this code shows the outpot in the admin panel
        return '{} {}'.format(self.ID,self.Answers)

class Awards(models.Model):
  ID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255)

  def __str__(self):
              # this code shows the outpot in the admin panel
        return '{} {}'.format(self.ID,self.Name)

class Subject(models.Model):
  ID = models.AutoField(primary_key=True)
  Subject = models.CharField(max_length=255)
  Subject_score = models.CharField(max_length=255) 

  def __str__(self):
              # this code shows the outpot in the admin panel
        return '{} {} {}'.format(self.ID,self.Subject,self.Subject_score)


class Summary(models.Model):
  Summary_Id =models.AutoField(primary_key=True)
  School_Id = models.ForeignKey(School, to_field='ID', related_name="school_id" , on_delete=models.CASCADE)
  Sydney_Participant = models.CharField(max_length=255)
  Syndey_Percentile = models.CharField(max_length=255) 
  Assessment_Areas_Id = models.ForeignKey(Assessment_Areas, to_field='ID', related_name="Assessment_Areas_id" , on_delete=models.CASCADE) 
  Award_Id = models.ForeignKey(Awards, to_field='ID', related_name="Awards_id" , on_delete=models.CASCADE) 
  Class_Id = models.ForeignKey(Class, to_field='ID', related_name="Class_id" , on_delete=models.CASCADE) 
  Correct_answer_percentage_per_class = models.CharField(max_length=255) 
  Correct_Answer = models.CharField(max_length=255) 
  Student_Id = models.ForeignKey(Student, to_field='ID', related_name="Student_id" , on_delete=models.CASCADE) 
  Participant = models.CharField(max_length=255) 
  Student_score = models.CharField(max_length=255) 
  Subject_Id = models.ForeignKey(Subject, to_field='ID', related_name="Subject_id" , on_delete=models.CASCADE) 
  Category_Id = models.CharField(max_length=255) 
  Year_level_name = models.CharField(max_length=255) 
  Answer_Id = models.ForeignKey(Answers,to_field='ID', related_name="Answers_id" , on_delete=models.CASCADE) 
  Correct_answer_Id = models.CharField(max_length=255) 
  def __str__(self):
              # this code shows the outpot in the admin panel
        return '{} {} {}'.format(self.Summary_Id,self.School_Id,self.Assessment_Areas_Id)