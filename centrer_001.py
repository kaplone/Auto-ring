#!/usr/bin/env python
# -*- coding: utf-8 -*-


def centrer_texte(texte):
    textes = texte.split("\n")
    
    l_max = 0
    
    for t in textes :
        if len(t) > l_max :
            l_max = len(t)
    
    
    for i in range(len(textes)) :
        textes[i] = " " * (l_max - len(textes[i])) + textes[i]
        #textes[i] = " " * int(l_max - len(textes[i] ) *1.1) + textes[i]
        #textes[i] = " " * int(l_max - len(textes[i] ) *1.4) + textes[i]
        #textes[i] = " " * int(l_max - len(textes[i] ) *1.7) + textes[i]
        #textes[i] = " " * int(l_max - len(textes[i]) *2.5) + textes[i]
        
    return "\n".join(textes)
