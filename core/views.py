from django.shortcuts import render

def home(request):
    # Página principal (basada en tu index.html/carousel)
    return render(request, 'core/home.html')

def libros(request):
    # Galería de libros (basada en tu pagina3.html)
    return render(request, 'core/libros.html')

def blog(request):
    # Blog/películas (basada en tu pagina2.html)
    return render(request, 'core/blog.html')

def tienda(request):
    # Galería de imágenes simple (cumple 4 secciones y “redes sociales” en footer)
    return render(request, 'core/tienda.html')

def faq(request):
    # Preguntas frecuentes.
    return render(request, 'core/faq.html')
