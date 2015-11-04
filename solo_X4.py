#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import sys
import os, os.path
import shutil
import subprocess

sys.path.append("/home/autor/Desktop/auto-ring")
import pair_000

dico_modele1 ={"1bas" : "2", "1droite" : "2", "1haut" : "2" , "1gauche" : "2",
               "2bas" : "3", "2droite" : "3", "2haut" : "1" , "2gauche" : "1",
               "+bas" : "+1", "+droite" : "+1", "+haut" : "1" , "+gauche" : "-1",
               "Zbas" : "1", "Zdroite" : "1", "Zhaut" : "1" , "Zgauche" : "-1"}
               
dico_modele2 ={"1bas" : "3", "1droite" : "2", "1haut" : "3" , "1gauche" : "3",
               "2bas" : "4", "2droite" : "4", "2haut" : "1" , "2gauche" : "1",
               "3bas" : "4", "3droite" : "4", "3haut" : "1" , "3gauche" : "2",
               "+bas" : "+1", "+droite" : "+1", "+haut" : "2" , "+gauche" : "-1",
               "Zbas" : "1", "Zdroite" : "1", "Zhaut" : "3" , "Zgauche" : "-1"}
               
dico_modele3 ={"1bas" : "4", "1droite" : "2", "1haut" : "4" , "1gauche" : "4",
               "2bas" : "5", "2droite" : "3", "2haut" : "1" , "2gauche" : "1",
               "3bas" : "5", "3droite" : "4", "3haut" : "2" , "3gauche" : "2",
               "4bas" : "5", "4droite" : "5", "4haut" : "2" , "4gauche" : "3",
               "+bas" : "+1", "+droite" : "+1", "+haut" : "2" , "+gauche" : "-1",
               "Zbas" : "1", "Zdroite" : "1", "Zhaut" : "2" , "Zgauche" : "-1"}
               
dico_modele4 ={"1bas" : "4", "1droite" : "2", "1haut" : "5" , "1gauche" : "5",
               "2bas" : "6", "2droite" : "3", "2haut" : "1" , "2gauche" : "1",
               "3bas" : "6", "3droite" : "4", "3haut" : "2" , "3gauche" : "2",
               "4bas" : "5", "4droite" : "5", "4haut" : "1" , "4gauche" : "3",
               "5bas" : "6", "5droite" : "6", "5haut" : "4" , "5gauche" : "4",
               "+bas" : "+1", "+droite" : "+1", "+haut" : "2" , "+gauche" : "-1",
               "Zbas" : "1", "Zdroite" : "1", "Zhaut" : "3" , "Zgauche" : "-1"}
               
dico_modele5 ={"1bas" : "4", "1droite" : "2", "1haut" : "6" , "1gauche" : "6",
               "2bas" : "5", "2droite" : "3", "2haut" : "1" , "2gauche" : "1",
               "3bas" : "7", "3droite" : "4", "3haut" : "2" , "3gauche" : "2",
               "4bas" : "6", "4droite" : "5", "4haut" : "1" , "4gauche" : "3",
               "5bas" : "7", "5droite" : "6", "5haut" : "2" , "5gauche" : "4",
               "6bas" : "7", "6droite" : "7", "6haut" : "4" , "6gauche" : "5",
               "+bas" : "+1", "+droite" : "+1", "+haut" : "5" , "+gauche" : "-1",
               "Zbas" : "1", "Zdroite" : "1", "Zhaut" : "3" , "Zgauche" : "-1"}
               
dico_modele6 ={"1bas" : "4", "1droite" : "2", "1haut" : "7" , "1gauche" : "7",
               "2bas" : "5", "2droite" : "3", "2haut" : "1" , "2gauche" : "1",
               "3bas" : "6", "3droite" : "4", "3haut" : "2" , "3gauche" : "2",
               "4bas" : "7", "4droite" : "5", "4haut" : "1" , "4gauche" : "3",
               "5bas" : "8", "5droite" : "6", "5haut" : "2" , "5gauche" : "4",
               "6bas" : "8", "6droite" : "7", "6haut" : "3" , "6gauche" : "5",
               "7bas" : "8", "7droite" : "8", "7haut" : "4" , "7gauche" : "6",
               "+bas" : "+1", "+droite" : "+1", "+haut" : "5" , "+gauche" : "-1",
               "Zbas" : "1", "Zdroite" : "1", "Zhaut" : "6" , "Zgauche" : "-1"}


repertoire_de_travail = "/home/autor/Desktop/temp/vdm_gimp" ###repertoire_de_travail###
range_vignettes_in = 1 ###range_vignettes_in###
range_vignettes_out = 6 ###range_vignettes_out###
range_numeros_in = 3 ###range_numeros_in###
range_numeros_out = 9 ###range_numeros_out###
range_page_in = 1 
range_page_out = 15 ###range_page_out###
page_en_cours = 11 ###page_en_cours###
nom_export = "" ###nom_export###
nom_export_hi = "" ###nom_export_hi###
nom_export_sel = "" ###nom_export_sel###
partie_en_cours = "" ###partie_en_cours###
partie_1_ou_2 = "" ###titre_partie###
lien_direct_autre_partie = "" ###lien_direct_autre_partie###
lien_direct_autre_partie_plus = "" ###lien_direct_autre_partie+###
total_des_pages_precedentes = 0 ###total_des_pages###
titre_label_1_ou_2 = "" ###titre_label_1_ou_2###



nom_export_hi_L = nom_export_hi[:-4] + "_letterbox.png"
nom_export_sel_L = nom_export_sel[:-4] + "_letterbox.png"

dic_vignettes = {}
dic_nums = {}
dic_nums_blur = {}
dic_pages = {}
dic_frames = {}
dic_pages_f = {}

fichier_spu_debut = "<subpictures>\n\t<stream>\n\t\t<spu\n\t\t\tforce='yes'\n\t\t\tstart='00:00:00.00'\n\t\t\thighlight='"
fichier_spu_fin = "\t\t</spu>\n\t</stream>\n</subpictures>"

range_vignettes = range(range_vignettes_in, range_vignettes_out)
range_numeros = range(range_numeros_in, range_numeros_out)
range_page = range(range_page_in, range_page_out)

liste_des_vignettes = sorted(os.listdir(repertoire_de_travail+ "/images"))

compteur = 0
marqueur= 0
marqueur_page = 1

#taille_vignettes = (300, 169)
#taille_frame = (305, 174)
#taille_frame_43 = (213, 174) ### * 9/16 * 4/3 se reduit en * 3/4

taille_vignettes = (270, 152)
#taille_frame = (274, 156)
taille_frame_43 = (198, 156)



#liste_des_coordonnees_h = (110, 110, 110, 310, 310, 310)
#liste_des_coordonnees_v = (40, 360, 680, 40, 360, 680)
#liste_des_coordonnees_v_frames = (28, 253, 478, 28, 253, 478)

liste_des_coordonnees_h = (138, 138, 138, 324, 324, 324)
liste_des_coordonnees_v = (96, 378, 660, 96, 378, 660)
#liste_des_coordonnees_v_frames = (72, 284, 496, 72, 284, 496)
#liste_des_coordonnees_v_frames = (72, 284, 496, 72, 284, 496) #### 768
liste_des_coordonnees_v_frames = (62, 260, 458, 62, 260, 458) #### 720 

#liste_des_coordonnees_h_nums = (55, 55, 55, 255, 255, 255)
#liste_des_coordonnees_v_nums = (280, 600, 920, 280, 600, 920)
#liste_des_coordonnees_v_nums2 = (250, 570, 890, 250, 570, 890)

liste_des_coordonnees_h_nums = (112, 112, 112, 298, 298, 298)
liste_des_coordonnees_v_nums = (338, 618, 898, 338, 618, 898)
liste_des_coordonnees_v_nums2 = (320, 600, 880, 320, 600, 880)

alpha = pdb.gimp_image_new(1024, 576, RGB)

fond = pdb.file_jpeg_load("/home/autor/Desktop/auto-ring/biblio/2013/authoring2013.jpg", "")

width_image = pdb.gimp_image_width(fond)

foreground = (0.0,0.0,0.0,1.0)
pdb.gimp_context_set_foreground(foreground)

######## integration des vignettes

for x in liste_des_vignettes : 

    if compteur not in range_vignettes :
        pass
    else :
        pdb.gimp_selection_none(fond)
        dic_vignettes["image_" + str(compteur)] = pdb.gimp_file_load_layer(fond, repertoire_de_travail + "/images/" + str(x))
        
        pdb.gimp_image_add_layer(
            fond,
            dic_vignettes["image_" + str(compteur)],
            0
            )
        pdb.gimp_layer_scale(
            dic_vignettes["image_" + str(compteur)],
            taille_vignettes[0], taille_vignettes[1],
            0
            )
        pdb.gimp_layer_set_offsets(
            dic_vignettes["image_" + str(compteur)],
            liste_des_coordonnees_v[marqueur],
            liste_des_coordonnees_h[marqueur]
            )
        marqueur = marqueur + 1
    compteur = compteur + 1
    
compteur = 0
marqueur = 0 

####### intégration des numeros de vignettes

for x in liste_des_vignettes:
    
    pdb.gimp_selection_none(fond)
    
    if compteur not in range_numeros :
        pass
    else :
        dic_nums_blur["texte_blur_" + str(compteur)] = pdb.gimp_text_layer_new(fond, "\n " + str(compteur), "sans bold", 22, 0)
        dic_nums["texte_" + str(compteur)] = pdb.gimp_text_layer_new(fond, "\n " + str(compteur), "sans bold", 22, 0)
        pdb.gimp_image_add_layer(
            fond,
            dic_nums_blur["texte_blur_" + str(compteur)],
            0
            )
        pdb.gimp_image_add_layer(
            fond, dic_nums["texte_" + str(compteur)],
            0
            )
        pdb.gimp_layer_resize_to_image_size(
            dic_nums_blur["texte_blur_" + str(compteur)]
            )
        pdb.gimp_by_color_select(
            dic_nums_blur["texte_blur_" + str(compteur)],
            foreground,
            0,
            0,
            0,
            0,
            0,
            0
            )
        pdb.gimp_selection_grow(
            fond,
            3
            )
        pdb.gimp_selection_feather(
            fond,
            15
            )
        pdb.gimp_edit_bucket_fill(
            dic_nums_blur["texte_blur_" + str(compteur)],
            0,
            0,
            70,
            0,
            0,
            0,
            0
            )
        if len(str(compteur)) == 1 :
            pdb.gimp_layer_set_offsets(
                dic_nums_blur["texte_blur_" + str(compteur)],
                liste_des_coordonnees_v_nums[marqueur],
                liste_des_coordonnees_h_nums[marqueur]
                )
            pdb.gimp_layer_set_offsets(
                dic_nums["texte_" + str(compteur)],
                liste_des_coordonnees_v_nums[marqueur],
                liste_des_coordonnees_h_nums[marqueur]
                )
        else :
            pdb.gimp_layer_set_offsets(
                dic_nums_blur["texte_blur_" + str(compteur)],
                liste_des_coordonnees_v_nums2[marqueur],
                liste_des_coordonnees_h_nums[marqueur]
                )
            pdb.gimp_layer_set_offsets(
                dic_nums["texte_" + str(compteur)],
                liste_des_coordonnees_v_nums2[marqueur],
                liste_des_coordonnees_h_nums[marqueur]
                )
        pdb.gimp_text_layer_set_color(
            dic_nums["texte_" + str(compteur)],
            (0.89,0.95,0.95,1.0)
            )
            
#### chiffres des vignettes >>> bleu = r100 v198 b228 (0.39,0.78,0.89,1.0)###
#### chiffres des vignettes >>> bleu pale = r229 v245 b247 ###

        marqueur = marqueur + 1
    compteur = compteur + 1
    
    
#### elements navigation >>> blanc ###
foreground = (0.95,0.95,0.95,1.0)
pdb.gimp_context_set_foreground(foreground)

### creer une liste avec les titre et tourner le nombre de fois necessaire

page = pdb.gimp_text_layer_new(fond, "PAGE : ", "sans", 20, 0)

if page_en_cours == 1 :
    if partie_en_cours != "1" :
        precedente = pdb.gimp_text_layer_new(fond, lien_direct_autre_partie, "sans", 20, 0)
    else :
        precedente = pdb.gimp_text_layer_new(fond, "MENU", "sans", 20, 0)
else :
    precedente = pdb.gimp_text_layer_new(fond, u"PR\u00c9C\u00c9DENTE", "sans", 20, 0)
if page_en_cours == range_page[-1]:
    if partie_en_cours != "4" :
        suivante = pdb.gimp_text_layer_new(fond, lien_direct_autre_partie_plus, "sans", 20, 0)
    else :
        suivante = pdb.gimp_text_layer_new(fond, "MENU", "sans", 20, 0)
else :
    suivante = pdb.gimp_text_layer_new(fond, "SUIVANTE", "sans", 20, 0)
    
precedente_width = pdb.gimp_drawable_width(precedente)
suivante_width = pdb.gimp_drawable_width(suivante)
offset_gap = 96

pdb.gimp_image_add_layer(
    fond,
    precedente,
    0
    )
pdb.gimp_image_add_layer(
    fond,
    page,
    0
    )
pdb.gimp_image_add_layer(
    fond,
    suivante,
    0
    )

pdb.gimp_layer_set_offsets(
    precedente,
    offset_gap,
    532
    )
pdb.gimp_layer_set_offsets(
    page,
    420,
    532
    )
pdb.gimp_layer_set_offsets(
    suivante,
    1024 - suivante_width - offset_gap,
    532
    )
############ titre en haut de la page ##########    
#### TITRE >>> violet = r93 v26 b109 ###
foreground = (0.40,0.23,0.08,1.0)

try :    
    layer_titre_page = pdb.gimp_text_layer_new(fond, partie_1_ou_2, "sans", 24, 0)
    pdb.gimp_image_add_layer(
        fond,
        layer_titre_page,
        0
        )
    width_titre_page = pdb.gimp_drawable_width(layer_titre_page)
    offset_titre_page = (width_image - width_titre_page) / 2
    
    pdb.gimp_layer_set_offsets(
        layer_titre_page,
        offset_titre_page,
        60
        )
        
    pdb.gimp_text_layer_set_color(
        layer_titre_page,
        (0.40,0.23,0.08,1.0)
        )
except : 
    pass
        

############ partie en haut de la page ##########
#### TITRE >>> bleu (0.39,0.78,0.89,1.0)####

layer_titre_label = pdb.gimp_text_layer_new(fond, titre_label_1_ou_2, "sans", 24, 0)
pdb.gimp_image_add_layer(
    fond,
    layer_titre_label,
    0
    )
width_titre_label = pdb.gimp_drawable_width(layer_titre_label)
offset_titre_label = (width_image - width_titre_label) / 2

pdb.gimp_layer_set_offsets(
    layer_titre_label,
    offset_titre_label,
    25
    )
    
pdb.gimp_text_layer_set_color(
    layer_titre_label,
    (0.39,0.78,0.89,1.0)
    )

dic_page_position = {}
    
######### les liens vers les pages    
    
for y in range_page :
    
############## la page en cours ###############""
    if y == page_en_cours :
        pdb.gimp_selection_none(fond)
        dic_pages["page_" + str(marqueur_page)] = pdb.gimp_text_layer_new(fond, "\n " + str(marqueur_page), "sans", 20, 0)
        dic_pages["page_blur_" + str(marqueur_page)] = pdb.gimp_text_layer_new(fond, "\n " + str(marqueur_page), "sans", 20, 0)

        dic_page_position["page_" + str(marqueur_page)] = 0
        pdb.gimp_image_add_layer(
            fond,
            dic_pages["page_blur_" + str(marqueur_page)],
            0
            )
        pdb.gimp_text_layer_set_color(
            dic_pages["page_blur_" + str(marqueur_page)],
            (0.0,0.0,0.0,1.0)
            )
            
        pdb.gimp_image_add_layer(
            fond,
            dic_pages["page_" + str(marqueur_page)],
            0
            )
        pdb.gimp_layer_set_offsets(
            dic_pages["page_blur_" + str(marqueur_page)],
            450 + 15 + marqueur_page * 40 ,
            509
            )
        pdb.gimp_layer_set_offsets(
            dic_pages["page_" + str(marqueur_page)],
            450 + 15 + marqueur_page * 40 ,
            509
            ) 
            ### 450+20 remplace 412 pour 350 ###      
        pdb.gimp_layer_resize_to_image_size(
            dic_pages["page_blur_" + str(marqueur_page)]
            )
        pdb.gimp_by_color_select(
            dic_pages["page_blur_" + str(marqueur_page)],
            (0.0,0.0,0.0,1.0),
            0,
            0,
            0,
            0,
            0,
            0
            )
        channel = pdb.gimp_selection_save(fond)
        pdb.gimp_selection_grow(
            fond,
            3
            )
        pdb.gimp_selection_feather(
            fond,
            20
            )
        pdb.gimp_edit_bucket_fill(
            dic_pages["page_blur_" + str(marqueur_page)],
            0,
            0,
            100,
            0,
            0,
            0,
            0
            )
            
        #pdb.gimp_text_layer_set_color(
            #dic_pages["page_blur_" + str(marqueur_page)],
            #(0.95,0.95,0.95,1.0)
            
        pdb.gimp_selection_none(fond)
        pdb.gimp_layer_set_mode(
            dic_pages["page_" + str(marqueur_page)],
            0
            )
        pdb.gimp_text_layer_set_color(
            dic_pages["page_" + str(marqueur_page)],
            (0.40,0.23,0.08,1.0)
            )
#### partie avant de la page en cours >>> violet = r93 v26 b109 ###

############### les vrais liens ##########
    else :
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
        #dic_width_pages[["page_" + str(marqueur_page)] = pdb.gimp_drawable_width(dic_pages["page_" + str(marqueur_page)])
    marqueur_page = marqueur_page +1
    
layer_flat = pdb.gimp_image_flatten(fond)
pdb.file_bmp_save(fond, layer_flat, nom_export, "save3bmp")

dico_modeles={"1": dico_modele1, "2": dico_modele2, "3": dico_modele3, "4": dico_modele4, "5": dico_modele5, "6": dico_modele6}
modele_a_utiliser = dico_modeles[str(range_vignettes_out - range_vignettes_in)]

##### pour les menus 16:9 widescreen ######

xml_file = nom_export[:-3] + "xml"
xml_open = open(xml_file, "w")
xml_open.write(fichier_spu_debut)
xml_open.write(nom_export_hi + "'\n\t\t\tselect='" + nom_export_sel + "'>\n")

for x in range(0,len(range_vignettes)) :
    l,r,u,d = modele_a_utiliser["%sgauche" % str(x+1)],modele_a_utiliser["%sdroite" % str(x+1)],modele_a_utiliser["%shaut" % str(x+1)],modele_a_utiliser["%sbas" % str(x+1)]
    xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%s' right='%s' up='%s' down='%s'/>\n"
                    % (
                    x+1,
                    pair_000.pair_down(liste_des_coordonnees_v_frames[x]),
                    pair_000.pair_down(liste_des_coordonnees_h[x]) - 4,
                    pair_000.pair_up(liste_des_coordonnees_v_frames[x] + taille_frame_43[0]) + 4,
                    pair_000.pair_up(liste_des_coordonnees_h[x] + taille_frame_43[1]),
                    l,r,u,d)
                    )
                    
    position_curseur = x + 1
    
position_curseur = position_curseur + 1
l,r,u,d = modele_a_utiliser["%sgauche" % str(position_curseur)],modele_a_utiliser["%sdroite" % str(position_curseur)],modele_a_utiliser["%shaut" % str(position_curseur)],modele_a_utiliser["%sbas" % str(position_curseur)]
xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%s' right='%s' up='%s' down='%s'/>\n"
                % (
                position_curseur,
                pair_000.pair_down(offset_gap/1.422),
                528,
                pair_000.pair_up((offset_gap + precedente_width)/1.422),
                560,
                l,r,u,d)
                )       
                     
position_curseur = position_curseur + 1

for x in range_page :
    if dic_page_position["page_%d" % x] == 0 :
        pass
    else :
        l,r,u,d = str(position_curseur-1),str(position_curseur+1),modele_a_utiliser["+haut"],str(position_curseur+1)
        xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%s' right='%s' up='%s' down='%s'/>\n"
                        % (
                        position_curseur,
                        pair_000.pair_down(dic_page_position["page_%d" % x]/1.422),
                        528,
                        pair_000.pair_up((dic_page_position["page_%d" % x]+14)/1.422) ,
                        560,
                        l,r,u,d)
                        )
                        
        position_curseur = position_curseur + 1

l,r,u,d = position_curseur-1,modele_a_utiliser["Zdroite"],modele_a_utiliser["Zhaut"],modele_a_utiliser["Zbas"]
xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%s' right='%s' up='%s' down='%s'/>\n"
                % (
                position_curseur,
                pair_000.pair_down((1024 - suivante_width - offset_gap)/1.422),
                528,
                pair_000.pair_up((1024 - offset_gap)/1.422),
                560,
                l,r,u,d)
                )                   

xml_open.write(fichier_spu_fin)
xml_open.close()

##### fichier spumux pour les menus 4:3 letterbox ######
######### new_y = (576 + 6*old_y)/8 ###########

xml_file = nom_export[:-4] + "_letterbox.xml"
xml_open = open(xml_file, "w")
xml_open.write(fichier_spu_debut)
xml_open.write(nom_export_hi[:-4] + "_letterbox.png'\n\t\t\tselect='" + nom_export_sel[:-4] + "_letterbox.png'>\n")

for x in range(0,len(range_vignettes)) :
    l,r,u,d = modele_a_utiliser["%sgauche" % str(x+1)],modele_a_utiliser["%sdroite" % str(x+1)],modele_a_utiliser["%shaut" % str(x+1)],modele_a_utiliser["%sbas" % str(x+1)]
    xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%s' right='%s' up='%s' down='%s'/>\n"
                    % (
                    x+1,
                    pair_000.pair_down(liste_des_coordonnees_v_frames[x]),
                    pair_000.pair_down((576 + 6*liste_des_coordonnees_h[x]-4)/8),
                    pair_000.pair_up(liste_des_coordonnees_v_frames[x] + taille_frame_43[0]),
                    pair_000.pair_up((576 + 6*(liste_des_coordonnees_h[x] + taille_frame_43[1]+4))/8),
                    l,r,u,d)
                    )
                    
    position_curseur = x + 1
    
position_curseur = position_curseur + 1
l,r,u,d = modele_a_utiliser["%sgauche" % str(position_curseur)],modele_a_utiliser["%sdroite" % str(position_curseur)],modele_a_utiliser["%shaut" % str(position_curseur)],modele_a_utiliser["%sbas" % str(position_curseur)]
xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%s' right='%s' up='%s' down='%s'/>\n"
                % (
                position_curseur,
                pair_000.pair_down(offset_gap/1.422),
                pair_000.pair_down((576 + 6*528)/8),
                pair_000.pair_up((offset_gap + precedente_width)/1.422),
                pair_000.pair_up((576 + 6*560)/8),
                l,r,u,d)
                )   
                         
position_curseur = position_curseur + 1

for x in range_page :
    if dic_page_position["page_%d" % x] == 0 :
        pass
    else :
        l,r,u,d = str(position_curseur-1),str(position_curseur+1),modele_a_utiliser["+haut"],str(position_curseur+1)
        xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%s' right='%s' up='%s' down='%s'/>\n"
                        % (
                        position_curseur,
                        pair_000.pair_down(dic_page_position["page_%d" % x]/1.422),
                        pair_000.pair_down((576 + 6*528)/8),
                        pair_000.pair_up((dic_page_position["page_%d" % x] + 14)/1.422),
                        pair_000.pair_up((576 + 6*560)/8),
                        l,r,u,d)
                        )
                        
        position_curseur = position_curseur + 1

l,r,u,d = position_curseur-1,modele_a_utiliser["Zdroite"],modele_a_utiliser["Zhaut"],modele_a_utiliser["Zbas"]
xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%s' right='%s' up='%s' down='%s'/>\n"
                % (
                position_curseur,
                pair_000.pair_down((1024 - suivante_width - offset_gap)/1.422),
                pair_000.pair_down((576 + 6*528)/8),
                pair_000.pair_up((1024 - offset_gap)/1.422),
                pair_000.pair_up((576 + 6*560)/8),
                l,r,u,d)
                )                   

xml_open.write(fichier_spu_fin)
xml_open.close()

##############
## creation du fichier Data.txt
###################

data_file = nom_export[:-4] + "_data.txt"
data_file_open = open(data_file, "w")
data_file_open.write("numero premiere vignette = " + str(range_numeros_in))
data_file_open.write("\n")
data_file_open.write("nombre de vignettes = " + str(range_numeros_out - range_numeros_in))
data_file_open.write("\n")

#data_file_open.write("cible lien gauche = " + str(total_des_pages_precedentes - 1))
data_file_open.write("cible lien gauche = " + str(total_des_pages_precedentes))
data_file_open.write("\n")
data_file_open.write("nombre d'autres pages = " + str(range_page_out - range_page_in - 1))
data_file_open.write("\n")
data_file_open.write("numero page en cours = " + str(page_en_cours))
data_file_open.write("\n")
#data_file_open.write("cible lien droite = " + str(total_des_pages_precedentes + 1))
data_file_open.write("cible lien droite = " + str(total_des_pages_precedentes + 2))
data_file_open.write("\n")
if partie_en_cours == "1":
    data_file_open.write("positition de la page dans le xml = " + str(page_en_cours + 1)) ### l'index vaut 1
if partie_en_cours == "2":
    data_file_open.write("positition de la page dans le xml = " + str(total_des_pages_precedentes + 1)) ### l'index vaut 1
if partie_en_cours == "3":
    data_file_open.write("positition de la page dans le xml = " + str(total_des_pages_precedentes + 1)) ### l'index vaut 1
if partie_en_cours == "4":
    data_file_open.write("positition de la page dans le xml = " + str(total_des_pages_precedentes + 1)) ### l'index vaut 1
data_file_open.close()

### generation et enregistrement des images higlight ###

compteur = 0
marqueur= 0
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
#pdb.gimp_layer_set_offsets(
    #layer_sous_1,
    #0,
    #22
    #)

for x in liste_des_vignettes:
    if compteur not in range_vignettes :
        pass
    else :
        pdb.gimp_selection_none(fond1)
        dic_frames["frame_" + str(compteur)] = pdb.gimp_file_load_layer(fond1, "/home/autor/Desktop/auto-ring/biblio/frame_bleu_violet100.png")
        dic_pages_f["page_f" + str(marqueur_page)] = pdb.gimp_text_layer_new(fond, "\n " + str(marqueur_page), "sans", 30, 0)
        
        pdb.gimp_image_add_layer(
            fond1,
            dic_frames["frame_" + str(compteur)],
            0
            )
        pdb.gimp_layer_set_offsets(
            dic_frames["frame_" + str(compteur)],
            liste_des_coordonnees_v[marqueur]-2,
            liste_des_coordonnees_h[marqueur]-2
            )
        marqueur = marqueur + 1
    compteur = compteur + 1
            

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

compteur = 0
marqueur= 0
marqueur_page = 1   

fond2 = pdb.gimp_image_new(1024, 576, RGB)

layer_1024_2 = pdb.gimp_layer_new(fond2, 1024, 576, 1, "", 100, 0)

pdb.gimp_image_add_layer(
    fond2,
    layer_1024_2,
    0
    )
    
layer_sous_2 = pdb.gimp_file_load_layer(fond2, "/home/autor/Desktop/auto-ring/biblio/sous-lignage_fin_bleu22_100.png")

pdb.gimp_image_add_layer(
            fond2,
            layer_sous_2,
            0
            )
#pdb.gimp_layer_set_offsets(
    #layer_sous_2,
    #0,
    #22
    #)

for x in liste_des_vignettes:
    if compteur not in range_vignettes :
        pass
    else :
        pdb.gimp_selection_none(fond2)
        dic_frames["frame_" + str(compteur)] = pdb.gimp_file_load_layer(fond2, "/home/autor/Desktop/auto-ring/biblio/frame_bleu_violet100.png")
        dic_pages_f["page_f" + str(marqueur_page)] = pdb.gimp_text_layer_new(fond, "\n " + str(marqueur_page), "sans", 30, 0)
        
        pdb.gimp_image_add_layer(
            fond2,
            dic_frames["frame_" + str(compteur)],
            0
            )
        pdb.gimp_layer_set_offsets(
            dic_frames["frame_" + str(compteur)],
            liste_des_coordonnees_v[marqueur]-2,
            liste_des_coordonnees_h[marqueur]-2
            )
        marqueur = marqueur + 1
    compteur = compteur + 1
            
layer_flat2 = pdb.gimp_image_merge_visible_layers(fond2, 0)
pdb.gimp_image_convert_indexed(fond2, 0, 0, 4, 0, 0, "4 couleurs")
pdb.gimp_image_scale(fond2, 720, 576)
pdb.file_png_save2(fond2, layer_flat2, nom_export_sel, "", 0, 0, 0, 0, 0, 0, 0, 0, 1)
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

mpg_g = subprocess.Popen("convert " + nom_export + " -resize 720x576\! -type truecolor -depth 8 ppm:- | ppmtoy4m -n50 -F25:1 -A64:45 -I p -r -S 420mpeg2 | mpeg2enc -n p -f8 -b8000 -a3 -o " + nom_export[:-3] + "m2v", shell =True)

while mpg_g.poll() == None :
            pass

mpl = subprocess.Popen("mplex -f 8 -o /dev/stdout " + nom_export[:-3] + "m2v "  + "/home/autor/Desktop/auto-ring/biblio/menu_audio.ac3 | spumux -v 2 " + nom_export[:-3] + "xml > " + nom_export[:-4] + "_s0.mpg", shell = True)
while mpl.poll() == None :
            pass

mpl_l = subprocess.Popen("spumux -s 1 -v 2 " + nom_export[:-4] + "_letterbox.xml < " + nom_export[:-4] + "_s0.mpg > " + nom_export[:-3] + "mpg", shell = True)
while mpl_l.poll() == None :
            pass



pdb.gimp_quit(0)

