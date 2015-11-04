import sys, os, os.path
import shutil
import subprocess
import time
    
def dcm15(fichier):
    numero = fichier.split("/")[1]
    
    try :
        os.popen("ssh -t root@192.168.1.100 'mkfifo /tmp/%s_fifo.m2v'" % numero[:-4])
    except :
        pass
    subprocess.Popen("ssh -t root@192.168.1.100 'mplayer /in/%s -dumpaudio -dumpfile /temp/%s.ac3'" % (fichier, numero[:-4]), shell=True)
    subprocess.Popen("ssh -t root@192.168.1.100 'mplayer /in/%s -dumpvideo -dumpfile /tmp/%s_fifo.m2v'" % (fichier, numero[:-4]), shell=True)
    os.popen("ssh -t root@192.168.1.100 'dd if=/tmp/%s_fifo.m2v of=/temp/%s_cut.m2v bs=2015 skip=1'" % (numero[:-4], numero[:-4]))
    os.popen("ssh -t root@192.168.1.100 'mplex -f8 /temp/%s.ac3 /temp/%s_cut.m2v -o /out/%s_mplex.mpg'" % (numero[:-4], numero[:-4], fichier[:-4]))
    #subprocess.Popen("ssh -t root@192.168.1.100 'mplex -f8 %s.ac3 %s_cut.m2v -o %s_mplex.mpg'" % (fichier[:-4], fichier[:-4], fichier[:-4]), shell=True)
    
def dcm25(fichier):
    numero = fichier.split("/")[1]
    
    try :
        os.popen("ssh -t root@192.168.1.100 'mkfifo /tmp/%s_fifo.m2v'" % numero[:-4])
    except :
        pass
    subprocess.Popen("ssh -t root@192.168.1.100 'mplayer /in/%s -dumpaudio -dumpfile /temp/%s.ac3'" % (fichier, numero[:-4]), shell=True)
    subprocess.Popen("ssh -t root@192.168.1.100 'mplayer /in/%s -dumpvideo -dumpfile /tmp/%s_fifo.m2v'" % (fichier, numero[:-4]), shell=True)
    os.popen("ssh -t root@192.168.1.100 'dd if=/tmp/%s_fifo.m2v of=/temp/%s_cut.m2v bs=2025 skip=1'" % (numero[:-4], numero[:-4]))
    os.popen("ssh -t root@192.168.1.100 'mplex -f8 /temp/%s.ac3 /temp/%s_cut.m2v -o /out/%s_mplex.mpg'" % (numero[:-4], numero[:-4], fichier[:-4]))
    #subprocess.Popen("ssh -t root@192.168.1.100 'mplex -f8 %s.ac3 %s_cut.m2v -o %s_mplex.mpg'" % (fichier[:-4], fichier[:-4], fichier[:-4]), shell=True)
    
def dcm(fichier):
    os.popen("ssh -t root@192.168.1.100 'ffmpeg -i /in/%s -vn -acodec copy /temp/%s.ac3'" % (fichier, fichier[:-4]))
    os.popen("ssh -t root@192.168.1.100 'ffmpeg -i /in/%s -an -vcodec copy /temp/%s.m2v'" % (fichier, fichier[:-4]))
    subprocess.Popen("ssh -t root@192.168.1.100 'mplex -f8 /temp/%s.ac3 /temp/%s.m2v -o /out/%s_mplex.mpg'" % (fichier[:-4], fichier[:-4], fichier[:-4]), shell=True)
    
    
#import os
#import sys
#f='/home/autor/Desktop/generique_4377.mpg' 
#sys.path.append("/home/autor/Desktop/auto-ring")
#import multiplex_002
#import multiplex_002 as mul
#mul.dcm(f)

#fichier = "/files/1727/generique_1727.mpg"
#dcm15(fichier)

