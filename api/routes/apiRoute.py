from django.urls import path,include
from api.views.poemViews import PoemViews
urlpatterns=[
path('poem/',PoemViews.as_view(),name="poem"),
]