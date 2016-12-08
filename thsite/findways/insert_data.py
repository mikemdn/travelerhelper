import xlrd
from findways.models import Place


def get_all_places():

    classeur = xlrd.open_workbook("thplaces.xlsx")
    nom_des_feuilles = classeur.sheet_names()
    feuille = classeur.sheet_by_name(nom_des_feuilles[0])

    for x in range(0, 67):
        place = Place(name="{}".format(feuille.cell_value(x, 0)), lat="{}".format(feuille.cell_value(x, 1)),
                  long="{}".format(feuille.cell_value(x, 2)))

        place.save()


def retrieve_places():
    return Place.objects.all()

get_all_places()
print(retrieve_places())