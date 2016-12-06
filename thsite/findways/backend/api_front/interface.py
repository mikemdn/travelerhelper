import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thsite.settings")
application = get_wsgi_application()
from findways.backend.api_front.api import ApiRoute


def display_ways(array):
    """This is how the information about the different possible ways will be displayed to the user"""
    for way in array.items():
        print(way[0] + " - {}mins, {}m, {} €".format(str(way[1][0]), str(way[1][1]), str(way[1][2])))
        print('-'*8)
        for elemWay in way[1][-1]:
            print('{} : {}m, {}mins'.format(elemWay[0], elemWay[1][0], elemWay[1][1]))
            for elem_step in elemWay[1][-1]:
                  print(' ' * 8 + elem_step['instruction'])
        print('=' * 20)


def main():
    dico = {'destination': 'Paris', 'charged': False, 'walk': True, 'bike': True, 'rich': False, 'car': True,
            'driving licence': True, 'navigo': False, 'credit card': True}

    way_manager = ApiRoute(dico).data_structure()
    print(way_manager)
    display_ways(way_manager)

if __name__ == "__main__":
    main()
