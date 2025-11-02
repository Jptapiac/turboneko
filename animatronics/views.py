from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Animatronic


def animatronic_list(request):
    queryset = Animatronic.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'animatronics/list.html', {'page_obj': page_obj})


