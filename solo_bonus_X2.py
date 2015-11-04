#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import sys, os
import subprocess

sys.path.append("/home/autor/Desktop/auto-ring")
import pair_000

repertoire_de_travail = "/home/autor/Desktop/temp/vdm_gimp" ###repertoire_de_travail###
nom_export = "" ###nom_export###
nom_export_hi = "" ###nom_export_hi###
nom_export_sel = "" ###nom_export_sel###
partie = 0 ###partie###
bonus = "" ###bonus###
couleur_texte = (1.0,0.0,0.0,1.0) ###couleur_texte###
premier_bonus = "" ###premier_bonus###
deuxieme_bonus = "" ###deuxieme_bonus###

nom_export_hi_L = nom_export_hi[:-4] + "_letterbox.png"
nom_export_sel_L = nom_export_sel[:-4] + "_letterbox.png"

fichier_spu_debut = "<subpictures>\n\t<stream>\n\t\t<spu\n\t\t\tforce='yes'\n\t\t\tstart='00:00:00.00'\n\t\t\thighlight='"
fichier_spu_fin = "\t\t</spu>\n\t</stream>\n</subpictures>"

dic_parties = {}
marqueur_partie = 1

taille_vignettes = (386, 216)
taille_frame = (392, 222)
#taille_frame_43 = (296, 286)
# diviser par 1.43
taille_frame_43 = (274, 222)

coordonnees_h = 190
coordonnees_v = (96, 542)
coordonnees_v43 = (67, 404)

dico_model_indexB ={"1bas" : 3, "1droite" : 2, "1haut" : 3 , "1gauche" : 3,
                    "2bas" : 3, "2droite" : 3, "2haut" : 3 , "2gauche" : 1,
                    "3bas" : 1, "3droite" : 2, "3haut" : 1 , "3gauche" : 1}

alpha = pdb.gimp_image_new(1024, 576, RGB)

fond = pdb.file_jpeg_load("/home/autor/Desktop/auto-ring/biblio/2013/authoring2013.jpg", "")

width_image = pdb.gimp_image_width(fond)

foreground = (0.40,0.23,0.08,1.0)
pdb.gimp_context_set_foreground(foreground)

base = repertoire_de_travail.split("/")[-1]

if premier_bonus ==  "Les coulisses":
    vignette = "%s_%s.jpg" %(base, "c")
elif premier_bonus ==  "Le diaporama":
    vignette = "%s_%s.jpg" %(base, "d") 
elif premier_bonus ==  "L'interview":
    vignette = "%s_%s.jpg" %(base, "i") 
elif premier_bonus ==  "Surprise !":
    vignette = "%s_%s.jpg" %(base, "s") 
elif premier_bonus ==  "Le best of":
    vignette = "%s_%s.jpg" %(base, "b") 
elif premier_bonus ==  u"Les r\u00e9p\u00e9titions":
    vignette = "%s_%s.jpg" %(base, "r") 
else :
    vignette = "%s_%s.jpg" %(base, "a")
vignette_1 = pdb.gimp_file_load_layer(fond, repertoire_de_travail + "/images_bonus/" + vignette)

if deuxieme_bonus ==  "Les coulisses":
    vignette = "%s_%s.jpg" %(base, "c") 
elif deuxieme_bonus ==  "Le diaporama":
    vignette = "%s_%s.jpg" %(base, "d") 
elif deuxieme_bonus ==  "L'interview":
    vignette = "%s_%s.jpg" %(base, "i") 
elif deuxieme_bonus ==  "Surprise !":
    vignette = "%s_%s.jpg" %(base, "s") 
elif deuxieme_bonus ==  "Le best of":
    vignette = "%s_%s.jpg" %(base, "b") 
elif deuxieme_bonus ==  u"Les r\u00e9p\u00e9titions":
    vignette = "%s_%s.jpg" %(base, "r") 
else :
    vignette = "%s_%s.jpg" %(base, "a")
vignette_2 = pdb.gimp_file_load_layer(fond, repertoire_de_travail + "/images_bonus/" + vignette)

        
pdb.gimp_image_add_layer(
    fond,
    vignette_1,
    0
    )
pdb.gimp_layer_scale(
    vignette_1,
    taille_vignettes[0], taille_vignettes[1],
    0
    )
pdb.gimp_layer_set_offsets(
    vignette_1,
    coordonnees_v[0],
    coordonnees_h
    )
    
pdb.gimp_image_add_layer(
    fond,
    vignette_2,
    0
    )
pdb.gimp_layer_scale(
    vignette_2,
    taille_vignettes[0], taille_vignettes[1],
    0
    )
pdb.gimp_layer_set_offsets(
    vignette_2,
    coordonnees_v[1],
    coordonnees_h
    )   
    
foreground = (0.40,0.23,0.08,1.0)
pdb.gimp_context_set_foreground(foreground)

layer_titre_bonus = pdb.gimp_text_layer_new(fond, "Bonus", "sans", 50, 0)
pdb.gimp_image_add_layer(
    fond,
    layer_titre_bonus,
    0
    )
width_titre_bonus = pdb.gimp_drawable_width(layer_titre_bonus)
offset_titre_bonus = (width_image - width_titre_bonus) / 2

pdb.gimp_layer_set_offsets(
    layer_titre_bonus,
    offset_titre_bonus,
    45
    )
    
foreground = (0.40,0.23,0.08,1.0)
pdb.gimp_context_set_foreground(foreground)

layer_bonus_1 = pdb.gimp_text_layer_new(fond, premier_bonus, "sans", 30, 0)
width_layer_bonus_1 = pdb.gimp_drawable_width(layer_bonus_1)
layer_bonus_2 = pdb.gimp_text_layer_new(fond, deuxieme_bonus, "sans", 30, 0)
width_layer_bonus_2 = pdb.gimp_drawable_width(layer_bonus_2)


pdb.gimp_image_add_layer(
    fond,
    layer_bonus_1,
    0
    )
pdb.gimp_image_add_layer(
    fond,
    layer_bonus_2,
    0
    )

pdb.gimp_layer_set_offsets(
    layer_bonus_1,
    290 - (width_layer_bonus_1 / 2),
    420
    )
pdb.gimp_layer_set_offsets(
    layer_bonus_2,
    1024 - (290 + (width_layer_bonus_2 / 2)),
    420
    )

layer_titre_bonus = pdb.gimp_text_layer_new(fond, "Bonus", "sans", 50, 0)
pdb.gimp_image_add_layer(
    fond,
    layer_titre_bonus,
    0
    )
width_titre_bonus = pdb.gimp_drawable_width(layer_titre_bonus)
offset_titre_bonus = (width_image - width_titre_bonus) / 2

pdb.gimp_layer_set_offsets(
    layer_titre_bonus,
    offset_titre_bonus,
    45
    )

foreground = (0.95,0.95,0.95,1.0)
pdb.gimp_context_set_foreground(foreground)
offset_gap = 96
layer_menu =  pdb.gimp_text_layer_new(fond, "MENU", "sans", 20, 0)

width_element_menu = pdb.gimp_drawable_width(layer_menu)


pdb.gimp_image_add_layer(
    fond,
    layer_menu,
    0
    )

pdb.gimp_layer_set_offsets(
    layer_menu,
    offset_gap,
    532
    )
    
    
    
layer_flat = pdb.gimp_image_flatten(fond)
pdb.file_bmp_save(fond, layer_flat, nom_export, "save3bmp")


### generation et enregistrement des images higlight ###

dic_parties = {}
marqueur_page = 1   

fond1 = pdb.gimp_image_new(1024, 576, RGB)

layer_1024 = pdb.gimp_layer_new(fond1, 1024, 576, 1, "", 100, 0)

pdb.gimp_image_add_layer(
    fond1,
    layer_1024,
    0
    )


### generation des vignettes highlight###   

frame_1_hi = pdb.gimp_file_load_layer(fond1, "/home/autor/Desktop/auto-ring/biblio/frame_bleue_bonus_X2_100.png")
frame_2_hi = pdb.gimp_file_load_layer(fond1, "/home/autor/Desktop/auto-ring/biblio/frame_bleue_bonus_X2_100.png")

layer_sous_1 = pdb.gimp_file_load_layer(fond1, "/home/autor/Desktop/auto-ring/biblio/sous-lignage_fin_bleu22_100.png")

pdb.gimp_image_add_layer(
	fond1,
	layer_sous_1,
	0
	)

pdb.gimp_image_add_layer(
    fond1,
    frame_1_hi,
    0
    )

pdb.gimp_layer_set_offsets(
    frame_1_hi,
    coordonnees_v[0]-2,
    coordonnees_h -2
    )
pdb.gimp_image_add_layer(
    fond1,
    frame_2_hi,
    0
    )

pdb.gimp_layer_set_offsets(
    frame_2_hi,
    coordonnees_v[1] -2,
    coordonnees_h -2
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

dic_parties ={}
marqueur_page = 1   

fond2 = pdb.gimp_image_new(1024, 576, RGB)

layer_1024_2 = pdb.gimp_layer_new(fond2, 1024, 576, 1, "", 100, 0)

pdb.gimp_image_add_layer(
    fond2,
    layer_1024_2,
    0
    )


frame_1_sel = pdb.gimp_file_load_layer(fond2, "/home/autor/Desktop/auto-ring/biblio/frame_bleue_bonus_X2_100.png")
frame_2_sel = pdb.gimp_file_load_layer(fond2, "/home/autor/Desktop/auto-ring/biblio/frame_bleue_bonus_X2_100.png")

layer_sous_2 = pdb.gimp_file_load_layer(fond2, "/home/autor/Desktop/auto-ring/biblio/sous-lignage_fin_bleu22_100.png")

pdb.gimp_image_add_layer(
	fond2,
	layer_sous_2,
	0
	)

pdb.gimp_image_add_layer(
    fond2,
    frame_1_sel,
    0
    )

pdb.gimp_layer_set_offsets(
    frame_1_sel,
    coordonnees_v[0]-2,
    coordonnees_h -2
    )
pdb.gimp_image_add_layer(
    fond2,
    frame_2_sel,
    0
    )

pdb.gimp_layer_set_offsets(
    frame_2_sel,
    coordonnees_v[1]-2,
    coordonnees_h -2
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
for x in range(0,2) :
    l,r,u,d = dico_model_indexB["%dgauche" %(x+1)],dico_model_indexB["%ddroite" %(x+1)],dico_model_indexB["%dhaut" %(x+1)],dico_model_indexB["%dbas" %(x+1)]
    xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                    % (
                    x+1,
                    int(pair_000.pair_down(coordonnees_v[x]/1.422)) -2,
                    coordonnees_h - 2,
                    int(pair_000.pair_down((coordonnees_v[x] + taille_frame[0])/1.422)) +2,
                    coordonnees_h + taille_frame[1] +2,
                    l,r,u,d)
                    )
l,r,u,d = dico_model_indexB["3gauche"],dico_model_indexB["3droite"],dico_model_indexB["3haut"],dico_model_indexB["3bas"]
xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                % (
                3,              
                int(pair_000.pair_down(offset_gap/1.422)) -2,
                528 -2,
                int(pair_000.pair_up((offset_gap + width_element_menu)/1.422)) +2,
                560 +2,
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
for x in range(0,2) :
    l,r,u,d = dico_model_indexB["%dgauche" %(x+1)],dico_model_indexB["%ddroite" %(x+1)],dico_model_indexB["%dhaut" %(x+1)],dico_model_indexB["%dbas" %(x+1)]
    xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                    % (
                    x+1,
                    int(pair_000.pair_down(coordonnees_v[x]/1.422)) -2,
                    int(pair_000.pair_down((576 + 6*coordonnees_h)/8)) - 2,
                    int(pair_000.pair_down((coordonnees_v[x] + taille_frame[0])/1.422)) +2,
                    int(pair_000.pair_down((576 + 6*(coordonnees_h + taille_frame[1]))/8)) +2,
                    l,r,u,d)
                    )
l,r,u,d = dico_model_indexB["3gauche"],dico_model_indexB["3droite"],dico_model_indexB["3haut"],dico_model_indexB["3bas"]
xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
                % (
                3,              
                int(pair_000.pair_down(offset_gap/1.422)) -2,
                int(pair_000.pair_down((576 + 6*528)/8)) -2,
                int(pair_000.pair_up((offset_gap + width_element_menu)/1.422)) +2,
                int(pair_000.pair_down((576 + 6*560)/8)) +2,
                l,r,u,d)
                )
xml_open.write(fichier_spu_fin)
xml_open.close()

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

