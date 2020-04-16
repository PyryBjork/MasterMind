import random 
import time
import numpy as np

OikeaVastaus = random.sample(range(1,8),4)
Pelijatkuu = True

rivi1 = [0,0,0,0]
rivi2 = [0,0,0,0]
rivi3 = [0,0,0,0]
rivi4 = [0,0,0,0]
rivi5 = [0,0,0,0]
rivi6 = [0,0,0,0]
rivi7 = [0,0,0,0]
rivi8 = [0,0,0,0]
rivi9 = [0,0,0,0]

rivi1tarkistus = [0,0]
rivi2tarkistus = [0,0]
rivi3tarkistus = [0,0]
rivi4tarkistus = [0,0]
rivi5tarkistus = [0,0]
rivi6tarkistus = [0,0]
rivi7tarkistus = [0,0]
rivi8tarkistus = [0,0]
rivi9tarkistus = [0,0]

def nayta():   #Tulostaa pelitilanteen
	print("Oikea paikka", "  Oikea numero")   
	print("    ",rivi9tarkistus[0],rivi9,rivi9tarkistus[1])
	print("    ",rivi8tarkistus[0],rivi8,rivi8tarkistus[1])
	print("    ",rivi7tarkistus[0],rivi7,rivi7tarkistus[1])																						
	print("    ",rivi6tarkistus[0],rivi6,rivi6tarkistus[1])																						
	print("    ",rivi5tarkistus[0],rivi5,rivi5tarkistus[1])																						
	print("    ",rivi4tarkistus[0],rivi4,rivi4tarkistus[1])
	print("    ",rivi3tarkistus[0],rivi3,rivi3tarkistus[1])
	print("    ",rivi2tarkistus[0],rivi2,rivi2tarkistus[1])
	print("    ",rivi1tarkistus[0],rivi1,rivi1tarkistus[1])

#----------------------------------------------------------------------------------------------------------------------------------------------

def kysy(Rivi, TarkistusRivi): #kysyy uuden rivin ja tarkistaa onko se sallittu ja montako oikeaa variä ja montako niistä oli oikealla paikalla
	
	tarkistus = True
	OikeaVari = 0
	OikeaPaikka = 0

	
	while tarkistus:
		
		vastaus = list(map(int,input("\nVastaus: ").strip().split()))[:5] #kysyy numeroita ja muuttaa vastauksen listaksi
		
		print("Tarksitetaan...")
		print(vastaus)
	
		if len(vastaus) == 4: #tarkistaa vastauksen pituuden
	
			print("oikea pituus...")
		
			ForTarkistus = True
		
			for i in range(4):
			
				if ForTarkistus == True:
				
					if 0 < vastaus[i] < 9:  #tarkistaa onko vastauksen numerot väliltä 1 - 8
						print("kohta",i + 1,"hyväksytty")
						
					else:
						print("kohta",i + 1,"hylätty")
						print("Voit arvata vain numeroita 1 - 8")
						ForTarkistus = False
				
				if i == 3 and ForTarkistus == True:
					
					if np.unique(vastaus).size == len(vastaus):  #tarkistaa onko kaikki vastauksen numerot eri numeroita
						tarkistus = False
						
					else:
						print("Vastauksessa ei saa olla useampaa samaa numeroa!")
		else:
			print("Vastauksen pitää olla neljä numeroa!")	
			
	tarkistus = True
	
	for i in range(4):  #tarkistaa oikeat numerot
		
		if vastaus[i] == OikeaVastaus[i]:
			OikeaPaikka = OikeaPaikka + 1
			
		if OikeaVastaus[i] in vastaus:
			OikeaVari = OikeaVari + 1
			
	OikeaVari = OikeaVari - OikeaPaikka
	
	
	TarkistusRivi[0] = OikeaPaikka # lisää tarkastuksn tulokset
	TarkistusRivi[1] = OikeaVari
	
	for i in range(4): # laittaa vastauksen määrätylle riville
		Rivi[i] = vastaus[i]

#--------------------------------------------------------------------------------------------------------------------------------
	
print("\n\n  Tervetuloa pelaamaan peliä nimeltä MasterMind!") #alku tekstit

time.sleep(1)

print("\n  Tässä pelissä sinun pitää päätellä nelinumeroinen koodi vihjeiden mukaisesti.")

time.sleep(2)

print("\n  Keskellä näkyy arvauksesi.\n\n  Oikealla puolella näkyy väärillä paikoilla olevien oikeiden numeroiden määrä.\n\n  Vasemmalla pulolla näkyy oikealla paikalla olevien oikeiden numeroiden määrä.")

time.sleep(2)

print("\n  Vastauksessa jokaisen numeron väliin tulee väli esim. 1 2 3 4") 

time.sleep(1)

print("\n  koodissa on neljä numeroa väliltä 1 - 8 \n") 

time.sleep(1)

nayta()

while Pelijatkuu: #toistaa peliä ja tarkastaa voiton
	
	for i in range(1):
		kysy(rivi1, rivi1tarkistus)
		nayta()
		
		if rivi1tarkistus[0] == 4: 
			print("Oikein! Voitit pelin!")
			break
		
		kysy(rivi2, rivi2tarkistus)
		nayta()
		
		if rivi2tarkistus[0] == 4:
			print("Oikein! Voitit pelin!")
			break
		
		kysy(rivi3, rivi3tarkistus)
		nayta()
		
		if rivi3tarkistus[0] == 4:
			print("Oikein! Voitit pelin!")
			break
		
		kysy(rivi4, rivi4tarkistus)
		nayta()
		
		if rivi4tarkistus[0] == 4:
			print("Oikein! Voitit pelin!")
			break
		
		kysy(rivi5, rivi5tarkistus)
		nayta()
		
		if rivi5tarkistus[0] == 4:
			print("Oikein! Voitit pelin!")
			break
		
		kysy(rivi6, rivi6tarkistus)
		nayta()
		
		if rivi6tarkistus[0] == 4:
			print("Oikein! Voitit pelin!")
			break
		
		kysy(rivi7, rivi7tarkistus)
		nayta()
		
		if rivi7tarkistus[0] == 4:
			print("Oikein! Voitit pelin!")
			break
		
		kysy(rivi8, rivi8tarkistus)
		nayta()
		
		if rivi8tarkistus[0] == 4:
			print("Oikein! Voitit pelin!")
			break
		
		kysy(rivi9, rivi9tarkistus)
		nayta()
		
		if rivi9tarkistus[0] == 4:
			print("Oikein! Voitit pelin!")
			break
			
		print("Hävisit pelin! Yritykset loppuivat!")
		
	print("koodi oli ", OikeaVastaus)
		
	ke = input("Haluatko pelata uudestaa? K/E :")
	if ke == "K":
		print("Uusi peli!") # nollataan taulukko ja arvotaan uusi vastaus
		
		OikeaVastaus = random.sample(range(1,8),4)
		
		rivi1 = [0,0,0,0]
		rivi2 = [0,0,0,0]
		rivi3 = [0,0,0,0]
		rivi4 = [0,0,0,0]
		rivi5 = [0,0,0,0]
		rivi6 = [0,0,0,0]
		rivi7 = [0,0,0,0]
		rivi8 = [0,0,0,0]
		rivi9 = [0,0,0,0]

		rivi1tarkistus = [0,0]
		rivi2tarkistus = [0,0]
		rivi3tarkistus = [0,0]
		rivi4tarkistus = [0,0]
		rivi5tarkistus = [0,0]
		rivi6tarkistus = [0,0]
		rivi7tarkistus = [0,0]
		rivi8tarkistus = [0,0]
		rivi9tarkistus = [0,0]
	else:
		Pelijatkuu = False



