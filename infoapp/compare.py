#etab=[{"choix":[0,2,1],"temp":2,"capacity":1},{"priorite":[0,1,2],"temp":[1,2],"capacity":1},{"priorite":[0,1,2],"temp":[1,2],"capacity":1}]
#etud=[{"choix":[0,1,2],"temp":1},{"choix":[1,2,0],"ac":0},{"choix":[1,2,2],"ac":0}]

import random
#pour generer chaque fois des resultats differentes
random.seed()



#Generation des donnnees : 
#------------------------------

#pour generer les donnees aleatoires des departements
def generate_Department_data(DEP_NUM):

    etab=[]
    ETUD_NUM = DEP_NUM#le nombre d'etudiant = le nombre d'etablissement

    for i in range(DEP_NUM):
        d={}
        k=random.sample(range(0, ETUD_NUM), ETUD_NUM)
        d["choix"]=k
        d["temp"]=-1
        d["capacity"]=1
        d["stable"]=0
        etab.append(d)

    return etab


#pour generer les donnees aleatoires des etudiants
def generate_Student_data(ETUD_NUM):

    etud=[]
    DEP_NUM=ETUD_NUM#le nombre d'etudiant = le nombre d'etablissement

    for i in range(ETUD_NUM):
        d={}
        k=random.sample(range(0,DEP_NUM), DEP_NUM)
        d["choix"]=k
        d["temp"]=-1
        d["stable"]=0
        etud.append(d)
    return etud


#Execution du mariage stable
#----------------------------

#Utiliser dans le mariage stable
def prefere(pri, id):
    lst=pri['choix']
    temp = pri['temp']
    n_i = -1
    for i in range(0,len(lst)):
        if(lst[i] == id): n_i=i

    #-2 -> continue
    #-3 -> arreter
    if n_i==-1: return -2
    if temp==-1: 
        pri['temp']=n_i
        return -4
    if n_i==temp:
        return -4
    if n_i<temp:
        pri['temp']=n_i
        return -3
    else :
        return -2

#mariage stable
def mariage_stable(etab,etud): #cas quand etab recoivent les voeux
    done=False

    # etu['temp'] stocke l'indice dans la liste des choix en cours de consideration
    for etu in etud: 
        etu['temp']=0

    while not(done):
        done=True #
        for i in range(0,len(etud)):
            etu = etud[i]
            if etu['temp']<len(etu['choix']):#if etu['stable']==0:
                etab_recv = etab[etu['choix'][etu['temp']]]
                n_i=prefere(etab_recv, i)
                if n_i==-3 or n_i==-2: #ancien match rejete
                    done=False
                if n_i==-2: #choixcourant rejete
                    etu['temp']+=1



#Methode de satisfaction 1 :
#------------------------------------

# sommer le rang des effectifs choisis pour mesurer
def mesure_dissatifaction_totale(lst):
    aux=0
    for i in lst: aux+=i['temp']
    return aux

# retrouver le max des rang des effectifs choisis pour mesurer
def mesure_dissatifaction_max(lst):
    aux=0
    for i in lst:
        if aux<i['temp']:
            aux=i['temp']
    return aux


#Methode de satisfaction 2 :
#------------------------------------

#calcule le pourcentage de satisfaction pour chaque valeur(Etab ou Etud) de lst
def pourcentage_satisfaction(lst):
    res=[]
    moy=0
    for i in lst:
        res.append(      float(1-float(i['temp']+1)/float(len(i['choix'])))*100         )
        moy+=(1-(i['temp']+1)/len(i['choix']))*100
    return (res,moy/len(lst))

#calcule le pourcentage de desatisfaction pour chaque valeur(Etab ou Etud) de lst
def pourcentage_desatisfaction(lst):
    res=[]
    moy=0
    for i in lst:
        res.append(float(float(i['temp']+1)/float(len(i['choix'])))*100)
        moy+=((i['temp']+1)/len(i['choix']))*100
    return (res,moy/len(lst))




#Test de la satisfaction en pourcentage :
def test_pourcecntage():
    etab=generate_Department_data(30)
    etud=generate_Student_data(30)
    mariage_stable(etab,etud)


    print("Priorite : ETABLISSEMENT ")
    print("-----------------------")

    print("Satisfaction Etab: ")
    l1,r1=pourcentage_satisfaction(etab)
    #print("L1 : ",l1)
    print("Res1_etab : ",r1)
    print("satisfaction Etud: ")
    l2,r2=pourcentage_satisfaction(etud)
    #print("L2 : ",l2)
    print("Res1_etud : ",r2)


    print("Priorite : ETUDIANT ")
    print("-----------------------")

    for x in etab: x['temp']=-1
    for x in etud: x['temp']=-1
    mariage_stable(etud,etab)

    print("Satisfaction Etab: ")
    l1,r1=pourcentage_satisfaction(etab)
    #print("L1 : ",l1)
    print("Res2_etab : ",r1)
    print("satisfaction Etud: ")
    l2,r2=pourcentage_satisfaction(etud)
    #print("L2 : ",l2)
    print("Res2_etud : ",r2)


#Execution N fois de l'algorithm de mariage + comparaison de satisfaction : 
#--------------------------------------------------------------------------------

def executionN(nbre_tours,nbre_etud_etab):
    sat_etab_max=[]
    sat_etab_sum=[]
    sat_etud_sum=[]
    sat_etud_max=[]
    for i in range(0,nbre_tours):
        etab=generate_Department_data(nbre_etud_etab)
        etud=generate_Student_data(nbre_etud_etab)
        l1=[]
        l2=[]
        l3=[]
        l4=[]
        for x in etab: x['temp']=-1
        for x in etud: x['temp']=-1
        mariage_stable(etab,etud)
        l1.append(mesure_dissatifaction_totale(etud))
        l2.append(mesure_dissatifaction_max(etud))
        l3.append(mesure_dissatifaction_totale(etab))
        l4.append(mesure_dissatifaction_max(etab))
        for x in etab: x['temp']=-1
        for x in etud: x['temp']=-1
        mariage_stable(etud,etab)
        l1.append(mesure_dissatifaction_totale(etud))
        l2.append(mesure_dissatifaction_max(etud))
        l3.append(mesure_dissatifaction_totale(etab))
        l4.append(mesure_dissatifaction_max(etab))
        sat_etab_max.append(l1)
        sat_etab_sum.append(l2)
        sat_etud_sum.append(l3)
        sat_etud_max.append(l4)
    print("Satisfaction etab max : ")
    print(sat_etab_max)
    print("satisfaction etab sum : ")
    print(sat_etab_sum)
    
    print("Satisfaction etud max : ")
    print(sat_etud_sum)
    print("Satisfaction etud sum : ")
    print(sat_etud_max)


#Execution N fois de l'algorithm de mariage + comparaison de satisfaction + Ordonnee les resultats obtenue: 
#-----------------------------------------------------------------------------------------------------------------
def affichage(comp_de,r1,r2):
        print("Comparaison "+comp_de+" : ")
        print("res etud  : ",r1,end=" ")
        if(r1<r2):
            print("<",end=" ")
        else :
            print(">",end=" ")
        print(r2)


def executionN_6(nbre_tours,nbre_etud_etab):
    res_comparaison=[]
    for i in range(0,nbre_tours):
        etab=generate_Department_data(nbre_etud_etab)
        etud=generate_Student_data(nbre_etud_etab)

        for x in etab: x['temp']=-1
        for x in etud: x['temp']=-1


        mariage_stable(etab,etud)#on donne priorite a l'etablissement
        _,res1_etab=pourcentage_satisfaction(etab)
        _,res1_etud=pourcentage_satisfaction(etud)


        for x in etab: x['temp']=-1
        for x in etud: x['temp']=-1
        mariage_stable(etud,etab)
        _,res2_etab=pourcentage_satisfaction(etab)
        _,res2_etud=pourcentage_satisfaction(etud)

        res_comparaison.append([res1_etud<res2_etud,res1_etab>res2_etab])

        print("Iteraion "+str(i)+" : ")
        affichage("Etudiant",res1_etud,res2_etud)
        affichage("Etablissement",res1_etab,res2_etab)


    print("Le resultat de comparaison : ")
    print(res_comparaison)


executionN_6(20,30)
#test_pourcecntage()