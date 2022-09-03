from django.urls import path
from . import views
urlpatterns = [
	path('challange_award/',views.ChallengeAward.as_view(),name='challenge_award'),
	path('amg_awards/',views.AmgAward.as_view(),name='amg_award'),
	path('award/',views.Award.as_view(),name='award'),
	path('applicationform/',views.ApplicationForm.as_view(),name='application'),
	path('',views.HomePage.as_view(),name='home'),
	path('ourpartner/',views.Partner.as_view(),name='partner'),
	path('agenda/',views.Agenda.as_view(),name='agenda'),
	path('context/',views.Context.as_view(),name='context'),
]
