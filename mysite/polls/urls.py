from django.urls import path

from . import views
from . import apiviews

app_name = 'polls'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
        path('questions/', apiviews.QuestionList.as_view(), name='question_list'),
        path('questions/<int:pk>', apiviews.QuestionDetail.as_view(), name='question_detail'),

]
