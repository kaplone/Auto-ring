#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import sys
import os, os.path
import shutil
import subprocess
import time

sys.path.append("/home/autor/Desktop/auto-ring")
import decoupe_titres_001 as decoupe_titres
import centrer_001 as centrer
import pair_000

repertoire_de_travail = "/home/autor/Desktop/temp/vdm_gimp" ###repertoire_de_travail###
nom_export = "" ###nom_export###
nom_export_hi = "" ###nom_export_hi###
nom_export_sel = "" ###nom_export_sel###
partie = 0 ###partie###
bonus = "" ###bonus###
couleur_texte = (1.0,0.0,0.0,1.0) ###couleur_texte###
nom_ecole = "" ###nom_ecole###
long_ecole = 0 ###long_ecole###
presente = "" ###presente###
long_presente = 0 ###long_presente###
sonsa = "" ###sonsa###
long_sonsa = 0 ###long_sonsa###
titre_spectacle = "" ###titre_spectacle###
long_titre = 0 ###long_titre###
titre_label_1 = "" ###titre_label_1###
titre_label_2 = "" ###titre_label_2###
titre_label_3 = "" ###titre_label_3###
titre_label_4 = "" ###titre_label_4###

nom_export_hi_L = nom_export_hi[:-4] + "_letterbox.png"
nom_export_sel_L = nom_export_sel[:-4] + "_letterbox.png"

fichier_spu_debut = "<subpictures>\n\t<stream>\n\t\t<spu\n\t\t\tforce='yes'\n\t\t\tstart='00:00:00.00'\n\t\t\thighlight='"
fichier_spu_fin = "\t\t</spu>\n\t</stream>\n</subpictures>"

dic_parties = {}
marqueur_partie = 1

dic_coords_spu = {}
dic_tailles_parties ={}

dico_model_indexB ={"1bas" : 3, "1droite" : 3, "1haut" : 2 , "1gauche" : 2,
                    "2bas" : 3, "2droite" : 3, "2haut" : 1 , "2gauche" : 1,
                    "3bas" : 4, "3droite" : 4, "3haut" : 1 , "3gauche" : 2,
                    "4bas" : 5, "4droite" : 5, "4haut" : 1 , "4gauche" : 3,
                    "5bas" : 6, "5droite" : 6, "5haut" : 1 , "5gauche" : 4,
                    "6bas" : 7, "6droite" : 7, "6haut" : 1 , "6gauche" : 5,
                    "7bas" : 8, "7droite" : 8, "7haut" : 1 , "7gauche" : 6,
                    "8bas" : 9, "8droite" : 9, "8haut" : 1 , "8gauche" : 7,
                    "9bas" : 10, "9droite" : 10, "9haut" : 1 , "9gauche" : 8,
                    "10bas" : 2, "10droite" : 2, "10haut" : 1 , "10gauche" : 9}
                    
dico_model_indexN ={"1bas" : 2, "1droite" : 2, "1haut" : 2 , "1gauche" : 2,
                    "2bas" : 3, "2droite" : 3, "2haut" : 1 , "2gauche" : 1,
                    "3bas" : 4, "3droite" : 4, "3haut" : 1 , "3gauche" : 2,
                    "4bas" : 5, "4droite" : 5, "4haut" : 1 , "4gauche" : 3,
                    "5bas" : 6, "5droite" : 6, "5haut" : 1 , "5gauche" : 4,
                    "6bas" : 7, "6droite" : 7, "6haut" : 1 , "6gauche" : 5,
                    "7bas" : 8, "7droite" : 8, "7haut" : 1 , "7gauche" : 6,
                    "8bas" : 9, "8droite" : 9, "8haut" : 1 , "8gauche" : 7,
                    "9bas" : 10, "9droite" : 10, "9haut" : 1 , "9gauche" : 8,
                    "10bas" : 2, "10droite" : 2, "10haut" : 1 , "10gauche" : 9}
                    
dico_model_indexB1 ={"1bas" : 3, "1droite" : 3, "1haut" : 2 , "1gauche" : 2,
                    "2bas" : 3, "2droite" : 3, "2haut" : 1 , "2gauche" : 1,
                    "3bas" : 4, "3droite" : 4, "3haut" : 1 , "3gauche" : 2,
                    "4bas" : 5, "4droite" : 5, "4haut" : 1 , "4gauche" : 3,
                    "5bas" : 6, "5droite" : 6, "5haut" : 1 , "5gauche" : 4,
                    "6bas" : 7, "6droite" : 7, "6haut" : 1 , "6gauche" : 5,
                    "7bas" : 8, "7droite" : 8, "7haut" : 1 , "7gauche" : 6,
                    "8bas" : 9, "8droite" : 9, "8haut" : 1 , "8gauche" : 7,
                    "9bas" : 10, "9droite" : 10, "9haut" : 1 , "9gauche" : 8,
                    "10bas" : 2, "10droite" : 2, "10haut" : 1 , "10gauche" : 9}
                    
dico_model_indexN1 ={"1bas" : 2, "1droite" : 2, "1haut" : 2 , "1gauche" : 2,
                    "2bas" : 3, "2droite" : 3, "2haut" : 1 , "2gauche" : 1,
                    "3bas" : 4, "3droite" : 4, "3haut" : 1 , "3gauche" : 2,
                    "4bas" : 5, "4droite" : 5, "4haut" : 1 , "4gauche" : 3,
                    "5bas" : 6, "5droite" : 6, "5haut" : 1 , "5gauche" : 4,
                    "6bas" : 7, "6droite" : 7, "6haut" : 1 , "6gauche" : 5,
                    "7bas" : 8, "7droite" : 8, "7haut" : 1 , "7gauche" : 6,
                    "8bas" : 9, "8droite" : 9, "8haut" : 1 , "8gauche" : 7,
                    "9bas" : 10, "9droite" : 10, "9haut" : 1 , "9gauche" : 8,
                    "10bas" : 2, "10droite" : 2, "10haut" : 1 , "10gauche" : 9}

vignettes_index = sorted(os.listdir(repertoire_de_travail+ "/images"))[0]

#taille_vignettes = (500, 281)
#taille_frame = (505, 286)
#taille_frame_43 = (353, 286)

taille_vignettes = (500, 281)
taille_frame = (505, 286)
taille_frame_43 = (353, 286)

#coordonnees_h = 180
#coordonnees_v = 260
#coordonnees_v43 = 182

coordonnees_h = 180
coordonnees_v = 260
coordonnees_v43 = 182

liste_des_titres_des_parties =[titre_label_1, titre_label_2, titre_label_3, titre_label_4]

alpha = pdb.gimp_image_new(1024, 576, RGB)

fond = pdb.file_jpeg_load("/home/autor/Desktop/auto-ring/biblio/2013/authoring2013.jpg", "")

foreground = (0.0,0.0,0.0,1.0)
pdb.gimp_context_set_foreground(foreground)

grosse_vignette = pdb.gimp_file_load_layer(fond, repertoire_de_travail + "/images/" + vignettes_index)
        
pdb.gimp_image_add_layer(
    fond,
    grosse_vignette,
    0
    )
pdb.gimp_layer_scale(
    grosse_vignette,
    taille_vignettes[0], taille_vignettes[1],
    0
    )
pdb.gimp_layer_set_offsets(
    grosse_vignette,
    coordonnees_v,
    coordonnees_h
    )
    
foreground = (0.4,0.1,0.1,1.0)
pdb.gimp_context_set_foreground(foreground)



marqueur_page = 1
allignement_parties = 0

width_image = pdb.gimp_image_width(fond)

#### navigation pages basses #####

offset_gap = 96

#### sans bonus #####

if bonus == "0" :
    texte_bonus = ""
    dic_coords_spu["coords_layer_bonus"] = (0,0)
    
    ###### une seule partie #######
    
    if partie == 1:
        time.sleep(1)
        dic_pages = {}
        dic_page_position = {}
        marqueur_page = 1
        while os.path.isfile(repertoire_de_travail + "/pages/solo_page_1_1_data.txt") != True :
            print 'waiting ...'
            time.sleep(0.5)
        pioche = open(repertoire_de_travail + "/pages/solo_page_1_1_data.txt")
        pioche_datas = pioche.readlines()
        for l in pioche_datas :
            
            if "nombre d'autres pages" in l :
                les_pages_de_l_index = int(l.split("=")[-1].strip()) + 1
                for p in range(1, les_pages_de_l_index +1):
                    dic_pages["page_" + str(marqueur_page)] = pdb.gimp_text_layer_new(fond, str(marqueur_page), "sans", 20, 0)
                    pdb.gimp_image_add_layer(
                        fond,
                        dic_pages["page_" + str(marqueur_page)],
                        0
                        )
                        
                    dic_page_position["page_" + str(marqueur_page)] = 450 + 20 + marqueur_page * 40  
                    ### 450+20 remplace 412 pour 350 ###    
                    pdb.gimp_layer_set_offsets(
                        dic_pages["page_" + str(marqueur_page)],
                        450 + 20 + marqueur_page * 40 ,
                        532
                        )
                        
                    pdb.gimp_text_layer_set_color(
                    dic_pages["page_" + str(marqueur_page)],
                    (0.95,0.95,0.95,1.0)
                    )    
                    ### blanc (0.95,0.95,0.95,1.0)
                    
                    marqueur_page = marqueur_page +1
                    
                    
                page = pdb.gimp_text_layer_new(fond, "PAGE : ", "sans", 20, 0)
                pdb.gimp_image_add_layer(
                                         fond,
                                         page,
                                         0
                                         )
                pdb.gimp_text_layer_set_color(
                                           page,
                                           (0.95,0.95,0.95,0.95)
                                           )    
                                           ### blanc (0.95,0.95,0.95,1.0)
                pdb.gimp_layer_set_offsets(
                                           page,
                                           420,
                                           532
                                           )
            
                
                
            else : pass
        
        
    ##### plusieurs parties ######
    
    else :
    
        for y in range(1, partie +1) :
            print "***********",  y
            dic_parties["partie_" + str(y)] = pdb.gimp_text_layer_new(fond, liste_des_titres_des_parties[y-1], "sans", 20, 0)
            pdb.gimp_image_add_layer(
                fond,
                dic_parties["partie_" + str(y)],
                0
                )
            pdb.gimp_text_layer_set_color(
            dic_parties["partie_" + str(y)],
            (0.95,0.95,0.95,1.0)
            )    
            ### blanc (0.95,0.95,0.95,1.0)
           
        ##### 2 parties #####   
           
        if partie == 2 :
            
            dic_tailles_parties["partie_2"] = pdb.gimp_drawable_width(dic_parties["partie_2"])
            dic_coords_spu["coords_partie_2"] = 1024 - offset_gap - dic_tailles_parties["partie_2"]
            dic_tailles_parties["partie_1"] = pdb.gimp_drawable_width(dic_parties["partie_1"])
            dic_coords_spu["coords_partie_1"] = offset_gap
            
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_1"],
                    dic_coords_spu["coords_partie_1"],
                    532
                    )
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_2"],
                    dic_coords_spu["coords_partie_2"],
                    532
                    )
                    
            ##### 3 parties #####   
           
        elif partie == 3 :
            
            dic_tailles_parties["partie_1"] = pdb.gimp_drawable_width(dic_parties["partie_1"])
            dic_coords_spu["coords_partie_1"] = offset_gap
            dic_tailles_parties["partie_3"] = pdb.gimp_drawable_width(dic_parties["partie_3"])
            dic_coords_spu["coords_partie_3"] = 1024 - offset_gap - dic_tailles_parties["partie_3"]
            dic_tailles_parties["partie_2"] = pdb.gimp_drawable_width(dic_parties["partie_2"])
            dic_coords_spu["coords_partie_2"] = (((dic_coords_spu["coords_partie_3"] - (offset_gap + dic_tailles_parties["partie_1"])) / 2 ) - dic_tailles_parties["partie_2"] / 2) + (offset_gap + dic_tailles_parties["partie_1"])
            
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_1"],
                    dic_coords_spu["coords_partie_1"],
                    532
                    )
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_2"],
                    dic_coords_spu["coords_partie_2"],
                    532
                    )
            
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_3"],
                    dic_coords_spu["coords_partie_3"],
                    532
                    )

        ##### 4 parties #####

        elif partie == 4 :
            
            dic_tailles_parties["partie_1"] = pdb.gimp_drawable_width(dic_parties["partie_1"])
            dic_tailles_parties["partie_2"] = pdb.gimp_drawable_width(dic_parties["partie_2"])
            dic_tailles_parties["partie_3"] = pdb.gimp_drawable_width(dic_parties["partie_3"])
            dic_tailles_parties["partie_4"] = pdb.gimp_drawable_width(dic_parties["partie_4"])
            
            intervale = (1024 - offset_gap - offset_gap - (dic_tailles_parties["partie_1"] + dic_tailles_parties["partie_2"] + dic_tailles_parties["partie_3"] + dic_tailles_parties["partie_4"])) / 3
            
            dic_coords_spu["coords_partie_1"] = offset_gap
            
            dic_coords_spu["coords_partie_2"] = offset_gap + dic_tailles_parties["partie_1"] + intervale
            
            dic_coords_spu["coords_partie_3"] = offset_gap + dic_tailles_parties["partie_1"] + intervale + dic_tailles_parties["partie_2"] + intervale 
            
            dic_coords_spu["coords_partie_4"] = 1024 - offset_gap - dic_tailles_parties["partie_4"]
            
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_1"],
                    dic_coords_spu["coords_partie_1"],
                    532
                    )
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_2"],
                    dic_coords_spu["coords_partie_2"],
                    532
                    )
            
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_3"],
                    dic_coords_spu["coords_partie_3"],
                    532
                    )
                    
            pdb.gimp_layer_set_offsets(
                    dic_parties["partie_4"],
                    dic_coords_spu["coords_partie_4"],
                    532
                    )

##### avec bonus ######
 
else :
    
    
    foreground = (0.95,0.95,0.95,1.0)
    pdb.gimp_context_set_foreground(foreground)
    texte_bonus = "BONUS"
    layer_bonus =  pdb.gimp_text_layer_new(fond, texte_bonus, "sans", 20, 0)
    dic_coords_spu["coords_layer_bonus"] = (pdb.gimp_drawable_width(layer_bonus), pdb.gimp_drawable_height(layer_bonus))
        
    try :
        pdb.gimp_image_add_layer(
            fond,
            layer_bonus,
            0
            )
    
    
        pdb.gimp_layer_set_offsets(
            layer_bonus,
            offset_gap,
            532
            )
    except : 
        pass
    
    
    ##### 1 partie #####    
    
    if partie == 1 :
        time.sleep(1)
        dic_pages = {}
        dic_page_position = {}
        marqueur_page = 1
        while os.path.isfile(repertoire_de_travail + "/pages/solo_page_1_1_data.txt") != True :
            print 'waiting ...'
            time.sleep(0.5)
        pioche = open(repertoire_de_travail + "/pages/solo_page_1_1_data.txt")
        pioche_datas = pioche.readlines()
        for l in pioche_datas :
            
            if "nombre d'autres pages" in l :
                les_pages_de_l_index = int(l.split("=")[-1].strip()) + 1
                for p in range(1, les_pages_de_l_index +1):
                    dic_pages["page_" + str(marqueur_page)] = pdb.gimp_text_layer_new(fond, str(marqueur_page), "sans", 20, 0)
                    pdb.gimp_image_add_layer(
                        fond,
                        dic_pages["page_" + str(marqueur_page)],
                        0
                        )
                        
                    dic_page_position["page_" + str(marqueur_page)] = 450 + 20 + marqueur_page * 40  
                    ### 450+20 remplace 412 pour 350 ###    
                    pdb.gimp_layer_set_offsets(
                        dic_pages["page_" + str(marqueur_page)],
                        450 + 20 + marqueur_page * 40 ,
                        532
                        )
                        
                    pdb.gimp_text_layer_set_color(
                    dic_pages["page_" + str(marqueur_page)],
                    (0.95,0.95,0.95,1.0)
                    )    
                    ### blanc (0.95,0.95,0.95,1.0)
                    
                    marqueur_page = marqueur_page +1
                    
                    
                page = pdb.gimp_text_layer_new(fond, "PAGE : ", "sans", 20, 0)
                pdb.gimp_image_add_layer(
                                         fond,
                                         page,
                                         0
                                         )
                pdb.gimp_text_layer_set_color(
                                           page,
                                           (0.95,0.95,0.95,0.95)
                                           )    
                                           ### blanc (0.95,0.95,0.95,1.0)
                pdb.gimp_layer_set_offsets(
                                           page,
                                           420,
                                           532
                                           )
            

            else : pass
       
    ##### 2 parties #####   
       
    elif partie == 2 :
        
        for y in range(1, partie +1) :
            dic_parties["partie_" + str(y)] = pdb.gimp_text_layer_new(fond, liste_des_titres_des_parties[y-1], "sans", 20, 0)
            pdb.gimp_image_add_layer(
                fond,
                dic_parties["partie_" + str(y)],
                0
                )
            pdb.gimp_text_layer_set_color(
            dic_parties["partie_" + str(y)],
            (0.95,0.95,0.95,1.0)
            )    
            ### blanc (0.95,0.95,0.95,1.0)
        
                
        dic_tailles_parties["partie_2"] = pdb.gimp_drawable_width(dic_parties["partie_2"])
        dic_coords_spu["coords_partie_2"] = 1024 - offset_gap - dic_tailles_parties["partie_2"]
        dic_tailles_parties["partie_1"] = pdb.gimp_drawable_width(dic_parties["partie_1"])
        dic_coords_spu["coords_partie_1"] = (1024 - offset_gap - dic_tailles_parties["partie_2"] - offset_gap - pdb.gimp_drawable_width(layer_bonus))/2 + offset_gap + pdb.gimp_drawable_width(layer_bonus) - pdb.gimp_drawable_width(dic_parties["partie_1"])/2
        
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_1"],
                dic_coords_spu["coords_partie_1"],
                532
                )
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_2"],
                dic_coords_spu["coords_partie_2"],
                532
                )
                    
    ##### 3 parties #####   
       
    elif partie == 3 :
        
        for y in range(1, partie +1) :
            dic_parties["partie_" + str(y)] = pdb.gimp_text_layer_new(fond, liste_des_titres_des_parties[y-1], "sans", 20, 0)
            pdb.gimp_image_add_layer(
                fond,
                dic_parties["partie_" + str(y)],
                0
                )
            pdb.gimp_text_layer_set_color(
            dic_parties["partie_" + str(y)],
            (0.95,0.95,0.95,1.0)
            )    
            ### blanc (0.95,0.95,0.95,1.0)
        
                
        dic_tailles_parties["partie_3"] = pdb.gimp_drawable_width(dic_parties["partie_3"])
        dic_coords_spu["coords_partie_3"] = 1024 - offset_gap - dic_tailles_parties["partie_3"]
        dic_tailles_parties["partie_2"] = pdb.gimp_drawable_width(dic_parties["partie_2"])
        dic_tailles_parties["partie_1"] = pdb.gimp_drawable_width(dic_parties["partie_1"])
        petit_gap = int((1024 - 96 - 96 - pdb.gimp_drawable_width(layer_bonus) - dic_tailles_parties["partie_1"] - dic_tailles_parties["partie_2"] - dic_tailles_parties["partie_3"])/ 3)
        dic_coords_spu["coords_partie_1"] = 96 + pdb.gimp_drawable_width(layer_bonus) + petit_gap
        dic_coords_spu["coords_partie_2"] = 96 + pdb.gimp_drawable_width(layer_bonus) + petit_gap + dic_tailles_parties["partie_1"] + petit_gap
        
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_1"],
                dic_coords_spu["coords_partie_1"],
                532
                )
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_2"],
                dic_coords_spu["coords_partie_2"],
                532
                )
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_3"],
                dic_coords_spu["coords_partie_3"],
                532
                )
                
    ##### 4 parties #####            
                
    elif partie == 4 :
        
        for y in range(1, partie +1) :
            dic_parties["partie_" + str(y)] = pdb.gimp_text_layer_new(fond, liste_des_titres_des_parties[y-1], "sans", 20, 0)
            pdb.gimp_image_add_layer(
                fond,
                dic_parties["partie_" + str(y)],
                0
                )
            pdb.gimp_text_layer_set_color(
            dic_parties["partie_" + str(y)],
            (0.95,0.95,0.95,1.0)
            )    
            ### blanc (0.95,0.95,0.95,1.0)
        
        dic_tailles_parties["partie_1"] = pdb.gimp_drawable_width(dic_parties["partie_1"]) 
        dic_tailles_parties["partie_2"] = pdb.gimp_drawable_width(dic_parties["partie_2"])     
        dic_tailles_parties["partie_3"] = pdb.gimp_drawable_width(dic_parties["partie_3"])
        dic_tailles_parties["partie_4"] = pdb.gimp_drawable_width(dic_parties["partie_4"])
        
        intervale = (1024 - offset_gap - offset_gap - (pdb.gimp_drawable_width(layer_bonus) + dic_tailles_parties["partie_1"] + dic_tailles_parties["partie_2"] + dic_tailles_parties["partie_3"] + dic_tailles_parties["partie_4"])) / 4
        
        dic_coords_spu["coords_partie_1"] = 96 + pdb.gimp_drawable_width(layer_bonus) + intervale
        dic_coords_spu["coords_partie_2"] = 96 + pdb.gimp_drawable_width(layer_bonus) + intervale + dic_tailles_parties["partie_1"] + intervale
        dic_coords_spu["coords_partie_3"] = 96 + pdb.gimp_drawable_width(layer_bonus) + intervale + dic_tailles_parties["partie_1"] + intervale + dic_tailles_parties["partie_2"] + intervale
        dic_coords_spu["coords_partie_4"] = 1024 - offset_gap - dic_tailles_parties["partie_4"]
        
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_1"],
                dic_coords_spu["coords_partie_1"],
                532
                )
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_2"],
                dic_coords_spu["coords_partie_2"],
                532
                )
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_3"],
                dic_coords_spu["coords_partie_3"],
                532
                )
        
        pdb.gimp_layer_set_offsets(
                dic_parties["partie_4"],
                dic_coords_spu["coords_partie_4"],
                532
                )
    
foreground = couleur_texte

###### =================================== TITRAGE ===========================================

nom_ecole = centrer.centrer_texte(nom_ecole)
titre_spectacle = centrer.centrer_texte(titre_spectacle)

nb_lignes = decoupe_titres.longueur(nom_ecole, titre_spectacle)
nb_lignes_ecole = decoupe_titres.longueur(nom_ecole)
nb_lignes_titre = decoupe_titres.longueur(titre_spectacle)

offset_top = 25
offset_bottom = 135

                    ######### debut ecole ##########


we = 30
layer_ecole = pdb.gimp_text_layer_new(fond, nom_ecole, "sans bold", we, 0)
width_ecole = pdb.gimp_drawable_width(layer_ecole)
height_ecole = pdb.gimp_drawable_height(layer_ecole)
while width_ecole > 750 :
    we = we -5
    layer_ecole = pdb.gimp_text_layer_new(fond, nom_ecole, "sans bold", we, 0)
    width_ecole = pdb.gimp_drawable_width(layer_ecole)
    height_ecole = pdb.gimp_drawable_height(layer_ecole)
pdb.gimp_image_add_layer(
    fond,
    layer_ecole,
    0
    )

#### ECOLE >>> violet = r93 v26 b109 ### (0.36,0.1,0.43,1.0)
#### ECOLE >>> rose = r229 v68 b135 ###
#### ECOLE >>> rose = 0.89 0.27 0.53 ###
#### ECOLE >>> choco = r103 v59 b20 ###
#### ECOLE >>> choco = 0.40 0.23 0.08 ###
pdb.gimp_text_layer_set_color(
    layer_ecole,
    (0.40,0.23,0.08,1.0)
    )

offset_ecole = (width_image - width_ecole) / 2

pdb.gimp_layer_set_offsets(
    layer_ecole,
    offset_ecole,
    offset_top
    )
   
                      ######### debut titre ##########
    
wt = 40
layer_titre = pdb.gimp_text_layer_new(fond, titre_spectacle, "sans", wt, 0)
width_titre = pdb.gimp_drawable_width(layer_titre)
while width_titre > 800 :
    wt = wt - 5
    layer_titre = pdb.gimp_text_layer_new(fond, titre_spectacle, "sans", wt, 0)
    width_titre = pdb.gimp_drawable_width(layer_titre)
    
offset_bottom_up = offset_bottom - (nb_lignes_titre * 20) # offset_bottom_up = offset_bottom - (nb_lignes_titre * 20)

pdb.gimp_image_add_layer(
    fond,
    layer_titre,
    0
    )
#### TITRE SPECTACLE >>> violet = r93 v26 b109 ###
pdb.gimp_text_layer_set_color(
    layer_titre,
    (0.40,0.23,0.08,1.0)
    )
width_titre = pdb.gimp_drawable_width(layer_titre)
offset_titre = (width_image - width_titre) / 2
    
pdb.gimp_layer_set_offsets(
    layer_titre,
    offset_titre,
    offset_bottom_up 
    ) 
    
                    ######### debut presente ##########  
        
layer_prez = pdb.gimp_text_layer_new(fond, presente, "sans italic", 20, 0)
pdb.gimp_image_add_layer(
    fond,
    layer_prez,
    0
    )
pdb.gimp_text_layer_set_color(
    layer_prez,
    (0.39,0.78,0.89,1.0)
    )    
    ### bleu (0.39,0.78,0.89,1.0)
    
width_prez = pdb.gimp_drawable_width(layer_prez)
height_prez = pdb.gimp_drawable_height(layer_prez)

if sonsa != "" :        
    layer_sonsa = pdb.gimp_text_layer_new(fond, sonsa, "sans italic", 20, 0)
    pdb.gimp_image_add_layer(
        fond,
        layer_sonsa,
        0
        )
    pdb.gimp_text_layer_set_color(
    layer_sonsa,
    (0.39,0.78,0.89,1.0)
    )
    ### bleu (0.39,0.78,0.89,1.0)
    
    width_sonsa = pdb.gimp_drawable_width(layer_sonsa)
    height_sonsa = pdb.gimp_drawable_height(layer_sonsa)
    
    if height_prez >= height_sonsa :        
        offset_prez_vert = ( 25 + height_ecole - ( height_prez / 2 ) + (offset_bottom_up - offset_top - height_ecole) / 2 )
    else :
        height_prez = height_sonsa
        offset_prez_vert = ( 25 + height_ecole - ( height_prez / 2 ) + (offset_bottom_up - offset_top - height_ecole) / 2 )
    
    offset_prez = (width_image - width_prez - width_sonsa - 15) / 2
    offset_sonsa = (offset_prez + width_prez + 15)
    pdb.gimp_layer_set_offsets(
        layer_sonsa,
        offset_sonsa,
        offset_prez_vert
        )
        ### initialement offset prez vertical = 65  
else :
    
    offset_prez = (width_image - width_prez - 15) / 2   
    offset_prez_vert = ( 25 + height_ecole - ( height_prez / 2 ) + (offset_bottom_up - offset_top - height_ecole) / 2 )



pdb.gimp_layer_set_offsets(
    layer_prez,
    offset_prez,
    offset_prez_vert
    )
    ### initialement offset prez vertical = 65
    

layer_flat = pdb.gimp_image_flatten(fond)
pdb.file_bmp_save(fond, layer_flat, nom_export, "save3bmp")


### generation et enregistrement des images higlight ###

marqueur_page = 1   

fond1 = pdb.gimp_image_new(1024, 576, RGB)

layer_1024 = pdb.gimp_layer_new(fond1, 1024, 576, 1, "", 100, 0)

pdb.gimp_image_add_layer(
    fond1,
    layer_1024,
    0
    )

layer_sous_1 = pdb.gimp_file_load_layer(fond1, "/home/autor/Desktop/auto-ring/biblio/sous-lignage_fin_bleu22_100.png")

pdb.gimp_image_add_layer(
            fond1,
            layer_sous_1,
            0
            )

### generation des vignettes highlight###   

grosse_frame_hi = pdb.gimp_file_load_layer(fond1, "/home/autor/Desktop/auto-ring/biblio/frame_bleu_violet_index100.png")
pdb.gimp_image_add_layer(
    fond1,
    grosse_frame_hi,
    0
    )
pdb.gimp_layer_set_offsets(
    grosse_frame_hi,
    coordonnees_v-2,
    coordonnees_h-2
    )
            
layer_flat1 = pdb.gimp_image_merge_visible_layers(fond1, 0)
pdb.gimp_image_convert_indexed(fond1, 0, 0, 4, 0, 0, "4 couleurs")
pdb.gimp_image_scale(fond1, 720, 576)
pdb.file_png_save2(fond1, layer_flat1, nom_export_hi, "", 0, 0, 0, 0, 0, 0, 0, 0, 0)
pdb.gimp_image_scale(fond1, 720, 432)
pdb.file_png_save2(fond1, layer_flat1, nom_export_hi[:-4] + "_temp.png", "", 0, 0, 0, 0, 0, 0, 0, 0, 0)

fond1_L = pdb.gimp_image_new(720, 576, RGB)
layer1_L = pdb.gimp_file_load_layer(fond1_L, nom_export_hi[:-4] + "_temp.png")

pdb.gimp_image_add_layer(
    fond1_L ,
    layer1_L,
    0
    )

pdb.gimp_layer_set_offsets(
            layer1_L ,
            0 ,
            72
            )
            
pdb.gimp_layer_resize_to_image_size(layer1_L)           
layer_flat1_L = pdb.gimp_image_merge_visible_layers(fond1_L, 2)
pdb.gimp_image_convert_indexed(fond1_L, 0, 0, 4, 0, 0, "4 couleurs")
pdb.file_png_save2(fond1_L, layer_flat1_L, nom_export_hi_L, "", 0, 0, 0, 0, 0, 0, 0, 0, 0)

### generation et enregistrement des images select ###

marqueur_page = 1   

fond2 = pdb.gimp_image_new(1024, 576, RGB)

layer_1024 = pdb.gimp_layer_new(fond2, 1024, 576, 1, "", 100, 0)

pdb.gimp_image_add_layer(
    fond2,
    layer_1024,
    0
    )

layer_sous_2 = pdb.gimp_file_load_layer(fond2, "/home/autor/Desktop/auto-ring/biblio/sous-lignage_fin_bleu22_100.png")

pdb.gimp_image_add_layer(
            fond2,
            layer_sous_2,
            0
            )

grosse_frame_sel = pdb.gimp_file_load_layer(fond2, "/home/autor/Desktop/auto-ring/biblio/frame_bleu_violet_index100.png")
        
pdb.gimp_image_add_layer(
    fond2,
    grosse_frame_sel,
    0
    )
pdb.gimp_layer_set_offsets(
    grosse_frame_sel,
    coordonnees_v-2,
    coordonnees_h-2
    )
            
layer_flat2 = pdb.gimp_image_merge_visible_layers(fond2, 0)
pdb.gimp_image_convert_indexed(fond2, 0, 0, 4, 0, 0, "4 couleurs")
pdb.gimp_image_scale(fond2, 720, 576)
pdb.file_png_save2(fond2, layer_flat2, nom_export_sel, "", 0, 0, 0, 0, 0, 0, 0, 0, 0)
pdb.gimp_image_scale(fond2, 720, 432)
pdb.file_png_save2(fond2, layer_flat2, nom_export_sel[:-4] + "_temp.png", "", 0, 0, 0, 0, 0, 0, 0, 0, 0)

fond2_L = pdb.gimp_image_new(720, 576, RGB)
layer2_L = pdb.gimp_file_load_layer(fond2_L, nom_export_sel[:-4] + "_temp.png")

pdb.gimp_image_add_layer(
    fond2_L ,
    layer2_L,
    0
    )

pdb.gimp_layer_set_offsets(
            layer2_L ,
            0 ,
            72
            )
            
pdb.gimp_layer_resize_to_image_size(layer2_L)           
layer_flat2_L = pdb.gimp_image_merge_visible_layers(fond2_L, 2)
pdb.gimp_image_convert_indexed(fond2_L, 0, 0, 4, 0, 0, "4 couleurs")
pdb.file_png_save2(fond2_L, layer_flat2_L, nom_export_sel_L, "", 0, 0, 0, 0, 0, 0, 0, 0, 0)

####### fichier spumux pour menu 16:9 widescreen #########

xml_file = nom_export[:-3] + "xml"
xml_open = open(xml_file, "w")
xml_open.write(fichier_spu_debut)
xml_open.write(nom_export_hi + "'\n\t\t\tselect='" + nom_export_sel + "'>\n")

##### spumux avec des bonus #########

if bonus != "0" :
    
    ###### spumux avec une seule partie ##########
    if partie == 1:
        nombre_de_liens = les_pages_de_l_index + 2
        l,r,u,d = dico_model_indexN1["1gauche"],dico_model_indexN["1droite"],dico_model_indexN["1haut"],dico_model_indexN["1bas"]
        xml_open.write("\t\t\t<button name='1' x0='%s' y0='%s' x1='%s' y1='%s' left='%d' right='%d' up='%d' down='%d'/>\n" 
                       %(
                       180 -2,
                       176 -2,
                       536 +2,
                       464 +2,
                       l,r,u,d)
                       )
                       
        l,r,u,d = dico_model_indexB["2gauche"],dico_model_indexB["2droite"],dico_model_indexB["2haut"],dico_model_indexB["2bas"]
        xml_open.write("\t\t\t<button name='2' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                        % (
                        int(pair_000.pair_down(offset_gap/1.422)) - 2,
                        528 - 2,
                        int(pair_000.pair_up((offset_gap + dic_coords_spu["coords_layer_bonus"][0])/1.422)) + 2,
                        560 + 2,
                        l,r,u,d)
                        )
                                              
        for x in range(1, les_pages_de_l_index + 1 ) :
            l,r,u,d = dico_model_indexN1["%dgauche" %(x+2)],dico_model_indexN["%ddroite" %(x+2)],dico_model_indexN["%dhaut" %(x+2)],dico_model_indexN["%dbas"  %(x+2)]
            if r > nombre_de_liens :
                r = 2
            else :
                pass
            if d > nombre_de_liens :
                d = 2
            else :
                pass
            xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                            % (
                            x+2,
                            int(pair_000.pair_down((450 + 20 + x * 40)/1.422)),
                            528 - 2,
                            int(pair_000.pair_up(((450 + 20 + x * 40) + 14)/1.422)),
                            560 + 2,
                            l,r,u,d)
                            )
        xml_open.write(fichier_spu_fin)
        xml_open.close()
    
    
    ############### spumux avec plusieurs parties ##########
    else :
    
        nombre_de_liens = partie + 2
        l,r,u,d = dico_model_indexB["1gauche"],dico_model_indexB["1droite"],dico_model_indexB["1haut"],dico_model_indexB["1bas"]
        xml_open.write("\t\t\t<button name='1' x0='%s' y0='%s' x1='%s' y1='%s' left='%d' right='%d' up='%d' down='%d'/>\n" 
                       %(
                       180 - 2,
                       176 - 2,
                       536 + 2,
                       464 + 2,
                       l,r,u,d)
                       )
        
        l,r,u,d = dico_model_indexB["2gauche"],dico_model_indexB["2droite"],dico_model_indexB["2haut"],dico_model_indexB["2bas"]
        xml_open.write("\t\t\t<button name='2' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                        % (
                        int(pair_000.pair_down(offset_gap/1.422)) - 2,
                        528 - 2,
                        int(pair_000.pair_up((offset_gap + dic_coords_spu["coords_layer_bonus"][0])/1.422)) + 2,
                        560 + 2,
                        l,r,u,d)
                        )
                           
        for x in range(1,partie + 1) :
            l,r,u,d = dico_model_indexB["%dgauche" %(x+2)],dico_model_indexB["%ddroite" %(x+2)],dico_model_indexB["%dhaut" %(x+2)],dico_model_indexB["%dbas" %(x+2)]
            if r > nombre_de_liens :
                r = 2
            else :
                pass
            if d > nombre_de_liens :
                d = 2
            else :
                pass
            xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                            % (
                            x+2,
                            int(pair_000.pair_down(dic_coords_spu["coords_partie_" + str(x)]/1.422)) - 2,
                            528 - 2,
                            int(pair_000.pair_up((dic_coords_spu["coords_partie_" + str(x)] + dic_tailles_parties["partie_" + str(x)])/1.422)) +2,
                            560 + 2,
                            l,r,u,d)
                            )
        xml_open.write(fichier_spu_fin)
        xml_open.close()

else :
    ######## spumux sans bonus ############
    
    ######## spumux une seule partie ############ 
    
    if partie == 1:
        l,r,u,d = dico_model_indexN1["1gauche"],dico_model_indexN["1droite"],dico_model_indexN["1haut"],dico_model_indexN["1bas"]
        xml_open.write("\t\t\t<button name='1' x0='%s' y0='%s' x1='%s' y1='%s' left='%d' right='%d' up='%d' down='%d'/>\n" 
                       %(
                       180 - 2,
                       176 - 2,
                       536 + 2,
                       464 + 2,
                       l,r,u,d)
                       )
        for x in range(1, les_pages_de_l_index + 1 ) :
            l,r,u,d = dico_model_indexN1["%dgauche" %(x+1)],dico_model_indexN["%ddroite" %(x+1)],dico_model_indexN["%dhaut" %(x+1)],dico_model_indexN["%dbas"  %(x+1)]
            if r > (les_pages_de_l_index + 1) :
                r = 2
            else :
                pass
            if d > (les_pages_de_l_index + 1) :
                d = 2
            else :
                pass
            xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                            % (
                            x+1,
                            int(pair_000.pair_down((450 + 20 + x * 40)/1.422)),
                            528 - 2,
                            int(pair_000.pair_up(((450 + 20 + x * 40) + 14)/1.422)),
                            560 + 2,
                            l,r,u,d)
                            )
        xml_open.write(fichier_spu_fin)
        xml_open.close()
    
     ######## spumux plusieures parties ############
    
    else :
        nombre_de_liens = partie + 1
        l,r,u,d = dico_model_indexN["1gauche"],dico_model_indexN["1droite"],dico_model_indexN["1haut"],dico_model_indexN["1bas"]
        xml_open.write("\t\t\t<button name='1' x0='%s' y0='%s' x1='%s' y1='%s' left='%d' right='%d' up='%d' down='%d'/>\n" 
                       %(
                       180 - 2,
                       176 - 2,
                       536 + 2,
                       464 + 2,
                       l,r,u,d)
                       )
        for x in range(1,nombre_de_liens) :
            l,r,u,d = dico_model_indexN["%dgauche" %(x+1)],dico_model_indexN["%ddroite" %(x+1)],dico_model_indexN["%dhaut" %(x+1)],dico_model_indexN["%dbas"  %(x+1)]
            if r > nombre_de_liens :
                r = 2
            else :
                pass
            if d > nombre_de_liens :
                d = 2
            else :
                pass
            xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                            % (
                            x+1,
                            int(pair_000.pair_down(dic_coords_spu["coords_partie_" + str(x)]/1.422)) - 2,
                            528 - 2,
                            int(pair_000.pair_up((dic_coords_spu["coords_partie_" + str(x)] + dic_tailles_parties["partie_" + str(x)])/1.422)) + 2,
                            560 + 2,
                            l,r,u,d)
                            )
        xml_open.write(fichier_spu_fin)
        xml_open.close()

####### fichier spumux pour menu 4:3 letterbox #########
######### new_y = (576 + 6*old_y)/8 ###########

xml_file = nom_export[:-4] + "_letterbox.xml"
xml_open = open(xml_file, "w")
xml_open.write(fichier_spu_debut)
xml_open.write(nom_export_hi[:-4] + "_letterbox.png'\n\t\t\tselect='" + nom_export_sel[:-4] + "_letterbox.png'>\n")

####### spumux avec des bonus ########

if bonus != "0" :
    
    ###### spumux une seule partie #########
    if partie == 1:
        l,r,u,d = dico_model_indexB["1gauche"],dico_model_indexB["1droite"],dico_model_indexB["1haut"],dico_model_indexB["1bas"]
        xml_open.write("\t\t\t<button name='1' x0='%s' y0='%s' x1='%s' y1='%s' left='%d' right='%d' up='%d' down='%d'/>\n" 
                       %(
                       180 - 2,
                       176 - 2,
                       536 + 2,
                       464 + 2,
                       l,r,u,d)
                       )
        
        l,r,u,d = dico_model_indexB["2gauche"],dico_model_indexB["2droite"],dico_model_indexB["2haut"],dico_model_indexB["2bas"]
        xml_open.write("\t\t\t<button name='2' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                        % (
                        int(pair_000.pair_down(offset_gap/1.422)) - 2,
                        int(pair_000.pair_down((576 + 6*528)/8)) -2,
                        int(pair_000.pair_up((offset_gap + dic_coords_spu["coords_layer_bonus"][0])/1.422)) + 2,
                        int(pair_000.pair_up((576 + 6*560)/8)) +2,
                        l,r,u,d)
                        )
                           
        for x in range(1,les_pages_de_l_index + 1) :
            l,r,u,d = dico_model_indexB["%dgauche" %(x+2)],dico_model_indexB["%ddroite" %(x+2)],dico_model_indexB["%dhaut" %(x+2)],dico_model_indexB["%dbas" %(x+2)]
            if r > (les_pages_de_l_index + 2) :
				###### change en de +1 en +2 pour permettre (en letterbox) d'atteindre le dernier bouton
                r = 2
            else :
                pass
            if d > (les_pages_de_l_index + 2) :
				###### change en de +1 en +2 pour permettre (en letterbox) d'atteindre le dernier bouton
                d = 2
            else :
                pass
            xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                            % (
                            x+ 2,
                            int(pair_000.pair_down((450 + 20 + x * 40)/1.422)),
                            int(pair_000.pair_down((576 + 6*528)/8)) -2,
                            int(pair_000.pair_up(((450 + 20 + x * 40) + 14)/1.422)),
                            int(pair_000.pair_up((576 + 6*560)/8)) +2,
                            l,r,u,d)
                            )
                            
        xml_open.write(fichier_spu_fin)
        xml_open.close()
        
        data_file = nom_export[:-4] + "_data.txt"
        data_file_open = open(data_file, "w")
        data_file_open.write("nombre de bonus = " + bonus)
        data_file_open.write("\n")
        data_file_open.write("nombre de liens sur la page index = " + str(les_pages_de_l_index + 2 ))
        data_file_open.write("\n")
        data_file_open.write("nombre de parties = " + str(partie))
        data_file_open.close()
        
    ############ spumux plusieurs parties ############  
    else :  
        nombre_de_liens = partie + 2
        l,r,u,d = dico_model_indexB["1gauche"],dico_model_indexB["1droite"],dico_model_indexB["1haut"],dico_model_indexB["1bas"]
        xml_open.write("\t\t\t<button name='1' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n" 
                        % (
                        180 -2,
                        int(pair_000.pair_down((576 + 6*176)/8)) -2,
                        536 +2,
                        int(pair_000.pair_up((576 + 6*464)/8)) +2,
                        l,r,u,d)
                        )
        
        l,r,u,d = dico_model_indexB["2gauche"],dico_model_indexB["2droite"],dico_model_indexB["2haut"],dico_model_indexB["2bas"]
        xml_open.write("\t\t\t<button name='2' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                        % (
                        int(pair_000.pair_down(offset_gap/1.422)) -2 ,
                        int(pair_000.pair_down((576 + 6*528)/8)) -2,
                        int(pair_000.pair_up((offset_gap + dic_coords_spu["coords_layer_bonus"][0])/1.422)) +2,
                        int(pair_000.pair_up((576 + 6*560)/8)) +2,
                        l,r,u,d)
                        )
        for x in range(1,partie + 1) :
            l,r,u,d = dico_model_indexB["%dgauche" %(x+2)],dico_model_indexB["%ddroite" %(x+2)],dico_model_indexB["%dhaut" %(x+2)],dico_model_indexB["%dbas" %(x+2)]
            if r > nombre_de_liens :
                r = 2
            else :
                pass
            if d > nombre_de_liens :
                d = 2
            else :
                pass
            xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                            % (
                            x+2,
                            int(pair_000.pair_down(dic_coords_spu["coords_partie_" + str(x)]/1.422)) -2,
                            int(pair_000.pair_down((576 + 6*528)/8)) -2,
                            int(pair_000.pair_up((dic_coords_spu["coords_partie_" + str(x)] + dic_tailles_parties["partie_" + str(x)])/1.422)) +2,
                            int(pair_000.pair_up((576 + 6*560)/8)) +2,
                            l,r,u,d)
                            )
        
        xml_open.write(fichier_spu_fin)
        xml_open.close()
        
        data_file = nom_export[:-4] + "_data.txt"
        data_file_open = open(data_file, "w")
        data_file_open.write("nombre de bonus = " + bonus)
        data_file_open.write("\n")
        data_file_open.write("nombre de liens sur la page index = " + str(nombre_de_liens))
        data_file_open.write("\n")
        data_file_open.write("nombre de parties = " + str(partie))
        data_file_open.close()

else :
    
    ######## spumu sans bonus #########
    
    ######## spumux une seule partie ######
    if partie == 1:
        l,r,u,d = dico_model_indexN1["1gauche"],dico_model_indexN["1droite"],dico_model_indexN["1haut"],dico_model_indexN["1bas"]
        xml_open.write("\t\t\t<button name='1' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n" 
                            % (
                            180 -2,
                            int(pair_000.pair_down((576 + 6*176)/8)) -2,
                            536 +2,
                            int(pair_000.pair_up((576 + 6*464)/8)) +2,
                            l,r,u,d)
                            )
                            
        for x in range(1, les_pages_de_l_index + 1) :
            print "--------- x letterbox", x
            l,r,u,d = dico_model_indexN1["%dgauche" %(x+1)],dico_model_indexN["%ddroite" %(x+1)],dico_model_indexN["%dhaut" %(x+1)],dico_model_indexN["%dbas"  %(x+1)]
            print l,r,u,d
            if r > (les_pages_de_l_index + 1) :
                r = 2
            else :
                pass
            if d > (les_pages_de_l_index + 1) :
                d = 2
            else :
                pass
            xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                            % (
                            x+1,
                            int(pair_000.pair_down((450 + 20 + x * 40)/1.422)),
                            int(pair_000.pair_down((576 + 6*528)/8)) -2,
                            int(pair_000.pair_up(((450 + 20 + x * 40) + 14)/1.422)),
                            int(pair_000.pair_up((576 + 6*560)/8)) +2,
                            l,r,u,d)
                            )
    
        xml_open.write(fichier_spu_fin)
        xml_open.close()
        
        data_file = nom_export[:-4] + "_data.txt"
        data_file_open = open(data_file, "w")
        data_file_open.write("nombre de bonus = " + bonus)
        data_file_open.write("\n")
        data_file_open.write("nombre de liens sur la page index = " + str(les_pages_de_l_index + 1 ))
        data_file_open.write("\n")
        data_file_open.write("nombre de parties = " + str(partie))
        data_file_open.close()
        
    else :
        
        nombre_de_liens = partie + 1
        l,r,u,d = dico_model_indexN["1gauche"],dico_model_indexN["1droite"],dico_model_indexN["1haut"],dico_model_indexN["1bas"]
        xml_open.write("\t\t\t<button name='1' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n" 
                            % (
                            180 -2,
                            int(pair_000.pair_down((576 + 6*176)/8)) -2,
                            536 +2,
                            int(pair_000.pair_up((576 + 6*464)/8)) +2,
                            l,r,u,d)
                            )
                            
        for x in range(1,nombre_de_liens) :
            l,r,u,d = dico_model_indexN["%dgauche" %(x+1)],dico_model_indexN["%ddroite" %(x+1)],dico_model_indexN["%dhaut" %(x+1)],dico_model_indexN["%dbas"  %(x+1)]
            if r > nombre_de_liens :
                r = 2
            else :
                pass
            if d > nombre_de_liens :
                d = 2
            else :
                pass
            xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                            % (
                            x+1,
                            int(pair_000.pair_down(dic_coords_spu["coords_partie_" + str(x)]/1.422)) -2,
                            int(pair_000.pair_down((576 + 6*528)/8)) -2,
                            int(pair_000.pair_up((dic_coords_spu["coords_partie_" + str(x)] + dic_tailles_parties["partie_" + str(x)])/1.422)) +2,
                            int(pair_000.pair_up((576 + 6*560)/8)) +2,
                            l,r,u,d)
                            )
    
        xml_open.write(fichier_spu_fin)
        xml_open.close()
        
        data_file = nom_export[:-4] + "_data.txt"
        data_file_open = open(data_file, "w")
        data_file_open.write("nombre de bonus = " + bonus)
        data_file_open.write("\n")
        data_file_open.write("nombre de liens sur la page index = " + str(nombre_de_liens))
        data_file_open.write("\n")
        data_file_open.write("nombre de parties = " + str(partie))
        data_file_open.close()
    

mpg_g = subprocess.Popen("convert " + nom_export + " -resize 720x576\! -type truecolor -depth 8 ppm:- | ppmtoy4m -n50 -F25:1 -A64:45 -I p -r -S 420mpeg2 | mpeg2enc -n p -f8 -b8000 -a3 -o " + nom_export[:-3] + "m2v", shell =True)

while mpg_g.poll() == None :
            pass

mpl = subprocess.Popen("mplex -f 8 -o /dev/stdout " + nom_export[:-3] + "m2v "  + "/home/autor/Desktop/auto-ring/biblio/menu_audio.ac3 | spumux -v 2 " + nom_export[:-3] + "xml > " + nom_export[:-4] + "_s0.mpg", shell = True)
while mpl.poll() == None :
            pass

mpl_l = subprocess.Popen("spumux -s 1 " + nom_export[:-4] + "_letterbox.xml < " + nom_export[:-4] + "_s0.mpg > " + nom_export[:-3] + "mpg", shell = True)
while mpl_l.poll() == None :
            pass
            
pdb.gimp_quit(0)

