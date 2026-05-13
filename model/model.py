import networkx as nx

from UI import view
from database.DAO import DAO


class Model:

    def __init__(self):

        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMap = {}
        for n in self._nodes:
            self._idMap[n.CCode] = n

        self._soluzioni = []

    def buildGraph(self, anno):
        self._nodes = DAO.getAllNodesAnno(anno)
        self._graph.add_nodes_from(self._nodes)
        self.addEdges(anno)

    def addEdges(self, anno):
        allEdges = DAO.getAllEdges(anno, self._idMap)
        for e in allEdges:
            self._graph.add_edge(e.u, e.v)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getConnesso(self):
        numero = nx.number_connected_components(self._graph)
        return numero

    def getGrado(self):
        risultato = []
        for n in self._nodes:
            risultato.append((n.StateNme,self._graph.degree(n)))
        return risultato

    def getTree(self, source):
        dfsTree = nx.dfs_tree(self._graph, source)
        return dfsTree.nodes()

    def dfs_recursive(self,node,visited):
        visited.add(node)

        for neighbor in self._graph.neighbors(node):
            if neighbor not in visited:
                self.dfs_recursive(neighbor,visited)

        return visited

