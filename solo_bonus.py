#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import sys, os
import subprocess

repertoire_de_travail = "/home/autor/Desktop/temp/vdm_gimp" ###repertoire_de_travail###
nom_export = "" ###nom_export###
nom_export_hi = "" ###nom_export_hi###
couleur_hi = (1.0,0.0,0.0,0.8) ###couleur_hi####
nom_export_sel = "" ###nom_export_sel###
couleur_sel = (1.0,0.0,0.0,1.0) ###couleur_sel###
couleur_texte = (1.0,0.0,0.0,1.0) ###couleur_texte###
nombre_bonus = 1 ###nombre_bonus###
premier = "" ###premier###

fichier_spu_debut = "<subpictures>\n\t<stream>\n\t\t<spu force='yes'\n\t\tstart='00:00:00.00'\n\t\t\thighlight='"
fichier_spu_fin = "\t\t</spu>\n\t</stream>\n</subpictures>"

dic_parties = {}
marqueur_partie = 1

vignettes_index = sorted(os.listdir(repertoire_de_travail+ "/images bonus"))[0]

taille_vignettes = (500, 281)
taille_frame = (505, 286)
taille_frame_43 = (345, 286)

coordonnees_h = 180
coordonnees_v = 260

alpha = pdb.gimp_image_new(1024, 576, RGB)

fond = pdb.file_jpeg_load("/home/autor/Desktop/temp/vdm_gimp/169.jpg", "")
width_image = pdb.gimp_image_width(fond)

foreground = (0.0,0.0,0.0,1.0)
pdb.gimp_context_set_foreground(foreground)

grosse_vignette = pdb.gimp_file_load_layer(fond, repertoire_de_travail + "/images bonus/" + vignettes_index)
		
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

	
layer_flat = pdb.gimp_image_flatten(fond)
pdb.file_bmp_save(fond, layer_flat, nom_export, "save3bmp")

layer_menu =  pdb.gimp_text_layer_new(fond, "Menu", "sans", 30, 0)


pdb.gimp_image_add_layer(
	fond,
	layer_menu,
	0
	)

pdb.gimp_layer_set_offsets(
	layer_menu,
	50,
	500
	)
	
layer_flat = pdb.gimp_image_flatten(fond)
pdb.file_bmp_save(fond, layer_flat, nom_export, "save3bmp")

xml_file = nom_export[:-3] + "xml"
xml_open = open(xml_file, "w")
xml_open.write(fichier_spu_debut)
xml_open.write(nom_export_hi + "'\n\t\t\tselect='" + nom_export_sel + "'>\n")
#for x in range(0,len(range_vignettes)) :
	#xml_open.write("\t\t\t<button name='%d' x0='%d' y0='%d' x1='%d' y1='%d' left='%d' right='%d' up='%d' down='%d'/>\n"
					#% (x, liste_des_coordonnees_v_frames[x],liste_des_coordonnees_h[x],liste_des_coordonnees_v_frames[x] + taille_frame_43[0],liste_des_coordonnees_h[x] + taille_frame_43[1],1,2,3,4))
xml_open.write(fichier_spu_fin)
xml_open.close()

mpg_g = subprocess.Popen("convert " + nom_export + " -resize 720x576\! -type truecolor -depth 8 ppm:- | ppmtoy4m -n50 -F25:1 -A64:45 -I p -r -S 420mpeg2 | mpeg2enc -n p -f8 -b8000 -a3 -o " + nom_export[:-3] + "m2v", shell =True)
#mpg_g = subprocess.Popen("ffmpeg -f image2 -vcodec bmp -r 25 -loop_input -i " + nom_export + " -t 4 -target pal-dvd -aspect 16:9 -an -y " + nom_export[:-3] + "m2v", shell =True)
#mpg_g = subprocess.Popen("mencoder mf://" + nom_export + " -ni -ovc lavc -oac copy -of mpeg -mpegopts format=dvd:tsaf -lavcopts vcodec=mpeg2video:vrc_buf_size=1835:vbitrate=8000:vrc_maxrate=9500:keyint=12:vstrict=0:trell:mbd=2:precmp=2:subcmp=2:cmp=2:dia=-10:predia=-10:cbp:mv0:vqmin=1:lmin=1:dc=10:aspect=16/9 -vf scale=720:576,hqdn3d=2:1:2  -o " + nom_export[:-3] + "m2v ", shell=True)

while mpg_g.poll() == None :
			pass

mpl = subprocess.Popen("mplex -f 8 -o /dev/stdout " + nom_export[:-3] + "m2v "  + "/home/autor/Desktop/auto-ring/biblio/menu_audio.ac3 | spumux -v 2 " + nom_export[:-3] + "xml > " + nom_export[:-3] + "mpg", shell = True)
while mpl.poll() == None :
			pass

### generation et enregistrement des images higlight ###

foreground = couleur_hi
pdb.gimp_context_set_foreground(foreground)

dic_parties = {}
marqueur_page = 1	

fond1 = pdb.gimp_image_new(1024, 576, RGB)

### generation des vignettes highlight###	

grosse_frame_hi = pdb.gimp_file_load_layer(fond1, "/home/autor/Desktop/auto-ring/biblio/frame_rouge_index70.png")
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
			
layer_flat1 = pdb.gimp_image_flatten(fond1)
pdb.file_bmp_save(fond1, layer_flat1, nom_export_hi, "save1_link_bmp")

### generation et enregistrement des images select ###

foreground = couleur_sel
pdb.gimp_context_set_foreground(foreground)

dic_parties ={}
marqueur_page = 1	

fond2 = pdb.gimp_image_new(1024, 576, RGB)
grosse_frame_sel = pdb.gimp_file_load_layer(fond2, "/home/autor/Desktop/auto-ring/biblio/frame_rouge_index100.png")
		
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
			
layer_flat1 = pdb.gimp_image_flatten(fond2)
pdb.file_bmp_save(fond1, layer_flat1, nom_export_sel, "save1_link_bmp")

pdb.gimp_quit(0)

