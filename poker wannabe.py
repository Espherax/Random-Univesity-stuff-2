
import random
# +++++++++++++ Inicio de Programación defensiva (9º^º)9 ++++++++++++++++++++++


# Verifica que los datos ingresados sean números enteros sin ningún carácter adicional.
def verfnum(num):
    m = 0
    for x in num:
        if x >= ":" or x < "0" or not ("0" <= x <= "9") or x == '':
            m = 1
    if m > 0 or num == '':
        again = verfnum(input("Debe ingresar un número entero, sin letras ni carácteres adicionales: "))
        again = int(again)
        return again
    else:
        num = int(num)
        return num


# Verifica que no se ingresen nombres en blanco
def verstr(name):
    while name == "":
        name = input("No deje espacios en blanco, vuelva a intentar: ")
    return name


# Verifica que los números ingresados sean dobles:
def verfdoble(num):
    while not num == "0" and not num == "4" and not num == "6" and not num == "8" and not num == "10":
        num = input("\nDebe ingresar un número par entre 4 y 10.\nSi no quiere apostar doble escriba un 0: ")
    num = int(num)
    return num
# ------------- Fin de programación Defensiva o(º^º)o ------------------------


# +++++++++++++ Inicio de Funciones para ambos juegos ++++++++++++++++++++++++
def nombres(nom):
    if nom:
        jug1 = verstr(input("Ingrese el nombre del jugador: "))
        return jug1
    else:
        jug1 = verstr(input("Ingrese el nombre del primer jugador: "))
        jug2 = verstr(input("Ingrese el nombre del segundo jugador: "))
        return jug1, jug2


def apuestas(cantjug):
    if cantjug:
        apuestas1 = verfnum(input("Ingrese su apuesta, sólo números: "))
        while apuestas1 <= 0:
            apuestas1 = verfnum(input("Debe ingresar una apuesta mayor a 1: "))
        return apuestas1
    else:
        apuestas1 = verfnum(input("Ingrese la apuesta del jugador 1, sólo números: "))
        while apuestas1 <= 0:
            apuestas1 = verfnum(input("Debe ingresar una apuesta mayor a 1: "))
        apuestas2 = verfnum(input("Ingrese la apuesta del jugador 2, sólo números: "))
        while apuestas2 <= 0:
            apuestas2 = verfnum(input("Debe ingresar una apuesta mayor a 1: "))
        return apuestas1, apuestas2


def continuar():
    enter = input("Pulse \"enter\" para continuar")
    while enter != "":
        enter = input("Pulse \"enter\" para continuar")


# --------------- Fin de Funciones para ambos juegos -------------------------

# +++++++++++++ Inicio de Funciones para el Juego Punto ++++++++++++++++++++++
def instruccionespunto():
    print("\n\n\n*****Instrucciones del Juego Punto:******\n·Cada jugador dispone de 4 tiradas.\n·El objetivo es sumar\
 puntos superando el puntaje del rival.\n·Los números que suman puntos son el 1,3,5.\n·El puntaje se determina según\
 las siguientes pautas:\n\t-Si sale el 1, se suma 1(un) punto (el único que muestra el dado)\n\t-Si sale el 3, se suman\
 2(dos) puntos (porque a los costados del punto central hay dos puntos).\n\t-Si sale el 5, se suman 4(cuatro) puntos\
(porque en este caso, hay cuatro puntos a los costados del central).\n\t-Si sale un número par (2, 4 o 6) no se suma\
 ningún punto (porque ese dado no tiene punto central).\n\t-Si en alguna de las tiradas el jugador saca tres números\
 pares iguales, entonces\tel jugador duplicará los puntos finales que haya sumado al terminar sus cuatro lanzamientos.")
    continuar()


def randomize():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    return d1, d2, d3


def tirardad(d1, d2, d3):
    print("Sus tiradas fueron:\nDado 1:", d1, "\nDado 2:", d2, "\nDado 3:", d3)
    doble = dobles(d1, d2, d3)
    if doble is True:
        print("Haz sacado dobles!Tu puntaje final será duplicado")
    puntaje = punto(d1, d2, d3)
    print("Tu puntaje es de:", puntaje, "\n")
    return doble, puntaje


def punto(d1, d2, d3):
    dados = d1, d2, d3
    puntaje = 0
    for x in dados:
        if x == 1:
            puntaje += 1
        elif x == 3:
            puntaje += 2
        elif x == 5:
            puntaje += 4
    return puntaje


def dobles(d1, d2, d3):
    if d1 == d2 == d3 and (d1 == 2 or d1 == 4 or d1 == 6):
        doble = True
        return doble
    else:
        doble = False
        return doble


def jugada():
    d1, d2, d3 = randomize()
    print("-" * 7, "Tirada del jugador 1", "-" * 6)
    doble1, jugador1 = tirardad(d1, d2, d3)
    continuar()
    d1, d2, d3 = randomize()
    print("-" * 7, "Tirada del jugador 2", "-" * 6)
    doble2, jugador2 = tirardad(d1, d2, d3)
    return doble1, jugador1, doble2, jugador2,


def calculos_finales(p, doble1, doble2):
    puntaje1, puntaje2 = p
    if doble1:
        puntaje1 = p[0] * 2
    if doble2:
        puntaje2 = p[1] * 2
    print("\n" * 4, "\nEl puntaje final del jugador 1:", puntaje1, "\nEl puntaje final del jugador 2:", puntaje2)
    if puntaje1 > puntaje2:
        ganador = 1
    elif puntaje1 < puntaje2:
        ganador = 2
    else:
        ganador = 0
    return ganador


def juegopunto():
    print("\n" * 3, "-" * 9, "Bienvenido al juego punto", "-" * 9, "\n" * 3)
    jugadores = nombres(False)
    apuesta = apuestas(False)
    print("-" * 9, "Jugada número 1", "-" * 9)
    jugada1 = jugada()
    print("Puntaje actual del jugador 1:", jugada1[1], "\nPuntaje actual del jugador 2:", jugada1[3])
    continuar()
    print("-" * 9, "Jugada número 2", "-" * 9)
    jugada2 = jugada()
    puntajeactual = jugada1[1] + jugada2[1], jugada1[3] + jugada2[3]
    print("Puntaje actual del jugador 1:", puntajeactual[0], "\nPuntaje actual del jugador 2:", puntajeactual[1])
    continuar()
    print("-" * 9, "Jugada número 3", "-" * 9)
    jugada3 = jugada()
    puntajeactual = puntajeactual[0] + jugada3[1], puntajeactual[1] + jugada3[3]
    print("Puntaje actual del jugador 1:", puntajeactual[0], "\nPuntaje actual del jugador 2:", puntajeactual[1])
    continuar()
    print("-" * 9, "Jugada número 4", "-" * 9)
    jugada4 = jugada()
    puntajeactual = puntajeactual[0] + jugada4[1], puntajeactual[1] + jugada4[3]
    print("Puntaje actual del jugador 1:", puntajeactual[0], "\nPuntaje actual del jugador 2:", puntajeactual[1])
    continuar()
    ganador = calculos_finales(puntajeactual, jugada1[0], jugada1[2])
    premio = apuesta[1] + apuesta[0]
    if premio >= 2000:
        porcentaje = "%25"
        comision = premio * 25 / 100
        premio -= comision
    else:
        porcentaje = "%15"
        comision = premio * 15 / 100
        premio -= comision
    if ganador == 1:
        print("*" * 3, "El ganador es el jugador 1: ", jugadores[0], "*" * 3)
        print("Su premio es de: $", premio)
        print("La comisión del casino es del", porcentaje, ": $", comision)
    elif ganador == 2:
        print("*" * 3, "El ganador es el jugador 2: ", jugadores[1], "*" * 3)
        print("Su premio es de: $", premio)
        print("La comisión del casino es del", porcentaje, ": $", comision)
    else:
        print("Empate!\nNo hubo ganadores.El casino no recibe comisión y se devuelven sus apuestas.")
        print("Apuesta del jugador 1: $", apuesta[0], "\nApuesta del jugador 2: $", apuesta[1])
    print("¡Gracias por participar!\nPresione enter para volver al menú")
    continuar()
    menupunto()


# ------------- Fin de Funciones para el Juego Punto -------------------------

# +++++++++++++ Inicio de Funciones para el Juego Craps ++++++++++++++++++++++

# Función Pase(o pass). Verifica si los números son iguales a 7 u 11 y retorna valor de verdad.
def pase(num):
    if num == 7 or num == 11:
        numpass = True
        return numpass
    else:
        numpass = False
        return numpass


# Función Craps. Verifica si son números craps y retorna valor de verdad.
def craps(num):
    if num == 2 or num == 3 or num == 12:
        numcrap = True
        return numcrap
    else:
        numcrap = False
        return numcrap


# Función principal del juego. Hemos agregado la opción de elegir entre modalidades Pass y don't pass, ya que ambas
# se contrarrestaban al apostar. No se veía muy lógico apostar en ambas.
def juegocraps():
    print("\n"*3, "-"*4, "Bienvenido al Juego Craps", "-"*4)
    print("\n\n", "-"*11, "Primer Ronda", "-"*11)
    total = 0
    continua = False
    apuestacrap = 0
    print("\n\nElje la modalidad que quieras apostar\n1 - Modalidad Pass Line\n2 - Modalidad Don't Pass Line\n3 - \
Volver al menú")
    choice = verfnum(input("Seleciona una opción: "))
    while choice != 3:
        if choice == 1:
            apuestacrap = apostar(0)
            tirada1 = tirardados()
            primera = verificarmodos(tirada1[2], apuestacrap, 0, 0)
            print("Tirada 1: ", tirada1[1], ",", tirada1[0], "=", tirada1[2])
            if primera == 1:
                total += (apuestacrap*2)
                continua = False
            else:
                total -= apuestacrap
                continua = True
            break
        elif choice == 2:
            apuestacrap = apostar(1)
            tirada1 = tirardados()
            primera = verificarmodos(tirada1[2], apuestacrap, 1, 0)
            print("Tirada 1: ", tirada1[1], ",", tirada1[0], "=", tirada1[2])
            if primera == 1:
                total += (apuestacrap*2)
                continua = False
            else:
                total -= apuestacrap
                continua = True
        elif choice == '':
            print("Debe ingresar una opción")
            choice = verfnum(input("Ingrese una opción: "))
            break
        else:
            choice = verfnum(input("Has ingresado un número erróneo.\nVuelve a intentar: "))
            break
    else:
        mainmenu()
        exit()
    modalidadactiva = choice
    print("Monto total: ", total)
    controndas = 1
    tirada2 = 0, 0, 0
    while continua:
        while tirada2[2] != 7 and tirada2[2] != tirada1[2]:
            controndas += 1
            totalronda = 0
            print("\n\nRonda", controndas)
            if modalidadactiva == 1:
                print("El número punto a igualar es: ", tirada1[2])
            else:
                print("El número punto que no debe igualar es: ", tirada1[2])
            apuesta2 = apostar(2)
            tirada2 = tirardados()
            if apuesta2[1] > 0:
                doble = verfdoble(input("Elja un Doble(hardways)[4, 8, 10, 12]: "))
            else:
                doble = 0
            modos = verificarmodos(tirada2, apuesta2, 2, doble)
            print("Sus tiradas fueron: ", tirada2[0], ",", tirada2[1], "=", tirada2[2])
            # Verifica si el field dio True. En ese caso realiza la operación.
            if modos[0]:
                totalronda += apuesta2[0]*2
            # Verifica si el Doble Field dio True. En ese caso realiza la operación.
            elif modos[1]:
                totalronda += (apuesta2[0]*2)*2
            # Verifica si el Hardways dio True. En ese caso realiza la operación.
            if modos[2] >= 7:
                if modos[2] == 9:
                    totalronda += apuesta2[1]*9
                else:
                    totalronda += apuesta2[1]*7
            print("monto de esta ronda: ", totalronda)
            total += totalronda
            print("Monto total: ", total)
        else:
            if modalidadactiva == 1:
                if tirada2[2] == tirada1[2]:
                    print("\n"*5, "Ganas por passline!")
                    total += (apuestacrap + apuestacrap)
                    print("Monto total:", total)
                    break
                else:
                    print("\n"*5, "Pierdes por passline!")
                    total -= apuestacrap
                    print("Monto total:", total)
                    break
            else:
                if tirada2[2] == tirada1[2]:
                    print("\n"*5, "Ganas por Don\'t pass line!")
                    total += apuestacrap + apuestacrap
                    print("Monto total:", total)
                    break
                else:
                    print("\n"*5, "Pierdes por Don't pass line!")
                    total -= apuestacrap
                    print("Monto total:", total)
                    break
    print("Fin de la partida!\n\n")

    if seguir():
        juegocraps()


# Función apostar, chequea la ronda, si es 0 y 1 refiera a las modalidades Pass y Don't Pass, el 2 es para la 2da ronda
def apostar(ronda):
    pline = dpline = fields = hardways = 0
    while pline == 0 and dpline == 0 and fields == 0 and hardways == 0:
        if ronda == 0:
            pline = verfnum(input("\nIngrese su apuesta para Pass Line: "))
            return pline
        if ronda == 1:
            dpline = verfnum(input("\nIngrese su apuesta para Don't Pass Line: "))
            return dpline
        elif ronda == 2:
            print("Ingrese su apuesta para las siguientes modalidades(ingrese 0 si no quiere apostar)")
            fields = verfnum(input("Apuesta para Field: "))
            hardways = verfnum(input("Apostar para Hardways: "))
            return fields, hardways
        if pline == 0 and dpline == 0 and fields == 0 and hardways == 0:
            print("Debes apostar al menos en una modalidad.\n\n")


# Función que retorna 3 valores de dados para asignar a una variable y crear una lista.
def tirardados():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    suma = d1 + d2
    return d1, d2, suma


# Funcón principal del juego. Verifica la ronda del mismo modo que verifica en las apuestas. Solo activa los campos
# Field y Hardways cuando se ha realizado una apuesta(un numero mayor a 0)
def verificarmodos(dados, valorapuesta, ronda, doble):
    passl = dontpl = False
    # total = 0
    if ronda == 2:
        field = fielddoble = hardways = False
        d1, d2 = dados[0], dados[1]
        print("Dados:", d1, d2)
        dados = d1+d2
        if valorapuesta[0] > 0:
            if dados == 3 or dados == 4 or dados == 9 or dados == 12 or dados == 11:
                print("Premio FIELD!: $", valorapuesta[0]*2)
                field = True
            elif dados == 2 or dados == 12:
                print("Premio FIELD doble!:$ ", (valorapuesta[0]*2)*2)
                fielddoble = True
            else:
                print("No ganas nada por Field")
                field = False
        if doble > 0:
            if dados == doble and (doble == 4 or doble == 6 or doble == 8 or doble == 10):
                if dados == 4 or dados == 10:
                    print("Has sacado Dobles! Multiplicas tu apuesta por 7: $", valorapuesta[1]*7)
                    hardways = 7
                elif dados == 6 or dados == 8:
                    print("Has sacado Dobles! Multiplicas tu apuesta por 9: $", valorapuesta[1]*9)
                    hardways = 9
            else:
                print("No ganas nada por Doble(Hardway)")
                hardways = 0
        print("TEST:", field, fielddoble, hardways)
        return field, fielddoble, hardways
    elif ronda == 0:
        if valorapuesta > 0:
            if pase(dados):
                print("\n****Has ganado por pass Line****: + $", valorapuesta*2, "\n")
                passl = 1
            elif craps(dados):
                print("\n****Has perdido por pass Line****: - $", valorapuesta, "\n")
                passl = 0
        return passl
    elif ronda == 1:
        if valorapuesta > 0:
            if craps(dados):
                print("\n****Has ganado por Don't Pass****: + $", valorapuesta*2, "\n")
                dontpl = 1
            elif pase(dados):
                print("\n****Has perdido por Don't Pass***: - $", valorapuesta, "\n")
                dontpl = 0
        return dontpl


def seguir():
    sigue = input("¿Quieres volver a jugar jugando? S/N")
    while sigue == 's' or sigue == 'S':
        return True
    while sigue == 'n' or sigue == 'N':
        return False
    while sigue != 'n' and sigue != 'N' and sigue != 's' and sigue != 'S':
        sigue = input("Debe introducir S (continuar) o N (No continuar): ")


# Apartado de instrucciones. (ノ^^)ノ
def instruccionespass():
    print("Modalidad Pass Line(Línea de pase o a buenas)\n1 - Se realiza un primer lanzamiento, conocido como\
lanzamiento de salida.\n2 - Ésta apuesta se gana con 7 u 11 (los pass) y se pierde con 2, 3 o 12 (los craps).\n\
3 - Si no salen ni los números pass(7 u 11) ni los números craps(2, 3 o 12), el juego continúa.\n4 - En esta etapa,\
el jugador intentará igualar el puntaje de la primera tirada. En caso de que salga 7, pierde automáticamente el \
juego.\n5 - En la segunda jugada, entonces, solo se gana al acertar el puntaje o sacar 7.\n6 - Las apuestas son 1 a 1")
    continuar()


def instruccionesdont():
    print("Modalidad Don't Pass Line (en contra o a malas):\n Es la modalidad inversa de Pass Line. En el\
tiro de salida se gana con craps y se pierde con pass. A partir del segundo tiro y una vez establecido el punto se \
gana sólo con el siete y se pierde sólo con la repetición del punto. En esta modalidad, las apuestas también se pagan \
uno a uno.")
    continuar()


def instruccionesfield():
    print("Modalidad Field:\nEn esta modalidad, las apuestas son tiro por tiro. Se gana cada vez que sale 2, 3, 4, 9,\
 10, 11, o 12. Se paga uno a uno a excepción del 2 y el 12, que pagan doble.")
    continuar()


def instruccioneshardways():
    print("Modalidad Hardways(duros o difíciles):\n Se gana cada vez que la combinación de los dados es doble y \
coincide con el número apostado por el jugador. El doble 2 y el doble 5 pagan siete a uno y el doble 3 y doble 4 \
pagan 9 a uno. Estas apuestas no juegan de salida y ganan sólo cuando el número sale difícil, es decir doble.: ")
    continuar()

# ------------- Fin de Funciones para el Juego Craps -------------------------

# +++++++++++++++++++++++++++++++++ Menúes +++++++++++++++++++++++++++++++++++++


# > Menú principal
def mainmenu():
    print("-" * 5, "Bienvendo al casino AED.", "-" * 5,
          "\n1 - Juego punto(2 jugadores)\n2 - Juego Craps (1 jugador)\n3 - Salir")
    choice = verfnum(input("Ingrese una opción: "))
    while choice != 3:
        if choice == 1:
            menupunto()
            break
        elif choice == 2:
            menucraps()
            break
        elif choice == '':
            print("Debe ingresar una opción")
            choice = verfnum(input("Ingrese una opción: "))
        else:
            print("Ha ingresado un número incorrecto, intente otra vez\n\n")
            choice = verfnum(input("Ingrese una opción: "))
    else:
        print("¡Nos vemos pronto!\n¡Que tenga un buen día! \(^-^)z")


# >>  Menú Juego Punto
def menupunto():
    print("\n" * 3)
    print("-" * 4, "Bienvenido al juego punto", "-" * 4,
          "\n1 - Comenzar Juego\n2 - Ver instrucciones\n3 - Volver al menú anterior")
    choice = verfnum(input("Ingrese una opción: "))
    while choice != 3:
        if choice == 1:
            juegopunto()
            break
        elif choice == 2:
            instruccionespunto()
            menupunto()
            break
        elif choice == '':
            print("Debe ingresar una opción")
            choice = verfnum(input("Ingrese una opción: "))
        else:
            print("Ha ingresado un número incorrecto, intente otra vez\n\n")
            choice = verfnum(input("Ingrese una opción: "))
    else:
        print("\n" * 3)
        mainmenu()


# >>  Menú Juego Craps
def menucraps():
    print("\n" * 3)
    print("Bienvenido al juego craps\n\n1 - Jugar\n2 - Instrucciones Modo Pass line\n3 - Instrucciones\
 Modo Don't Pass Line\n4 - Instrucciones  Modo Field\n5 - Instrucciones  Modo Hardways\n6 - Volver al menú anterior")
    choice = verfnum(input("Ingresar una opción: "))
    while choice != 5:
        if choice == 1:
            print("Juego Craps")
            juegocraps()
        elif choice == 2:
            print("\n\n\n", "-" * 6, "Instrucciones Modalidad Pass Line", "-" * 6)
            instruccionespass()
            menucraps()
        elif choice == 3:
            print("\n\n\n", "-" * 3, "Instrucciones Modalidad Don't Pass Line", "-" * 3)
            instruccionesdont()
        elif choice == 4:
            print("\n\n\n", "-" * 8, "Instrucciones Modalidad Field", "-" * 8)
            instruccionesfield()
        elif choice == 5:
            print("\n\n\n", "-" * 7, "Instrucciones Modalidad Hardways", "-" * 7)
            instruccioneshardways()
        elif choice == '':
            print("Debe ingresar una opción")
            choice = verfnum(input("Ingrese una opción: "))
        else:
            print("Ha ingresado un número incorrecto, intente otra vez\n\n")
            choice = verfnum(input("Ingrese una opción: "))
    else:
        print("\n" * 3)
        mainmenu()

# ----------------------------- Fin de Menúes ------------------------------------
mainmenu()