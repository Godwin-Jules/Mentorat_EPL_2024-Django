from django.urls import path
from . import views


urlpatterns = [
    path('', views.StartingView.as_view(), name='starting'),
    path('months/', views.MonthsView.as_view(), name='months'),
    path('months/add-goal/', views.AddGoalView.as_view(), name='add_goal'),
    path('months/add-skill/', views.AddSkillView.as_view(), name='add_skill'),
    path('months/add-challenge/', views.ChallengesView.as_view(), name='add_challenge'),
    path('months/<str:month>/', views.MonthChallengesView.as_view(), name='challenges'),
    path('months/<str:month>/<slug:slug>/', views.SingleChallengeView.as_view(), name='challenge'),
    path('goals/', views.GoalsView.as_view(), name="all_goals"),
    path('skills/', views.SkillsView.as_view(), name="all_skills"),
    path('challenges/', views.ChallengesView.as_view(), name='all_challenges'),
]