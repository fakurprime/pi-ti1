
import random as r
deste = []
el1 = []
el2 = []
el3 = []
el4 = []
zula1=[]
zula2=[]
zula3=[]
zula4=[]
puan1 = 0
puan2 = 0
puan3 = 0
puan4 = 0
#♣️♠️♥️♦️
def destediz():# 1 den 13 e kadar tüm sayıları desteye ekler ve onlara özel işaretler ekler.
    for i in range (1,14):
        kart = str(i) + "♦️"
        deste.append(kart)
    for i in range (1,14):
        kart = str(i) + "♣️"
        deste.append(kart)
    for i in range (1,14):
        kart = str(i) + "♠️"
        deste.append(kart)
    for i in range (1,14):
        kart = str(i) + "♥️"
        deste.append(kart)            
destediz()
destedenrastgelekart = deste[r.randint(0,len(deste)-1)]
orta = []
deste.remove(destedenrastgelekart)
for i in range(4):
    orta.append(destedenrastgelekart)
def kartdagıt(liste):# verilen listeye desteden rastgele 4 kart ekler.
    if len(deste) >= 4:
        for i in range(4):
            destedenrastgelekart = deste[r.randint(0,len(deste)-1)]
            deste.remove(destedenrastgelekart)
            liste.append(destedenrastgelekart)
       
kartdagıt(el1)  
kartdagıt(el2)
kartdagıt(el3)
kartdagıt(el4)
#def puanlama(zula):
#    for kartdegeri() == 1 in 


def kartdegeri(kart): #kartın son harfini silerek list yapar.
    return list(kart)[:-2]
def tur(el,zula,yapay,puan):

    if len(el) != 0:
   
        if yapay == 1:# rastgele kart atan randombot
            kartat = el[r.randint(0,len(el))-1]
            print("atılan kart: ",kartat)
            orta.append(kartat)
            if len(orta) != 1:
                if kartdegeri(kartat) == list("11"):
                    if kartdegeri(orta[0]) == list("11"):
                        print("MEGA PİŞTİ","+20 PUAN")
                        puan += 20
                    print("eli aldı!")
                    for i in orta[:]:
                        zula.append(i)
                        orta.remove(i)    
                elif kartdegeri(kartat) == kartdegeri(orta[-2]):
                    if len(orta) == 2:
                        print("PİŞTİ","+10 PUAN")
                        puan += 10
                    print("eli aldı!")
                    for i in orta[:]:
                        zula.append(i)
                        orta.remove(i)  
            el.remove(kartat)    
            
            print("orta: ",orta[-1:])
            #print("zula",zula)
            
        else:
            
            print("bu el senin",el)
            kartat = el[int(input("hangi kartı atacaksın?"))-1]
            print("atılan kart: ",kartat)
            orta.append(kartat) 
            if len(orta) != 1:
                if kartdegeri(kartat) == list("11"):
                    if kartdegeri(orta[0]) == list("11"):
                        print("MEGA PİŞTİ","+20 PUAN")
                        puan += 20
                    print("eli aldı!")
                    for i in orta[:]:
                        zula.append(i)
                        orta.remove(i)     
                elif kartdegeri(kartat) == kartdegeri(orta[-2]):
                    if len(orta) == 2:
                        print("PİŞTİ","+10 PUAN")
                        puan += 10
                    print("eli aldı!")
                    for i in orta[:]:
                        zula.append(i)
                        orta.remove(i)   
            el.remove(kartat)               
            print("orta: ",orta[-1:])
            #print("zula",zula)
#♣️♠️♥️♦️
def zulasay(zula,puan):
    puanlısayılar = ["1♣️","1♠️","1♥️","1♦️","11♣️","11♠️","11♥️","11♦️"]
    for i in puanlısayılar:
        if zula.count(i) == 1:
            puan += 1
    zulalar = [len(zula1),len(zula2),len(zula3),len(zula4)]
    max = g.biggest(zulalar)
    if len(zula1) == max:
        puan += 3
    if len(zula2) == max:
        puan += 3
    if len(zula3) == max:
        puan += 3
    if len(zula4) == max:
        puan += 3        
    
print("orta: ",orta[-1:],flush=1)  
for i in range(4):  
    tur(el1,zula1,0,puan1)
    tur(el2,zula2,1,puan2)
    tur(el3,zula3,1,puan3)
    tur(el4,zula4,1,puan4) 
    print("next")
for i in range(3):
    kartdagıt(el1)    
    kartdagıt(el2)
    kartdagıt(el3)
    kartdagıt(el4)
    for i in range(4):
        tur(el1,zula1,0,puan1)
        tur(el2,zula2,1,puan2)
        tur(el3,zula3,1,puan3)
        tur(el4,zula4,1,puan4) 
zulasay(zula1,puan1)
zulasay(zula2,puan2)
zulasay(zula3,puan3)
zulasay(zula4,puan4)
puanlar = [puan1,puan2,puan3,puan4]
print("1. ",puan1,"2. ",puan2,"3. ",puan3,"4. ",puan4)
print("kazanan: ",g.biggest(puanlar))    
