from Deklaration import Deklaration

class Pre_Sampling:
# ------------------- Konstruktor -------------------------------------------------------------------
    def __init__(self):
        Deklaration.__init__(self)


# hier werden alle Kombis zugelassen, auch vorerst die, die örtlich, zeitlich gar nicht möglich sind

def Kombi1(self):
    kombinationen = []
    for i in self.Flights:
        for j in self.Flights:
            for t in self.Aircrafttypes:
                kombinationen.append([i, j, 0, t])
                kombinationen.append([i, j, 1, t])
    return len(kombinationen), kombinationen


# print(Kombi1())


# hier werden nur die Kombis zugelassen, bei denen der Ort passt, Zeit egal

def Kombi2(self):
    kombinationen = []
    for i in self.Flights:
        for j in self.Flights:
            for t in self.Aircrafttypes:
                if self.Flights[i][4] == self.Flights[j][3]:
                    kombinationen.append([i, j, 0, t])
                    kombinationen.append([i, j, 1, t])
    return len(kombinationen), kombinationen


# print(Kombi2())


# hier wird zusätzlich betrachtet ob der Abflugzeitpunkt des 2. Flugs nach der Ankunft des 1. FLugs ist

def Kombi3(self):
    kombinationen = []
    for i in self.Flights:
        for j in self.Flights:
            for t in self.Aircrafttypes:
                if self.Flights[i][4] == self.Flights[j][3]:
                    if self.Flights[i][6] <= self.Flights[j][5]:
                        kombinationen.append([i, j, 0, t])
                        kombinationen.append([i, j, 1, t])
    return len(kombinationen), kombinationen


# print(Kombi3())


# hier betrachtet man zusätzlich noch, dass das zeitlich auch mit den TA Zeiten klappt

def Kombi4(self):
    kombinationen = []
    for i in self.Flights:
        for j in self.Flights:
            for t in self.Aircrafttypes:
                if self.Flights[i][4] == self.Flights[j][3]:
                    multiplier = self.Airports[self.Flights[i][4]][3]
                    if self.Flights[i][6] + (self.Flights[i][13] + self.Flights[j][12]) * multiplier <= self.Flights[j][5]:
                        kombinationen.append([i, j, 0, t])
                        kombinationen.append([i, j, 1, t])
    return len(kombinationen), kombinationen


# print(Kombi4())


# hier wird zusätzlich geschaut ob zwischen den beiden Flügen eine Wartung ausgeführt werden kann r=1 oder nicht =0

def Kombi5(self):
    kombinationen = []
    for i in self.Flights:
        for j in self.Flights:
            for t in self.Aircrafttypes:
                if self.Flights[i][4] == self.Flights[j][3]:
                    multiplier = self.Airports[self.Flights[i][4]][3]
                    if self.Flights[i][6] + (self.Flights[i][13] + self.Flights[j][12]) * multiplier <= self.Flights[j][5]:
                        if self.Flights[i][6] + (self.Flights[i][13] + self.Flights[j][12]) * multiplier + self.Aircrafttypes[t][11] <= \
                                self.Flights[j][5] \
                                and self.Airports[self.Flights[i][4]][1] == "HUB LH":
                            kombinationen.append([i, j, 0, t])
                            kombinationen.append([i, j, 1, t])
                        else:
                            kombinationen.append([i, j, 0, t])
    return len(kombinationen), kombinationen


# print(Kombi5())


# hier wird zusätzlich überprüft ob die Range des Flugzeugs für die  Distanz des Fluges auch ausreicht

def Kombi6(self):
    kombinationen = []
    for i in self.Flights:
        for j in self.Flights:
            for t in self.Aircrafttypes:
                if self.Aircrafttypes[t][6] >= self.Flights[i][7] and self.Aircrafttypes[t][6] >= self.Flights[j][7]:  # hier ergänzt
                    if self.Flights[i][4] == self.Flights[j][3]:
                        multiplier = self.Airports[self.Flights[i][4]][3]
                        if self.Flights[i][6] + (self.Flights[i][13] + self.Flights[j][12]) * multiplier <= self.Flights[j][5]:
                            if self.Flights[i][6] + (self.Flights[i][13] + self.Flights[j][12]) * multiplier + self.Aircrafttypes[t][11] <= \
                                    self.Flights[j][5] \
                                    and self.Airports[self.Flights[i][4]][1] == "HUB LH":
                                kombinationen.append([i, j, 0, t])
                                kombinationen.append([i, j, 1, t])
                            else:
                                kombinationen.append([i, j, 0, t])
    return kombinationen  # len(kombinationen)


print(Kombi6())
