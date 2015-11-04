import os


dico_des_variables = {"nombre_de_pages" : 0, "numero_de_la_page" : 0, "nombre_de_page_index" : 0, "nombre_d_images" : 0, "total" : 0}

def generation_pages(self, NOM_DE_L_ECOLE, PRESENTE, SON_SA_LEUR, SPECTACLE, NOMBRE_DE_PAGES_INDEX):
    
    if NOM_DE_L_ECOLE == None : pass
    
    else : 
        pointeur = 0
        liste_des_images= []
        images = os.listdir("images/")
        for x in images :
            dico_des_variables["nombre_d_images"] = len(liste_des_images)
            total=len(sorted(liste_des_images))-1
            dico_des_variables["total"] = total
            if total%6 == 0:
                nombre_de_pages = total/6
            else :
                nombre_de_pages = total/6+1
            #print total, nombre_de_pages
        
        dico_des_variables["nombre_de_pages"] = nombre_de_pages
        liste_html =[]
        ranges=[(0,)]

        for x in range(0, nombre_de_pages) :
            range0 = ( x*6+1, x*6+2, x*6+3,x*6+4, x*6+5,x*6+6)
            ranges.append(range0)
            print ranges
            
            #### 1 tour de boucle par vignette #####
            dico_des_variables["nombre_de_page_index"] = NOMBRE_DE_PAGES_INDEX
            decalage = dico_des_variables["nombre_de_page_index"]
            for x in (sorted(liste_des_images)[decalage:]) :
                    
                if pointeur <= total :
                    pointeur = pointeur + 1
                    
                    dico_des_variables["nombre_de_pages"] = ((pointeur-7)/6+2)-1
                    
            
def livret(self, fff):
    return dico_des_variables

