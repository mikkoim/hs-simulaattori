# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 01:32:26 2017

@author: Mikko Impiö
"""

import time
import random
import tweepy
import schedule
import sys
from title_config import *

import markov
import txtfile_processing as tp

def tallenna(otsikko):

    # tallennetaan otsikot tiedostoon
    tiedostonimi = "otsikot.txt"

    # otsikot
    f = open(tiedostonimi,'a')
    f.write(otsikko + '\r\n')
    f.close()

def twitter(viesti):
    """
    kommunikoi twitter API:n kanssa ja twiittaa tulokset
    :param: viesti: twiitattava viesti
    :return:
    """

    #autentikoinititiedot haetaan config.py-tiedostosta
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = tweepy.API(auth)

    #päivittää statuksen
    api.update_status(viesti)


def job():
    
    path = './data/'
    h, headers = tp.read_headers(path)
    
    gen = markov.TitleGenerator()
    grams = random.choice([1,1,1,1,1,2])
    gen.train(h,grams)
    #twiittaa luodun otsikon
    otsikko = gen.generate()
    twitter(otsikko)
#    print(otsikko)
    tallenna(otsikko)
    
def jobtest():
    print("test")


def main():
    try:
        #tunnin välein twiitti
        
#        for i in range(24):
#            aika = str(i) + ":00"
#            schedule.every().day.at(aika).do(job)
    
        #twiitti minuutin välein testitarkoituksia varten
        
        for i in range(60):
            aika = "17:" + str(i)
            schedule.every().day.at(aika).do(job)
        
        
#        for i in ["09", "18"]:
#            aika = str(i) + ":00"
#            schedule.every().day.at(aika).do(job)

        while True:
            #sys.stdout.write("\r" + time.strftime("%H.%M.%S"))
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        pass

main()
