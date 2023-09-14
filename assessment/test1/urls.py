


from django.urls import path

from test1.views import AnswersDetail, AnswersList, Assessment_AreasDetail, Assessment_AreasList, AwardsDetail, AwardsList, ClassDetail, ClassList, SchoolDetail, SchoolList, StudentDetail, StudentList, SubjectDetail, SubjectList, SummaryDetail, SummaryList


urlpatterns = [
    path('School/', SchoolDetail.as_view()),
    path('School/<int:pk>/', SchoolList.as_view()),

    path('Class/', ClassDetail.as_view()),
    path('Class/<int:pk>/', ClassList.as_view()),
    
    path('Assessment_Areas/', Assessment_AreasDetail.as_view()),
    path('Assessment_Areas/<int:pk>/', Assessment_AreasList.as_view()),
    
    path('Student/', StudentDetail.as_view()),
    path('Student/<int:pk>/', StudentList.as_view()),
    
    path('Answers/', AnswersDetail.as_view()),
    path('Answers/<int:pk>/', AnswersList.as_view()),
    
    path('Awards/', AwardsDetail.as_view()),
    path('Awards/<int:pk>/', AwardsList.as_view()),

    path('Subject/', SubjectDetail.as_view()),
    path('Subject/<int:pk>/', SubjectList.as_view()),

    path('Summary/', SummaryDetail.as_view()),
    path('Summary/<int:pk>/', SummaryList.as_view()),
]