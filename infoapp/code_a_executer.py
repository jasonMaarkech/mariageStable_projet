#etab=[{"choix":[0,2,1],"temp":2,"capacity":1},{"priorite":[0,1,2],"temp":[1,2],"capacity":1},{"priorite":[0,1,2],"temp":[1,2],"capacity":1}]
#etud=[{"choix":[0,1,2],"temp":1},{"choix":[1,2,0],"ac":0},{"choix":[1,2,2],"ac":0}]


import random
#pour generer chaque fois des resultats differentes
random.seed()




#Generation des donnnees : 
#------------------------------

#c'est la generation des informations des departements
def generate_Department_data(DEP_NUM=10):

    etab=[]
    ETUD_NUM=DEP_NUM#le nombre d'etudiant = le nombre d'etablissement

    id_dep=0#utiliser pour donner un identification pour chaque departement
    for i in range(DEP_NUM):
        d={}
        k=random.sample(range(0, ETUD_NUM), ETUD_NUM)
        d["id"]=id_dep
        d["choix"]=k
        d["temp"]=-1
        d["capacity"]=1
        d["stable"]=0
        id_dep+=1
        etab.append(d)
    return etab


#c'est la generation des informations des etudiants
def generate_Student_data(ETUD_NUM=10):

    etud=[]
    DEP_NUM=ETUD_NUM#le nombre d'etudiant = le nombre d'etablissement

    id_etud=0#utiliser pour donner un identification pour chaque etudiant
    for i in range(ETUD_NUM):
        d={}
        k=random.sample(range(0,DEP_NUM), DEP_NUM)
        d["id"]=id_etud
        d["choix"]=k
        d["temp"]=-1
        d["capacity"]=1
        d["stable"]=0
        id_etud+=1
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
def marriage_stable(etab,etud): #cas quand etab recoivent les voeux
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
    for i in lst:
       aux+=i['temp']
    return aux

# retrouver le max des rang des effectifs choisis pour mesurer
def mesure_dissatifaction_max(lst):
    aux=0
    for i in lst:
        if aux<i['temp']:
            aux=i['temp']
    return aux





#ajout du resultat sur le dictionnaire des donnees
def addResult_toDict(dic,sat):
    for x,y in zip(dic,sat):
        x['res']=x['choix'][x['temp']]
        x['sat']=y
    return dic

#-------------------------------------------------------------------------------------------------
#new a ajouter :


#calcule le pourcentage de satisfaction pour chaque valeur(Etab ou Etud) de lst
def pourcentage_satisfaction(lst):
    res=[]
    moy=0
    for i in lst:
        res.append(      float(1-float(i['temp'])/float(len(i['choix'])))*100         )
        moy+=(1-(i['temp'])/len(i['choix']))*100
    return (res,moy/len(lst))

#calcule le pourcentage de desatisfaction pour chaque valeur(Etab ou Etud) de lst
def pourcentage_desatisfaction(lst):
    res=[]
    moy=0
    for i in lst:
        res.append(float(float(i['temp'])/float(len(i['choix'])))*100)
        moy+=((i['temp'])/len(i['choix']))*100
    return (res,moy/len(lst))
