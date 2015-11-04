#!/usr/bin/env python
# -*- coding: utf-8 -*-

def longueur (ecole, titre = None) :
    
    l_e = len(ecole.split("\n"))
    try :
        l_t = len(titre.split("\n"))
    except :
        l_t = 0
    return l_e + l_t

