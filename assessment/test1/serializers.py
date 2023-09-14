from rest_framework import serializers

from test1.models import Answers, Assessment_Areas, Awards, Class, School, Student, Subject, Summary



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('__all__')

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('__all__')

class Assessment_AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment_Areas
        fields = ('__all__')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('__all__')

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = ('__all__')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('__all__')

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('__all__')
        expandable_fields = {
                             'School': (SchoolSerializer, {'source': 'ID', 'fields': ['ID','Name']}),
                             'Class': (ClassSerializer, {'source': 'ID', 'fields': ['ID','Class']}),
                             'Assessment_Areas': (Assessment_AreasSerializer, {'source': 'ID', 'fields': ['ID','Name']}),
                             'Awards': (AwardsSerializer, {'source': 'ID', 'fields': ['ID','Name']}),
                             'Student': (StudentSerializer, {'source': 'ID', 'fields': ['ID','Fullname']}),
                             'Subject': (SubjectSerializer, {'source': 'ID', 'fields': ['ID','Subject','Subject_score']}),
                             'Answers': (AnswersSerializer, {'source': 'ID', 'fields': ['ID','Answers']}),

                             }