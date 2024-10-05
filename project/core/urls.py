from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
     path("lista/", views.PDFListView.as_view(), name="list"),
    path('download/<int:pdf_id>/', views.download_pdf, name='download_pdf'),
]