from tkinter import *
from api_front.api import ApiRoute


class Interface(Frame):

    """User Interface Window"""

    def __init__(self, fenetre, question, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.dico = {}
        self.nb_item = 0
        self.criteria_name = question[0]
        self.question = question[1]
        self.criteria = []

        self.message = Label(self, text=self.question)

        self.message.pack()
        self.bouton_oui = Button(self, text="Yes", command=self.oui)
        self.bouton_oui.pack(side="left")

        self.bouton_non = Button(self, text="No", command=self.non)
        self.bouton_non.pack(side="right")

    def oui(self):
        self.dico[self.criteria_name] = True
        self.quit()

    def non(self):
        self.dico[self.criteria_name] = False
        self.quit()


def display_ways(json):
    """This is how the information about the different possible ways will be displayed to the user"""
    print("To go from : {} \n        to : {}".format(json["start_address"], json["end_address"]))
    print('=' * 20)
    array = json["routes"]
    for way in array.items():
        print(way[0] + " - {}mins, {}m, {} €".format(str(way[1]["Total duration"]), str(way[1]["Total distance"]), str(way[1]["Price"])))
        print('-'*8)
        for elemWay in way[1]["Route details"].items():
            print('{} : {}m, {}mins'.format(elemWay[0], elemWay[1]["ElemWay Distance"], elemWay[1]["ElemWay Duration"]))
            for elem_step in elemWay[1]["ElemWay Steps"]:
                  print(' ' * 8 + elem_step['instruction'])
        print('=' * 20)


def main():

    dico = {'destination': 'Paris', 'charged': False, 'walk': True, 'bike': True, 'rich': False, 'car': True,
            'driving licence': True, 'navigo': False, 'credit card': True, 'criteria': 1}

    way_manager = ApiRoute(dico).data_structure()
    print("json : {}".format(way_manager))
    display_ways(way_manager)


"""
    L = [('charged', 'Are you charged ?'), ('walk', 'Do you want to walk ?'),
         ('bike', 'Do you want to use a bike ?'), ('rich', 'Is the price important for you ?'),
         ('driving licence', 'Do you have a driving licence ?'), ('navigo', 'Do you have a Navigo pass ?'),
         ('credit card', 'Do you have a credit card ?'), ('car', 'Do you have a car ?')]

    dico = {}
    dico['destination'] = input("Where do you want to go ? : ")

    for question in L:
        fenetre = Tk()
        interface = Interface(fenetre, question)

        interface.mainloop()
        interface.destroy()
        for cle, valeur in interface.dico.items():
            dico[cle] = valeur

    print(dico)
"""



"""
    display_ways({'Velib':[['w1',(1, 15,0,[{'distance': '25 m', 'duration':'1min','instruction':'Turn left'},{'distance': '45 m', 'duration':'1min','instruction':'Turn Right'}, {'distance': '225 m', 'duration':'2min','instruction':'Come on !'}])], ['c',(6, 24, 6.4,[{'distance': '25 m', 'duration':'1min','instruction':'This'}, {'distance': '25 m', 'duration':'1min','instruction':'is'}, {'distance': '25 m', 'duration':'1min','instruction':'awesome'}])], ['w2', (0.1, 1, 0, [{'distance': '25 m', 'duration':'1min','instruction':'Like Usain Bolt'}])]],
                 'Autolib':[['w1', (2.3, 12, 0, [{'distance': '25 m', 'duration':'1min','instruction':'Take a car'}, {'distance': '25 m', 'duration':'1min','instruction':'Drive'}])], ['c', (6, 24, 7.2, [{'distance': '25 m', 'duration':'1min','instruction':'That'}, {'distance': '25 m', 'duration':'1min','instruction':'is'}, {'distance': '25 m', 'duration':'1min','instruction':'easy'}])], ['w2',(0.1, 1, 0, [{'distance': '25 m', 'duration':'1min','instruction':'You'}, {'distance': '25 m', 'duration':'1min','instruction':'are'}, {'distance': '25 m', 'duration':'1min','instruction':'here'}])]],
                 'Subway': [['s', (8, 33, 2.75, [{'distance': '25 m', 'duration':'1min','instruction':'Take the A line'}, {'distance': '25 m', 'duration':'1min','instruction':'Take the 5 line'}])], ['w', (15, 25, 0, [{'distance': '25 m', 'duration':'1min','instruction':'Sors du métro'}])]]})
"""

if __name__ == "__main__":
    main()