from . import models

with open('../tests.txt', 'w') as file:
    mineral = models.Mineral.objects.get(pk=1)
    file.write(mineral)
2