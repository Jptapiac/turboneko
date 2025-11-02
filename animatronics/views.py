from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Animatronic

# Vista con filtros y paginación
def animatronic_list(request):
    # Obtener todos los registros
    queryset = Animatronic.objects.all()

    # Capturar los filtros por GET
    category = request.GET.get('category')
    manufacturer = request.GET.get('manufacturer')

    # Aplicar filtros si existen
    if category:
        queryset = queryset.filter(category__name__icontains=category)
    if manufacturer:
        queryset = queryset.filter(manufacturer__name__icontains=manufacturer)

    # Paginación (9 elementos por página)
    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pasar al template
    return render(request, 'animatronics/list.html', {'page_obj': page_obj})
