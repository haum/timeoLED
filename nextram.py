#! /usr/bin/env python
# -*- coding:utf8 -*-
#
import requests
import re
import time
import json
import os

def main():

    while True:
        URL="http://timeoapi.haum.org"
        session = requests.Session()
        session.headers.update({'User-Agent': 'timeoLED', 'Content-type': 'application/x-www-form-urlencoded'})
        code_arret = '801'
        code_line= 'T1_A'
        result_line = json.loads(session.get(URL+"/v1/lines/"+code_line).text)
        arret = result_line['stations'][code_arret]['name']
        
    
        result_passage = session.get(URL+"/v1/stations/"+str(code_arret)+"/"+code_line)
        donnes_passage = json.loads(result_passage.text)
        if donnes_passage['stops'][0] == "now": temps = " maintenant"
        else: temps =" dans "+donnes_passage['stops'][0]
        message_led = "Prochain tram quittant "+arret+temps
        print(message_led)
        
        
        
        # for temps_pass in donnes_passage['stops']: print(temps_pass)
        # print(donnes_passage['stops'][0])
        
    
        os.system('python ./Py_affiche.py -p /dev/tab_led -m5 "{0}"'.format(message_led))
        time.sleep(60)

if __name__=='__main__':
    main()
