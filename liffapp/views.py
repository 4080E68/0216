from django.shortcuts import render
from liffapp.models import cpu
# Create your views here.


def liff(request):
    cpus = cpu.objects.get(id=7)

    return render(request, 'index_form.html', locals())
