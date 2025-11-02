from animatronics.models import Category, Manufacturer

def global_context(request):
    """
    Custom context processor to add global variables to all templates
    """
    return {
        'categories': Category.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
        'latest_animatronics': request.user.reviews.all()[:3] if request.user.is_authenticated else None,
    }