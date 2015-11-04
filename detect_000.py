import sys, os, os.path
import shutil
import subprocess
import time

class Detect_mpg:
    
    def ac3(self,fichier):
        
        ac = subprocess.Popen("ffmpeg -i %s" % fichier, shell=True, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
        r_ac = ac.stderr.readlines()
        for r in r_ac :
            if "Audio:" in r.split(" "):
                if r.split(" ")[7][:-1] == "ac3" :
                    return "ac3"
                else :
                    return r.split(" ")[7][:-1]
            else :
                pass
            
class Taille_iso:
    
    def t_iso(self,fichier):
        t_i = subprocess.Popen("ls -la  %s" % fichier, shell=True, stdout=subprocess.PIPE)#, bufsize=1, universal_newlines=True)
        r_ti = t_i.stdout.readlines()
        for r in r_ti:
            return str(int(r.split(" ")[4]) / 1024 / 1024)
            
class Presence:
    
    def fichier_present(self,fichier) :
        if os.path.isfile(fichier) == True :
            return True
        else :
            return None
            
class Chapitres:
    
    def chapitres_womble(self, fichier):
        tc_chapitres = open(fichier, "r")
        lecture_tc_chapitres = tc_chapitres.readlines()
        for x in lecture_tc_chapitres :
            if x[3:8] == "total":
                return x.split(" ")[2]
            else :
                pass 
    
    def chapitres_edius(self, fichier):
        
        
        
        fichier_womble = fichier
        fichier_edius = fichier[:-3] +  "csv"

        tc_chapitres_in = open(fichier_edius, "r")
        tc_chapitres_out = open(fichier_womble, "w")
        lecture_tc_chapitres = tc_chapitres_in.readlines()
        
        for l in lecture_tc_chapitres:
            tc_chapitres_out.write(l.split(",")[1].split('"')[1] + "\n")
            
        tc_chapitres_in.close()
        tc_chapitres_out.close()
        
        return lecture_tc_chapitres[-1].split(",")[0]
        
            
detect = Detect_mpg()
#detect.ac3("/mnt/nfs1/fait_saison_2011/4546/cartes/1-6/BPAV/CLPR/800_1172_01/800_1172_01.MP4")

taille = Taille_iso()
#taille.t_iso("/mnt/isos/33_1.iso")

presence = Presence()

chapitres = Chapitres()
#print(chapitres.chapitres_edius("/mnt/nfs_out/4882/chapitres.txt"))
