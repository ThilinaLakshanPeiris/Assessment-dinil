from django.shortcuts import render
from rest_framework import generics

from test1.models import Answers, Assessment_Areas, Class, School, Student,Awards, Subject, Summary
from test1.serializers import AnswersSerializer, Assessment_AreasSerializer, AwardsSerializer, ClassSerializer, SchoolSerializer, StudentSerializer, SubjectSerializer, SummarySerializer

# Create your views here.
class SchoolDetail(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    # pagination_class = LimitOffsetPagination
class SchoolList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    # pagination_class = LimitOffsetPagination

class ClassDetail(generics.ListCreateAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    # pagination_class = LimitOffsetPagination
class ClassList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    # pagination_class = LimitOffsetPagination

class Assessment_AreasDetail(generics.ListCreateAPIView):
    serializer_class = Assessment_AreasSerializer
    queryset = Assessment_Areas.objects.all()
    # pagination_class = LimitOffsetPagination
class Assessment_AreasList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Assessment_AreasSerializer
    queryset = Assessment_Areas.objects.all()
    # pagination_class = LimitOffsetPagination

class StudentDetail(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # pagination_class = LimitOffsetPagination
class StudentList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # pagination_class = LimitOffsetPagination

class AnswersDetail(generics.ListCreateAPIView):
    serializer_class = AnswersSerializer
    queryset = Answers.objects.all()
    # pagination_class = LimitOffsetPagination
class AnswersList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswersSerializer
    queryset = Answers.objects.all()
    # pagination_class = LimitOffsetPagination

class AwardsDetail(generics.ListCreateAPIView):
    serializer_class = AwardsSerializer
    queryset = Awards.objects.all()
    # pagination_class = LimitOffsetPagination
class AwardsList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardsSerializer
    queryset = Awards.objects.all()
    # pagination_class = LimitOffsetPagination

class SubjectDetail(generics.ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    # pagination_class = LimitOffsetPagination
class SubjectList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    # pagination_class = LimitOffsetPagination

class SummaryDetail(generics.ListCreateAPIView):
    serializer_class = SummarySerializer
    queryset = Summary.objects.all()
    # pagination_class = LimitOffsetPagination
class SummaryList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SummarySerializer
    queryset = Summary.objects.all()
    # pagination_class = LimitOffsetPagination