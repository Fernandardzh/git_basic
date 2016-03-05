import random

print("Vamos a jugar\n Piedra papel tijeras lagarto spock \nSalirz para salirs\n plz no escribas nada raro!")

usuario = input("que escoges?")
juego() = []

usuario = usuario.lower()
opc = ["piedra", "papel", "tijeras", "lagarto", "spock"]
pc = opc[random.randin(0,4)]
jugadas = {0: [["aplasta", "aplasta"],[lagarto, tijeras]], 1: [["tapa", "desautoriza"],[piedra, spock]], 2: [["corta", "decapita"],[papel, lagarto]], 3: [["envenena", "come"],[spock, papel]], 4: [["rompe", "vaporiza"],[tijeras, piedra]]}

while usuario != "S":
	while not juego in valores:
    		print("que mal plan te dije que no -.- ")
        	usuario = input("que escoges?")
		
	if pc in jugadas[usuario][1]:
               	print("GANAUSUARIO")
        elif usuario in jugadas[pc][1]:
               	print("GANAMAQUINA")
        else:
               	print("EMPATE")
