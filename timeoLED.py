#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# timeoLED.py
#
# Copyright © 2013 jerome B (jblbl) <jerome@jblb.no-ip.org>
#
#
# Distributed under WTFPL terms
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.
#

# la doc de l'api : http://timeoapi.readthedocs.org/fr/latest/index.html
 
"""
  
"""
import requests
import re
import json

# from bs4 import BeautifulSoup as BS


URL="http://timeoapi.haum.org"
session = requests.Session()

session.headers.update({'User-Agent': 'timeoLED', 'Content-type': 'application/x-www-form-urlencoded'})

# session.get(URL)

get_lines = "/v1/lines"

result = session.get(URL+get_lines)

# print json.dumps(result.json())


# donc, on commence par faire défiler les noms des lignes.
# pour les besoins de l'API, le dictionnaire est mise dans : resultat['lines']

# c'est une manière de faire que je trouve dégueu : je préfère récupérer le résultat sous
# forme de string et le ramener à du python autrement (voir en dessous)
#resultat = result.json()
#lignes = resultat['lines'] # ici, lignes contient le dico kivabien

resultat_txt = result.text
resultat_json = json.loads(resultat_txt) # loads pour Load String
lignes = resultat_json['lines']

# voilà donc :) merci bien !


lignes_tup = lignes.items()
    # lignes.items() est un itérateur (une fausse liste pour faire simple)
    # qui renvoie des tuple(2) c'est à dire des couples (clé,valeur) pour le
    # dictionnaire :
    # a = {"foo": 1, "bar": 2}
    # for k,v in a.items(): print(k+" > "+str(v)) # v est un int
    # foo > 1
    # bar > 2

    # on trie la liste par numero de ligne // 2nd element du tuple  !! tri aphabetique !!
lignes_tup.sort(key=lambda tup: tup[1])

# maintenant, on fait défiler les lignes et on demande à
# l'utilisateur à chaque fois s'il veut les arrets de la ligne
#for k,v in lignes.items():
for k,v in lignes_tup:
    # lignes.items() est un itérateur (une fausse liste pour faire simple)
    # qui renvoie des tuple(2) c'est à dire des couples (clé,valeur) pour le
    # dictionnaire :
    # a = {"foo": 1, "bar": 2}
    # for k,v in a.items(): print(k+" > "+str(v)) # v est un int
    # foo > 1
    # bar > 2
    
    reponse = raw_input("Afficher arrêt pour ligne : "+k.encode('utf8')+" ? (N/o) ")
    if reponse=='o':
        result = session.get(URL+"/v1/lines/"+v)
        donnes = json.loads(result.text)
        
        print("Arrets : ")
        for i in donnes['stations'].values():
            reponse = raw_input("Afficher delais pour arret : "+i.encode('utf8')+" ? ")
            if reponse=='o':
                print(i)
                break
        break
        
    
