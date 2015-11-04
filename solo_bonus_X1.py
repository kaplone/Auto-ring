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
couleur_hi = (1.0,0.0,0.0,0.8) ###couleur_hi####
nom_export_sel = "" ###nom_export_sel###
couleur_sel = (1.0,0.0,0.0,1.0) ###couleur_sel###
couleur_texte = (1.0,0.0,0.0,1.0) ###couleur_texte###
premier_bonus = "" ###premier_bonus###

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

 

nom_export_hi_L = nom_export_hi[:-4] + "_letterbox.png"
nom_export_sel_L = nom_export_sel[:-4] + "_letterbox.png"

fichier_spu_debut = "<subpictures>\n\t<stream>\n\t\t<spu force='yes'\n\t\tstart='00:00:00.00'\n\t\t\thighlight='"
fichier_spu_fin = "\t\t</spu>\n\t</stream>\n</subpictures>"

dic_parties = {}
marqueur_partie = 1

taille_vignettes = (500, 281)
taille_frame = (505, 286)
taille_frame_43 = (353, 286)

coordonnees_h = 180
coordonnees_v = 260
coordonnees_v43 = 182

dico_model_indexB ={"1bas" : 2, "1droite" : 2, "1haut" : 2 , "1gauche" : 2,
                    "2bas" : 1, "2droite" : 1, "2haut" : 1 , "2gauche" : 1}

alpha = pdb.gimp_image_new(1024, 576, RGB)

fond = pdb.file_jpeg_load("/home/autor/Desktop/auto-ring/biblio/2013/authoring2013.jpg", "")
width_image = pdb.gimp_image_width(fond)

foreground = (0.40,0.23,0.08,1.0)
pdb.gimp_context_set_foreground(foreground)

grosse_vignette = pdb.gimp_file_load_layer(fond, repertoire_de_travail + "/images_bonus/" + vignette)
		
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
	
foreground = couleur_texte

layer_premier_bonus = pdb.gimp_text_layer_new(fond, premier_bonus, "sans", 30, 0)
pdb.gimp_image_add_layer(
    fond,
    layer_premier_bonus,
    0
    )
width_premier_bonus = pdb.gimp_drawable_width(layer_premier_bonus)
offset_premier_bonus = (width_image - width_premier_bonus) / 2

pdb.gimp_layer_set_offsets(
    layer_premier_bonus,
    offset_premier_bonus,
    465
    )
	
layer_flat = pdb.gimp_image_flatten(fond)
pdb.file_bmp_save(fond, layer_flat, nom_export, "save3bmp")

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

####### fichier spumux pour menu 16:9 widescreen #########

xml_file = nom_export[:-3] + "xml"
xml_open = open(xml_file, "w")
xml_open.write(fichier_spu_debut)
xml_open.write(nom_export_hi + "'\n\t\t\tselect='" + nom_export_sel + "'>\n")

l,r,u,d = dico_model_indexB["1gauche"],dico_model_indexB["1droite"],dico_model_indexB["1haut"],dico_model_indexB["1bas"]
xml_open.write("\t\t\t<button name='1' x0='%s' y0='%s' x1='%s' y1='%s' left='%d' right='%d' up='%d' down='%d'/>\n"
				%(
				180 -2,
				176 -2 ,
				536 +2,
				464 +2,
				l,r,u,d)
				)
l,r,u,d = dico_model_indexB["2gauche"],dico_model_indexB["2droite"],dico_model_indexB["2haut"],dico_model_indexB["2bas"]
xml_open.write("\t\t\t<button name='2' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
				% (
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

l,r,u,d = dico_model_indexB["1gauche"],dico_model_indexB["1droite"],dico_model_indexB["1haut"],dico_model_indexB["1bas"]
xml_open.write("\t\t\t<button name='1' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n" 
				%(			
				180 -2,
				int(pair_000.pair_down((576 + 6*176)/8)) -2,
				536 +2,
				int(pair_000.pair_up((576 + 6*464)/8)) +2,
				l,r,u,d)
				)
l,r,u,d = dico_model_indexB["2gauche"],dico_model_indexB["2droite"],dico_model_indexB["2haut"],dico_model_indexB["2bas"]
xml_open.write("\t\t\t<button name='2' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
				% (
				int(pair_000.pair_down(offset_gap/1.422)) -2,
				int(pair_000.pair_down((576 + 6*528)/8)) -2,
				int(pair_000.pair_up((offset_gap + width_element_menu)/1.422)) +2,
				int(pair_000.pair_down((576 + 6*560)/8)) +2,
				l,r,u,d)
				)
								

xml_open.write(fichier_spu_fin)
xml_open.close()

#data_file = nom_export[:-4] + "_data.txt"
#data_file_open = open(data_file, "w")
#data_file_open.write("premier bonus = " + premier_bonus)

#data_file_open.close()

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
#pdb.gimp_layer_set_offsets(
    #layer_sous_2,
    #0,
    #22
    #)

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

