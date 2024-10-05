from django.shortcuts import render
from .models import PDFS
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.

def index(request):
    return render(request, "core/index.html")

class PDFListView(ListView):
    model = PDFS
    template_name = 'tu_template.html'
    context_object_name = 'pdfs'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return PDFS.objects.filter(name__icontains=query)
        return PDFS.objects.all()

def download_pdf(request, pdf_id):
    pdf = PDFS.objects.get(id=pdf_id)
    response = HttpResponse(pdf.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf.file.name}"'
    return response