from django.shortcuts import render
from django.template.defaulttags import register
from random import randint

from . import models
# Create your views here.


def minerals_list(request):
    # getting all the objects to display their title in the webpage
    minerals = models.Mineral.objects.all()
    rnd_pk = randint(1, minerals.count())
    return render(request, 'minerals_app/index.html', {'minerals': minerals, 'rnd_pk': rnd_pk})


def minerals_detail(request, pk):
    # initializing main_mineral_dict for other necessary fields like name, image_filename, etc.
    main_mineral_dict = {}
    # initializing mineral_dict for fields and their attributes
    mineral_dict = {}
    # getting the minerals from database
    my_mineral = models.Mineral.objects.get(pk=pk)
    # getting all the fields in model
    fields = models.Mineral._meta.get_fields()
    # filtering the fields that are empty
    for field in fields:
        field = field.name
        # getting each field's value in the database
        field_attr = getattr(my_mineral, field)
        if field_attr:
            field_name = " ".join(field.split("_")).title()
            if field not in ["id", "name", "image_filename", "image_caption"]:
                mineral_dict[field_name] = field_attr
            else:
                main_mineral_dict[field] = field_attr
    name = main_mineral_dict.get('name')
    image_filename = "minerals_app/images/" + name + ".jpg"
    image_caption = main_mineral_dict.get('image_caption')
    minerals = models.Mineral.objects.all()
    rnd_pk = randint(1, minerals.count())
    # sending most useful data to the template called detail.html
    return render(request, 'minerals_app/detail.html', {'rnd_pk': rnd_pk,
                                                        'name': name,
                                                        'image_filename': image_filename,
                                                        'image_caption': image_caption,
                                                        'mineral_dict': mineral_dict})


@register.filter
def get_item(dictionary, key):
    """To use dictionary values in the template"""
    return dictionary.get(key)
