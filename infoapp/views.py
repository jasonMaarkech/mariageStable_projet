from django.shortcuts import render
from infoapp import code_a_executer




#utiliser pour cree une copie du dictionnaire
def copyDict(l):
    k=[]
    for x in l:
        t={}
        t['id']=x["id"]
        t['choix']=x["choix"]
        t['temp']=x["temp"]
        t['capacity']=x["capacity"]
        t['stable']=x["stable"]
        k.append(t)
    return k;



#je re-initialise la valeur de temps a -1
def reInitialisationTmp(dict):
    for x in dict: x['temp']=-1
        


def index(request):

    #ces variables sont utiliser pour remplire l'informations de satisfactions 
    sat_etud_pEtab=''
    sat_etab_pEtab=''
    sat_etud_pEtud=""
    sat_etab_pEtud=""


    #contient info etab et etud generer aleatoirement
    ietab=""
    ietud=""

    #contient les informations si on fait un marriage stable priorite etudiant et priorite etablissement
    etab=""
    etud=""

    #utiliser si on fait un marriage stable priorite etab et etud et on les compare
    netud=""
    netab=""

    #staisfaction methode2
    sat_etud_pEtab_m2_moy=''
    sat_etab_pEtab_m2_moy=''
    sat_etud_pEtud_m2_moy=""
    sat_etab_pEtud_m2_moy=""
    etud_m2_ar=''
    etab_m2_ar=''
    netud_m2_ar=""
    netab_m2_ar=""





    if request.method=="POST":

        #je cherche les donnees envoyees
        num=request.POST['num']#le num d'etab et d'etud
        mariage=request.POST['mariage']# le type de mariage voulue
   


        #on converte en integer
        num=int(num)
        mariage=int(mariage)


        #on genere les informatons des etudiants et des etablissements
        ietab=code_a_executer.generate_Department_data(num)
        ietud=code_a_executer.generate_Student_data(num)


        #je prend une copie de ces informations
        etab=copyDict(ietab)
        etud=copyDict(ietud)


        if mariage==2:
            netab=copyDict(ietab)
            netud=copyDict(ietud)



        if mariage==0 :
            code_a_executer.marriage_stable(etab,etud)
            sat_etud_pEtab='etud totale :' + str(code_a_executer.mesure_dissatifaction_totale(etud)) + ', etud max : ' + str(code_a_executer.mesure_dissatifaction_max(etud))
            sat_etab_pEtab='etab totale :' + str(code_a_executer.mesure_dissatifaction_totale(etab)) + ', etab max : ' + str(code_a_executer.mesure_dissatifaction_max(etab))

            etud_m2_ar,sat_etud_pEtab_m2_moy=code_a_executer.pourcentage_satisfaction(etud)
            etab_m2_ar,sat_etab_pEtab_m2_moy=code_a_executer.pourcentage_satisfaction(etab)

        if mariage==1 :
            code_a_executer.marriage_stable(etud,etab)
            sat_etud_pEtud='etud totale :' + str(code_a_executer.mesure_dissatifaction_totale(etud)) + ', etud max : ' + str(code_a_executer.mesure_dissatifaction_max(etud))
            sat_etab_pEtud='etab totale :' + str(code_a_executer.mesure_dissatifaction_totale(etab)) + ', etab max : ' + str(code_a_executer.mesure_dissatifaction_max(etab))


            etud_m2_ar,sat_etud_pEtud_m2_moy=code_a_executer.pourcentage_satisfaction(etud)
            etab_m2_ar,sat_etab_pEtud_m2_moy=code_a_executer.pourcentage_satisfaction(etab)


        if mariage==2:
            code_a_executer.marriage_stable(etab,etud)
            sat_etud_pEtab='etud totale :' + str(code_a_executer.mesure_dissatifaction_totale(etud)) + ', etud max : ' + str(code_a_executer.mesure_dissatifaction_max(etud))
            sat_etab_pEtab='etab totale :' + str(code_a_executer.mesure_dissatifaction_totale(etab)) + ', etab max : ' + str(code_a_executer.mesure_dissatifaction_max(etab))
            etud_m2_ar,sat_etud_pEtab_m2_moy=code_a_executer.pourcentage_satisfaction(etud)
            etab_m2_ar,sat_etab_pEtab_m2_moy=code_a_executer.pourcentage_satisfaction(etab)



            reInitialisationTmp(netab)
            reInitialisationTmp(netud)
            code_a_executer.marriage_stable(netud,netab)
            sat_etud_pEtud='etud totale :' + str(code_a_executer.mesure_dissatifaction_totale(netud)) + ', etud max : ' + str(code_a_executer.mesure_dissatifaction_max(netud))
            sat_etab_pEtud='etab totale :' + str(code_a_executer.mesure_dissatifaction_totale(netab)) + ', etab max : ' + str(code_a_executer.mesure_dissatifaction_max(netab))
            netud_m2_ar,sat_etud_pEtud_m2_moy=code_a_executer.pourcentage_satisfaction(netud)
            netab_m2_ar,sat_etab_pEtud_m2_moy=code_a_executer.pourcentage_satisfaction(netab)


            netab=code_a_executer.addResult_toDict(netab,netab_m2_ar)
            netud=code_a_executer.addResult_toDict(netud,netud_m2_ar)


        etab=code_a_executer.addResult_toDict(etab,etab_m2_ar)
        etud=code_a_executer.addResult_toDict(etud,etud_m2_ar)



        return render(request, 'hello_world.html', {'sat_etab_pEtab_m2_moy':sat_etab_pEtab_m2_moy,'sat_etud_pEtab_m2_moy':sat_etud_pEtab_m2_moy,'sat_etab_pEtud_m2_moy':sat_etab_pEtud_m2_moy,'sat_etud_pEtud_m2_moy':sat_etud_pEtud_m2_moy,'ietab':ietab,'ietud':ietud,'etab':etab,'etud':etud,'netab':netab ,'netud':netud ,'sat_etud_pEtab':sat_etud_pEtab,'sat_etab_pEtab':sat_etab_pEtab,'sat_etud_pEtud':sat_etud_pEtud,'sat_etab_pEtud':sat_etab_pEtud})

    return render(request, 'hello_world.html', {})

def GenEtab(request):
    ietab=code_a_executer.generate_Department_data()
    return render(request, 'hello_world.html', {'ietab':ietab})

def GenEtud(request):
    ietud=code_a_executer.generate_Student_data()
    return render(request, 'hello_world.html', {'ietud':ietud})
