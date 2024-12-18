from django.urls import path
from legal.views import DocumentAnalysisView

urlpatterns = [
    path('api/analyze/', DocumentAnalysisView.as_view(), name='document_analysis'),
]
