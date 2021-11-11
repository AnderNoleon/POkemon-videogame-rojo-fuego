class Pokedex:

    def __init__(self):
        self.nombre=""
        self.id=""
        self.poke_n=[]
        self.poke_i=[]

    def ingresar_n(self,nombre):
        self.poke_n.append(nombre)

    def ingresar_i(self,id):
        self.poke_i.append(id)
    
    def pokede(self):
        for k in self.poke_i :
            for l in self.poke_n :
                print(k,l)

    