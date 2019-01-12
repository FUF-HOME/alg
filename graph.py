class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connetTo = {}
    def addNeighbor(self,nbr,weigh=0):
        self.connetTo[nbr] = weigh
    