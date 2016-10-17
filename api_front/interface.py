from tkinter import *
from business.WayManager import WayManager

class Interface(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

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

    def following_question(self):
        if self.nb_item < len(self.questions) - 1:
            self.nb_item += 1
            self.message["text"] = "{}".format(self.questions[self.input_name])
        else:
            self.quit

    def oui(self):
        """.

        """
        self.dico[self.criteria_name] = True
        self.quit()

    def non(self):
        self.dico[self.criteria_name] = False
        self.quit()

def display_ways(array):
    for way in array.items():
        print(way[0])
        print('-'*8)
        for elemWay in way[1].items():
            print('{} : {}km, {}min'.format(elemWay[0], elemWay[1][0], elemWay[1][1]))
            for instruction in elemWay[1][2]:
                  print(' ' * 4 + instruction)
        print('=' * 20)

def main():
    dico = {'destination' : 'Paris','charged' : True , 'walk' : True,
         'bike' : False, 'rich' : False,
         'driving licence' : True, 'navigo' : False,
         'credit card' : True}
    way_manager = WayManager(dico)

    """
    L = [('charged', 'Are you charged ?'), ('walk', 'Do you want to walk ?'),
         ('bike', 'Do you want to use a bike ?'), ('rich', 'Is the price important for you ?'),
         ('driving licence', 'Do you have a driving licence ?'), ('navigo', 'Do you have a Navigo pass ?'),
         ('credit card', 'Do you have a credit card ?')]

    dico = {}

    for question in L:
        fenetre = Tk()
        interface = Interface(fenetre, question)

        interface.mainloop()
        interface.destroy()
        for cle, valeur in interface.dico.items():
            dico[cle] = valeur

    print(dico)

    display_ways({'Velib':{'w1':(1, 15,['Turn left', 'Turn Right', 'Come on !']), 'c':(6, 24,['This', 'is', 'awesome']), 'w2':(0.1, 1, ['Like Usain Bolt'])},
                 'Autolib':{'w1':(2.3, 12, ['Take a car', 'Drive']), 'c':(6, 24,['That', 'is', 'easy']), 'w2':(0.1, 1, ['You', 'are', 'here'])},
                 'Subway':{'s':(8, 33,['Take the A line', 'Take the 5 line'])}})
        """

if __name__ == "__main__":
    main()