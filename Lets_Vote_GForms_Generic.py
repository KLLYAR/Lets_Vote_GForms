import mechanize
import sys
from threading import *
import time
import random

#pP = People
#qtd = Quantity

link = ''
identificationNames = ['']
answers = ['']

boostVoting = False

def vote(pPAtSameTime):
    global boostVoting, qtd
    times = 1
    
    if(boostVoting):
        times = pPAtSameTime
        boostVoting = False
    else:
        times = 1
        
    for i in range(times):
        br = mechanize.Browser()
        br.open(link)
        br.select_form(nr=0)

    answer(br, answers)
    
    br.submit()
    br.close()
    print("Votes left: ", qtd)

def answer(br, array):
    cont = 1
    while(cont < len(array)):
        br.form.controls[cont].readonly = False
        br.form.controls[cont].disabled = False
    
        
        answer = br.form.controls[cont].name
        br[answer] = array[cont]

    idName = br.form.controls[0].name
    br[idName] = random.choice(identificationNames)
        
def configure(pPAtSameTime, chance):
    global boostVoting, qtd
        
    tri = random.random()
    if(qtd >= pPAtSameTime):
        if(tri > 1 - chance and tri < 1):
            print("boosting: ", pPAtSameTime)
            qtd -= pPAtSameTime - 1
            boostVoting = True
        vote(pPAtSameTime)
        qtd -= 1
        print("people at the same time: ", pPAtSameTime)
        time.sleep(0)
        
qtd = 0
def main():
    global qtd
    qtd = int(input('How many votes: '))
    while(qtd > 0):
        configure(1, 0.5)
        configure(3, 0.3)
        configure(5, 0.2)


main()
