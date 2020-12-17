from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Class, Category

# Create your views here.


def all_classes(request):
    """ A view to show all classes, including sorting and search queries """

    classes = Class.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                classes = classes.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            classes = classes.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            classes = classes.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('classes'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            classes = classes.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'classes': classes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'classes/classes.html', context)


def class_detail(request, class_id):
    """ A view to show individual class details """

    a_class = get_object_or_404(Class, pk=class_id)

    context = {
        'class': a_class,
    }

    return render(request, 'classes/class_detail.html', context)
