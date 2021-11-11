import random
from pokemon import Pokemon
from batalla import Batalla
import os
import winsound #canciones 
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
from tienda import Tienda
from pokedex import Pokedex

video_path="intro.mp4"
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("")
            break
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()

PlayVideo(video_path)
print("\033[1;32m")
batalla=Batalla()
tienda = Tienda() ##tienda
pokedex=[]
winsound.PlaySound('primer.wav',winsound.SND_ASYNC)
nombre = input('Cual es su nombre: ')
print('Cual sera su pokemon inicial? ')
print("1) Bulbasaur")
print("2) Charmander ")
print("3) Squirtle ")
id= int(input())
pokemon = Pokemon(id)
pokemon.apodo_pokemon = input('Ingrese apodo al pokemon incial: ')
os.system("pause")
print('las estadisticas de tu primer pokemon')
pokemon.datos_equipo_pokemon()
pokemo= pokemon.pokemon()
os.system("pause")
os.system("cls")
while True:
    winsound.PlaySound('Poke.wav',winsound.SND_ASYNC)
    print("Menu principal:") 
    print('\nAcciones:')
    print('1- Equipo Pokémon.')
    print('2- Batallas contra Pokémon salvajes:')
    print('3- Pokédex.:')
    print('4-  Tienda.')
    print('5- Salir.')
    
    opcion = int(input('Seleccione una acción: '))
    os.system("cls")
    if opcion == 1:
        winsound.PlaySound('equipo.wav',winsound.SND_ASYNC)
        pokemon.pokemon()
        os.system("pause")
    elif opcion ==2:
        winsound.PlaySound('batalla.wav',winsound.SND_ASYNC)
        print("tu rival es:")
      
        idr = random.randint(1,151)
        pokemonr = Pokemon(idr)
        pokemonr.pokemon()
        rc=pokemonr.rc
        psr=pokemonr.ps
        niv=pokemon.nivel
        nivr=pokemonr.nivel 
        nivr= random.randint(niv-5,niv+5)
        exp=pokemon.exp

        #estadisticas basicas
        ps=pokemon.ps
        res=pokemon.ps
        at=pokemon.at
        ats=pokemon.ats
        df=pokemon.df
        dfs=pokemon.dfs
        vel =pokemon.vel
        # valores iniciales 
        psi=random.randint(1,ps)
        ati=random.randint(1,at)
        atsi=random.randint(1,ats)
        dfi=random.randint(1,df)
        dfsi=random.randint(1,dfs)
        veli=random.randint(1,vel)
        #puntos de salud 
        psc = batalla.puntos_salud_comb(psi,ps,niv)
        # puntos de ataque
        atc=batalla.datos_combate(ati,at,niv)
        # puntos de defensa
        dfc=batalla.datos_combate(dfi,df,niv)
        # puntos de ataque especial
        atsc=batalla.datos_combate(atsi,ats,niv)
        # puntos de defensa especial
        dfsc=batalla.datos_combate(dfsi,dfs,niv)
        # puntos de velocidad
        velc=batalla.datos_combate(veli,vel,niv)
        #potencia
        pote=pokemon.p1
        #tipos 
        t=pokemon.tip
        tr=pokemonr.tip
        #efectividad
        e=batalla.efectividad(t,tr)
        if e == None :
            e=1
        #bonificacion
        movtt = pokemon.movt1
        mov = pokemon.mov1
        if mov == movtt:
            bo=1
        elif mov != movtt:
            bo=1
        #v ??
        v=random.randint(85,100)

        #ander
        #estadisticas basicas
        atr=pokemonr.at
        atsr=pokemonr.ats
        dfr=pokemonr.df
        dfsr=pokemonr.dfs
        velr=pokemonr.vel
        # valores iniciales 
        psir=random.randint(1,psr)
        atir=random.randint(1,atr)
        atsir=random.randint(1,atsr)
        dfir=random.randint(1,dfr)
        dfsir=random.randint(1,dfsr)
        velir=random.randint(1,velr)
        #puntos de salud 
        pscr = batalla.puntos_salud_comb(psir,psr,nivr)
        # puntos de ataque
        atcr=batalla.datos_combate(atir,atr,nivr)
        # puntos de defensa
        dfcr=batalla.datos_combate(dfi,df,nivr)
        # puntos de ataque especial
        atscr=batalla.datos_combate(atsi,ats,nivr)
        # puntos de defensa especial
        dfscr=batalla.datos_combate(dfsi,dfs,nivr)
        # puntos de velocidad
        velcr=batalla.datos_combate(veli,vel,nivr)
        #potencia
        poter=pokemonr.p1
        #tipos 
        t=pokemon.tip
        tr=pokemonr.tip
        #efectividad
        er=batalla.efectividad(tr,t)
        if er == None :
            er=1
        #bonificacion
        movttr = pokemon.movt1
        movr = pokemon.mov1
        if movr == movttr:
            bor=1
        elif movr != movttr:
            bor=1
        #v ??
        vr=random.randint(85,100)
        os.system(str(idr)+'.png')
        os.system("pause")
        os.system("cls")
        
        if vel>velr:
            t=1
        else:
            t=2        
        print("batalla pokemon:")
        while ps>0 and psr >0 :
            if t==1:
                print(pokemon.nombre, pokemon.nivel ,pokemon.puntos_sa, pokemon.ps)
                print( pokemonr.nombre, pokemonr.nivel ,pokemonr.puntos_sa, pokemonr.ps)
                os.system("pause")
                print("Que deseas hacer??")
                print("1. Atacar")
                print("2. Capturar al pokemon")
                print("3. Mochila ")
                print("4. huir")
                opcion =int(input("escoja una opcion: "))
                if opcion ==1 :
                    daño =batalla.ataque(niv,atc,pote,dfc,bo,e,v)
                    dinero = tienda.dinero(niv)
                    pokemonr.ps =pokemonr.ps - daño
                    experiencia = batalla.experiencia(niv,velr)
                    if pokemonr.ps <=0:
                        print("el pokemon enemigo se deblilito")
                        print(f"ganaste de experiencia: {experiencia}")
                        print(f"ganaste de dinero:")
                        print(f"El dinero total : {dinero} ")
                        pokemon.exp=pokemon.exp+experiencia
                        if pokemon.exp >= 100:
                            pokemon.nivel+=1
                            pokemon.exp-100
                        t=2
                        pokemon.ps=res
                        break
                elif opcion ==2:
                    p=0
                    s=0
                    u=0
                    m=0
                    r=batalla.captura(rc,psr,p,s,u,m)
                    if r==True:
                        t=2
                        break
                    else:
                        t=2
                        continue
                elif opcion ==3:
                    print(ps)
                    p = batalla.mochila(ps,ps)
                    pokemon.ps = p
                    t=2
                else :
                    r = batalla.huir(vel, velr)
                    if r ==False: 
                        print("no pudiste huir :c")
                    else :
                        break
            else: 
                dañor =batalla.ataque(nivr,atcr,poter,dfcr,bor,er,vr)
                pokemon.ps =pokemon.ps - dañor
                if pokemon.ps <=0:
                        print("tu pokemon se deblilito")
                        print('Ha sido demasiado rapido ,intenta de nuevo---')
                        pokemon.ps=res
                        break
                t=1
        os.system("pause")
    elif opcion ==3:
        winsound.PlaySound('pokedex.wav',winsound.SND_ASYNC)
        pokemonr.pokedex()#componer 
    elif opcion ==4:
        winsound.PlaySound('tienda.wav',winsound.SND_ASYNC)
        tienda.tienda() #lista 
    elif opcion ==5:
        break
