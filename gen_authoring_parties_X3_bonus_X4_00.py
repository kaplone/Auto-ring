import sys, os, os.path
import shutil
import subprocess
import time

def dvdaut(repertoire_de_travail, nom_export, lettre_1, lettre_2, lettre_3, lettre_4, liste_fake) :

    dic_datas_pages = {}

    xml_inter_file = "/pages/" + nom_export + "_inter.xml"
    xml_inter_open = open(repertoire_de_travail + xml_inter_file, "w")

    fichier_inter_debut = """<dvdauthor dest="%s/export_dvd_mplex">
    <vmgm>
        <fpc> jump titleset 1 menu entry root; </fpc>
    </vmgm>
    <titleset>
        <menus>
            <video format="pal" aspect="16:9" resolution="720x576" widescreen="nopanscan"> </video>
            <audio format="ac3" lang="FR"></audio>
            <subpicture>
                <stream mode="widescreen" id="0" />
                <stream mode="letterbox" id="1" />
            </subpicture>
            <pgc entry="root">
                <vob file="%s/pages/solo_index.mpg" pause="inf"></vob>
<!--
				page1
				solo_index_data.txt
-->
                <button name="1"> jump title 1 ; </button>\n""" % (repertoire_de_travail, repertoire_de_travail)
    xml_inter_open.write(fichier_inter_debut)


    liste_des_datas = []
    liste_des_datas_temp = sorted(os.listdir(repertoire_de_travail + "/pages"))
    for d in liste_des_datas_temp :
        if "solo_page" in d :
            if ".txt" in d :
                liste_des_datas.append(d)
            else :
                pass
        else :
            pass
    print liste_des_datas

    solo_last = open(repertoire_de_travail + "/pages/" + liste_des_datas[-1], "r")
    lecture_solo_last = solo_last.readlines()
    for l in lecture_solo_last :
        if "positition de la page dans le xml" in l :
            derniere_page_avant_les_bonus = l.split("=")[-1].strip()

    solo_debut_partie_2 = open(repertoire_de_travail + "/pages/solo_page_2_1_data.txt", "r")
    lecture_solo_debut_partie_2 = solo_debut_partie_2.readlines()
    for l in lecture_solo_debut_partie_2 :
        if "positition de la page dans le xml" in l :
            premiere_page_partie_2 = l.split("=")[-1].strip()

    solo_index_data = open(repertoire_de_travail + "/pages/solo_index_data.txt", "r")
    lecture_solo_index_data = solo_index_data.readlines()
    for l in lecture_solo_index_data :
        if "nombre de bonus" in l :
            nombre_de_bonus = l.split("=")[-1].strip()
            if nombre_de_bonus != "0" :
                lien_bonus = """                <button name="2">jump menu %d; </button>\n""" % (int(derniere_page_avant_les_bonus) + 1)
                xml_inter_open.write(lien_bonus)
                for l in lecture_solo_index_data :
                    if "nombre de liens sur la page index" in l :
                        nombre_de_liens_sur_la_page_index = l.split("=")[-1].strip()
                    elif "nombre de parties" in l :
                        nombre_de_parties = l.split("=")[-1].strip()
                for n in range(3, int(nombre_de_liens_sur_la_page_index) +1) :
                    if n == 3 :
                        lien_page_n = """                <button name="3">jump menu 2; </button>\n"""
                    else :
                        lien_page_n = """                <button name="%d">jump menu %d; </button>\n""" % (n, int(premiere_page_partie_2))
                    xml_inter_open.write(lien_page_n)
            else :
                for l in lecture_solo_index_data :
                    if "nombre de liens sur la page index" in l :
                        nombre_de_liens_sur_la_page_index = l.split("=")[-1].strip()
                    elif "nombre de parties" in l :
                        nombre_de_parties = l.split("=")[-1].strip()
                for n in range(2, int(nombre_de_liens_sur_la_page_index) +1) :
                    if n == 2 :
                        lien_page_n = """                <button name="2">jump menu 2; </button>\n"""
                    else :
                        lien_page_n = """                <button name="%d">jump menu %d; </button>\n""" % (n, int(premiere_page_partie_2))
                    xml_inter_open.write(lien_page_n)
        else :
            pass

    ###### TC CHAPITRES ########

    tc_chapitres = open(repertoire_de_travail + "/chapitres.txt", "r")
    lecture_tc_chapitres = tc_chapitres.readlines()
    tc = ""
    nouveau_compteur = 0
    for x in lecture_tc_chapitres :
        if x[0] in ["/", "[", "F"]:
            pass
        else :
            if nouveau_compteur == 0 :
                y = "00:00"
            else :
                if x.split(":")[0] != "00" :
                    y = ",%s:%s:%s.%02d" % (x.split(":")[0],x.split(":")[1],x.split(":")[2], int(x.split(":")[3]) * 4)
                else :
                    y = ",%s:%s.%02d" % (x.split(":")[1],x.split(":")[2], int(x.split(":")[3]) * 4)
            tc = tc + y
            nouveau_compteur = nouveau_compteur +1



    fichier_inter_01 = """            </pgc>
            <pgc>
                <vob file="%s/pages/solo_page_1_1.mpg" pause ="inf"></vob>\n"""  % repertoire_de_travail
    xml_inter_open.write(fichier_inter_01)
    
    flag_up_fake = 0

    for x in range(0, int(derniere_page_avant_les_bonus)) :

        try :
            repere = """<!--
                        page%d
                        %s
        -->\n""" % (x + 2, liste_des_datas[x])
            xml_inter_open.write(repere)
        

            dic_datas_pages["page_%d" % (x + 1)] = open(repertoire_de_travail + "/pages/" + liste_des_datas[x])
            lecture_dic_datas_pages = dic_datas_pages["page_%d" % (x + 1)].readlines()
            for l in lecture_dic_datas_pages :
                
                if "numero premiere vignette" in l :
                    dic_datas_pages["page_%d_premiere_vignette" % (x + 1)] = l.split("=")[-1].strip()
                elif "nombre de vignettes" in l :
                    dic_datas_pages["page_%d_nombre_vignettes" % (x + 1)] = l.split("=")[-1].strip()
                elif "cible lien gauche" in l :
                    dic_datas_pages["page_%d_lien_gauche" % (x + 1)] = l.split("=")[-1].strip()
                elif "nombre d'autres pages" in l :
                    dic_datas_pages["page_%d_autres_pages" % (x + 1)] = l.split("=")[-1].strip()
                elif "numero page en cours" in l :
                    dic_datas_pages["page_%d_page_en_cours" % (x + 1)] = l.split("=")[-1].strip()
                elif "cible lien droite" in l :
                    dic_datas_pages["page_%d_lien_droite" % (x + 1)] = l.split("=")[-1].strip()
                elif "positition de la page dans le xml" in l :
                    dic_datas_pages["page_%d_pos_xml" % (x + 1)] = l.split("=")[-1].strip()

            marque = 0
            for h in range(int(dic_datas_pages["page_%d_premiere_vignette" % (x + 1)]), int(dic_datas_pages["page_%d_premiere_vignette" % (x + 1)]) + int(dic_datas_pages["page_%d_nombre_vignettes" % (x + 1)])) :
                
                if h + flag_up_fake in liste_fake :
                    flag_up_fake = flag_up_fake +1
                
                marque = marque +1
                lien_vignette = """                <button name="%d">jump title 2 chapter %d; </button>\n""" % (marque, h + flag_up_fake)
                xml_inter_open.write(lien_vignette)
            if dic_datas_pages["page_%d_lien_gauche" % (x + 1)] == "0" :
                lien_gauche = """                <button name="%d">jump menu 1; </button>\n""" % (marque + 1)
            else :
                lien_gauche = """                <button name="%d">jump menu %s; </button>\n""" % (marque + 1, dic_datas_pages["page_%d_lien_gauche" % (x + 1)])
            xml_inter_open.write(lien_gauche)
            marque = marque + 1
            for k in range(1, int(dic_datas_pages["page_%d_autres_pages" % (x + 1)]) + 2) :
                if k != int(dic_datas_pages["page_%d_page_en_cours" % (x + 1)]) :
                    marque = marque + 1
                    if int(dic_datas_pages["page_%d_page_en_cours" % (x + 1)]) != int(dic_datas_pages["page_%d_pos_xml" % (x + 1)]) -1 :
                        cible_page = int(premiere_page_partie_2) + k - 1
                    else :
                        cible_page = k + 1
                    lien_page = """                <button name="%d">jump menu %d; </button>\n""" % (marque, cible_page)
                    xml_inter_open.write(lien_page)
                else :
                    pass
            print x, int(dic_datas_pages["page_%d_lien_droite" % (x + 1)]), int(derniere_page_avant_les_bonus)
            if int(dic_datas_pages["page_%d_lien_droite" % (x + 1)]) > int(derniere_page_avant_les_bonus) :
                lien_droite = """                <button name="%d">jump menu 1;  </button>\n""" % (marque + 1)
            else :
                lien_droite = """                <button name="%d">jump menu %s; </button>\n""" % (marque + 1, dic_datas_pages["page_%d_lien_droite" % (x + 1)])
            xml_inter_open.write(lien_droite)
        except : pass
        
######### elements de transition entre les contenus ###############        
        
        if x != (int(derniere_page_avant_les_bonus) -2) :
            try :
                fin_titleset = """            </pgc>

            <pgc>
                <vob file="%s/pages/%s.mpg" pause ="inf"></vob>\n""" % (repertoire_de_travail, liste_des_datas[x + 1][:-9])
            except :
                print "----fin de la boucle des parties ----"
                
        elif x == (int(derniere_page_avant_les_bonus) -2) :
            break
        xml_inter_open.write(fin_titleset)
    
######### page des bonus ########

	#solo_bonus_data = open(repertoire_de_travail + "/pages/solo_bonus_data.txt", "r")
    #lecture_solo_bonus_data = solo_bonus_data.readlines()
    #for l in lecture_solo_bonus_data :
		

	fichier_inter_bonus = """            </pgc>
            <pgc>
                <vob file="%s/pages/solo_bonus.mpg" pause ="inf"></vob>\n"""  % repertoire_de_travail
    xml_inter_open.write(fichier_inter_bonus)
    
    repere = """<!--
                        page des bonus
                        %d
        -->\n""" % (int(derniere_page_avant_les_bonus) + 1)
    xml_inter_open.write(repere)
    lien_vignette = """                <button name="1">jump title 3; </button>
                <button name="2">jump title 4; </button>
                <button name="3">jump title 5; </button> 
                <button name="4">jump title 6; </button>   
                <button name="5">jump menu entry root; </button>\n"""
    xml_inter_open.write(lien_vignette)
    
    

        
    final_titleset = """            </pgc>
        </menus>
        <titles>
            <video format="pal" aspect="16:9" resolution="720x576" widescreen="nopanscan"> </video>
            <audio format="ac3" lang="FR"></audio>
            <pgc>
                <vob file="%s/generique_%s_mplex.mpg"></vob>
                <post> jump title 2; </post>
            </pgc>
            <pgc>
                <vob file="%s/%s_mplex.mpg" chapters="%s"></vob>
                <post>call menu entry root;</post>
            </pgc>
            <pgc>
                <vob file="%s/%s_bonus_%s_mplex.mpg"></vob>
                <post>call menu entry root;</post>
            </pgc> 
            <pgc>
                <vob file="%s/%s_bonus_%s_mplex.mpg"></vob>
                <post>call menu entry root;</post>
            </pgc> 
            <pgc>
                <vob file="%s/%s_bonus_%s_mplex.mpg"></vob>
                <post>call menu entry root;</post>
            </pgc>  
            <pgc>
                <vob file="%s/%s_bonus_%s_mplex.mpg"></vob>
                <post>call menu entry root;</post>
            </pgc> 
        </titles>
    </titleset>
</dvdauthor>""" % (repertoire_de_travail, nom_export, repertoire_de_travail, nom_export, tc,repertoire_de_travail, nom_export, lettre_1,repertoire_de_travail, nom_export, lettre_2 ,repertoire_de_travail, nom_export, lettre_3, repertoire_de_travail, nom_export, lettre_4)
    
    xml_inter_open.write(final_titleset)
    xml_inter_open.close()

