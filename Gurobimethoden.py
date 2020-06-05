from Deklaration import Deklaration
from Pre_Sampling import Pre_Sampling
class Gurobimethoden:
# ------------------- Konstruktor -------------------------------------------------------------------
    def __init__(self):
        Deklaration.__init__(self)
        Presampling.__init__(self)

    def Kilometerkosten(self):
        kombisVomPreSampling = self.Kombi6(self.Flights, self.Aircrafttypes, self.Airports)
        KilometerFlugKosten = [0 for i in range(len(kombisVomPreSampling))]
        for i in range(len(kombisVomPreSampling)):
            KilometerFlugKosten[i] = Flights[kombisVomPreSampling[i][1]][7] * Aircrafttypes[kombisVomPreSampling[i][3]][
            9]  # =dist_j* kmCost_t
        return KilometerFlugKosten


print(Kilometerkosten())


def VariablenListeFürGurobi(self):
    kombis = self.Kombi6(self.Flights, self.Aircrafttypes, self.Airports)
    Liste = []
    for i in range(len(kombis)):
        Liste.append((kombis[i][0], kombis[i][1], kombis[i][2], kombis[i][3]))
    return Liste


print(VariablenListeFürGurobi())

# You can also provide your own list of tuples as indices. For example, x = model.addVars([(3,'a'), (3,'b'), (7,'b'), (7,'c')])
# would be accessed in the same way as the previous example x[3,'a'], x[7,'c']

m = Model('test')

x = m.addVars(VariablenListeFürGurobi(),
              vtype=GRB.BINARY,
              obj=Kilometerkosten())

m.addConstrs(
    (x.sum(i, '*', '*', '*') <= 1 for i in self.Flights.keys()), 'Jeder Flug hat höchstens einen Nachfolger')

m.addConstrs(
    (x.sum('*', j, '*', '*') <= 1 for j in self.Flights.keys()), 'Jeder FLug hat höchstens einen Vorgänger')

for t in self.Aircrafttypes.keys():
    m.addConstrs(
        (x.sum(i, '*', '*', t) == x.sum('*', i, '*', t) for i in self.Flights.keys()), 'Flusserhaltung')

# Zielfunktion nimmt auch tatsächlich (sinvolle?) Werte an, falls diese Nebenbedingung einkommentiert wird muss der Constraint drüber auskommentiert werden
# m.addConstrs(
#  (x.sum('*', '*', '*', t) == 3  for t in self.Aircrafttypes.keys()))

m.write('Test.lp')
m.optimize()

# print(x)
# print(x.keys()[0])    #so kann man für die Nebenbedingungen auf unsere Indizes zugreifen
# print(x.keys()[i][0])


# Example usage:

# x = m.addVars([(1,2), (1,3), (2,3)])
# expr = x.sum()       # LinExpr: x[1,2] + x[1,3] + x[2,3]
# expr = x.sum(1, '*') # LinExpr: x[1,2] + x[1,3]
# expr = x.sum('*', 3) # LinExpr: x[1,3] + x[2,3]
# expr = x.sum(1, 3)   # LinExpr: x[1,3]