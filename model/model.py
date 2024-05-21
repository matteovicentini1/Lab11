import copy

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.nodi = []
        self.grafo= nx.Graph()
        self.idmap={}
        self.percorsofinale=[]
        self.lunghezzaarchi=0
        self.peso=0


    def creagrafo(self,colore):
        self.nodi = DAO.getnodi(colore)
        self.grafo.add_nodes_from(self.nodi)
        for i in self.nodi:
            self.idmap[i.Product_number]=i

    def creaconnessioni(self,anno,colore):
        archi = DAO.getarchi(anno,colore)
        for x,y,z in archi:
            if self.grafo.has_edge(x,y):
                continue
            else:
                self.grafo.add_edge(self.idmap[x],self.idmap[y],weight=z)

    def numnodi(self):
        return len(self.grafo.nodes)

    def numarchi(self):
        return len(self.grafo.edges)

    def tremaggiori(self):
        l = []
        for u,v in self.grafo.edges:
            l.append((u,v,self.grafo[u][v]['weight']))
        fine = sorted(l,key=lambda x:x[2],reverse=True)
        return fine[:3]

    def percorso(self,id):
        self.lunghezzaarchi = 0
        self.peso = 0
        self.percorsofinale=[]
        nodo =self.idmap[id]
        self.ricorsione(nodo,[nodo])
        return self.percorsofinale,self.lunghezzaarchi



    def ricorsione(self,n,parziale):
        if len(parziale) == lun:
            if self.lunghezzaarchi<len(parziale):
                self.lunghezzaarchi=len(parziale)
                self.percorsofinale = copy.deepcopy((parziale))
            return
        for v in self.grafo.neighbors(parziale[-1]):
            if v not in parziale:
                parziale.append(v)
                self.ricorsione(parziale, lun)
                parziale.pop()