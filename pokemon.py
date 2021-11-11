import random
import time 
import json 
import requests
import os
from batalla import Batalla
from pokedex import Pokedex
podex=Pokedex()
class Pokemon:
    def __init__(self,id):
        self.nombre = ""
        self.id=id
        self.exp=0
        self.apodo_pokemon =""
        self.nivel= 0
        self.puntos_sa = 0
        self.poke=""
        self.batalla=""
        self.pokede=[]
        self.df=0
        self.at=0
        self.ats=0
        self.dfs=0
        self.vel=0
        self.ps=0
        self.rc=0
        self.p1=0
        self.p2=0
        self.tip=""
        self.mov1=""
        self.mov2=""
        self.movt1=""
        self.movt2=""   
    def pokemon (self):
        self.nivel = 5
        aleatorio1 = random.randint(1,20)
        aleatorio2 = random.randint(1,20)
        pokemon_movimientos1 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio1}/").json()
        pokemon_movimientos2 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio2}/").json()
        poke= requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.id}').json()
        self.poke=requests.get(poke ['species']['url']).json()
        print(f"No. {poke['id']}- {self.poke['names'][6]['name']} ")
        print(f"apodo - {self.apodo_pokemon}  nivel es: {self.nivel} " )
        self.exp =poke['base_experience']
        print(f"exp actual {self.exp}")
        for i in poke['types']:
            tipos=requests.get(i['type']['url']).json()
            print(f"- {tipos['names'][4]['name']}")
        self.tip=tipos['names'][4]['name']
        print(f"Movimientos {pokemon_movimientos1['names'][5]['name']}")
        self.mov1=pokemon_movimientos1['names'][5]['name']
        self.p1=pokemon_movimientos1['power']
        self.movt1=pokemon_movimientos1['type']
        print(f"Movimientos {pokemon_movimientos2['names'][5]['name']}")
        self.p2=pokemon_movimientos2['power']
        self.movt2=pokemon_movimientos2['type']
        self.mov2=pokemon_movimientos2['names'][5]['name']
        print("Puntos de combate:")
        for item in poke['stats']:
            puntos=requests.get(item['stat']['url']).json()
            print(f"{puntos['names'][4]['name']}: {item['base_stat']}")
        puntos=requests.get(poke['stats'][0]['stat']['url']).json()
        self.puntos_sa=f"{puntos['names'][4]['name']}"
        self.ps=poke['stats'][0]['base_stat']
        self.at=poke['stats'][1]['base_stat']
        self.df=poke['stats'][2]['base_stat']
        self.ats=poke['stats'][4]['base_stat']
        self.dfs=poke['stats'][5]['base_stat']
        self.vel=poke['stats'][5]['base_stat']
        self.nombre=f"{self.poke['names'][6]['name']}"
        podex.ingresar_n(self.nombre)
        podex.ingresar_i(self.id)
        r=requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.id}").json()
        self.rc=r["capture_rate"]
    def datos_equipo_pokemon(self):
        if self.id == 1:
            #nombre_inicial = 'Bulbasur'
            self.id=1
            os.system(str(self.id)+'.png')
        elif self.id ==2:
            #nombre_inicial = 'Charmander'
            self.id=4
            os.system(str(self.id)+'.png')
        elif self.id==3:
            #nombre_inicial = 'Squirtle'
            self.id=7
            os.system(str(self.id)+'.png')
        else:
            print('Error al eligir pokemon inicial')
    def pokedex(self):
        podex.pokede() 
  