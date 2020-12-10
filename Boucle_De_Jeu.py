import plateau as plt
import pioche as pio
import PlacementDeMot as pdm
"""
def tour_joueur(lplateau , sac , main):
    #list_plateau=plt.init_jetons()
    #lplateau=plt.affiche_plateau(list_plateau)
    #sac=pio.init_pioche(pio.init_dico())
    main=pio.piocher(7,sac)
    print(main)
    Q1.lower()=input("passer,echange,placer ? ")
    if Q1.lower()=="echange":
        jetons_list=[]
        nb_jeton=int(input("combien des jetons vous voulez echange"))
        for i in range(nb_jeton):
            jetons=input("choisir un jeton")
            jetons_list.append(jetons)
        echange=pio.echanger(jetons_list,main,sac)
        print(main)
    elif Q1.lower()=="placer":
        mot=input("entrez un mot : ")
        ligne=int(input("ligne de depart ? "))
        colone=int(input("colone de depart ? "))
        dir=input("v ou h ? ")
        placer=pdm.placer_mot(lplateau,main,mot,ligne,colone,dir)
        print(placer)
    elif Q1.lower()=="passer":
        pass
#print(tour_joueur())
"""
def tour_joueur(lplateau , sac , main, nom):
    #list_plateau=plt.init_jetons()
    #lplateau=plt.affiche_plateau(list_plateau)
    #sac=pio.init_pioche(pio.init_dico())
    #main=pio.piocher(7,sac)
    affiche_plateau(lplateau)
    print("Les lettres dans votre main sont : ",main)
    Q1=input("passer (s), echanger (e), placer (p) ? ")
    if Q1.lower() == ("echange" or "e"):
        while True:
            jetons_list=[]
            jetons = input("Ecrivez les jetons que vous souhaitez les echanger\nseparez les par des virgules : ")
            jetons = jetons.upper()
            jetonsf = jetons.replace(' ','')
            jetons_list = jetonsf.split(",")
            #echange = pio.echanger(jetons_list,main,sac)
            echange = pio.echanger(jetons_list,main,sac)
            if echange : break
        print(main)
        #la partie echange est bien vérifier
    elif Q1.lower()== ("placer" or "p"):
        while True:
            coords = pdm.lire_coords()
            ligne = coords[0]
            colone = coords[1]
            mot = input("Quelle mot voulez vous placer : ")
            dir = input("direction vertical (v) ou horizontal (h) ? : ")
            if dir == 'vertical' : dir = 'v'
            if dir == 'horizontal': dir = 'h'
            placer = pdm.placer_mot(lplateau,main,mot,colone,ligne,dir)
            if placer : break
            print(placer)
        #partie placer verifier
    elif Q1.lower()== ("passer" or "s"):
        pass

#fonction qui détecte la fin de la partie
def fin_partie(sac,lm):
    '''
    Fonction renvoie True tant que le sac est suffisant
    est False le sac est insuffisant
    '''
    if len(lm) == 7 :
        return True
    else:
        besoin = 7 - len(lm)
        if besoin > len(sac):
            return False
        else:
            return True
