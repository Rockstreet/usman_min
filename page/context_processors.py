from .models import Page, Menu, MenuSection,  Setting, Sliders
from django.core.cache import cache
from django.conf import settings

def context(request):
    cached_menus = cache.get(settings.MYMENU_CACHE_KEY)
    cached_carousel = cache.get(settings.CAROUSEL_CACHE_KEY)

    if cached_menus is not None:
        return cached_menus
    menus = Menu.objects.filter()
    context = {'menu': {}}
    for menu in menus:
        context['menu'][menu.slug] = menu
    cache.set(settings.MYMENU_CACHE_KEY, context, settings.CACHE_TIMEOUT)

    if cached_carousel is not None:
            return cached_carousel
    carousels = Sliders.objects.filter()
    context = {'carousel': {}}
    for carousel in carousels:
        context['carousel'][carousel.slug] = carousel
    cache.set(settings.CAROUSEL_CACHE_KEY, context, settings.CACHE_TIMEOUT)



    return context



def sitting(request):

    sitting=Setting.objects.first()


    return {"sitting":sitting}





