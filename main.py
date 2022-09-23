#Autor Marc Corominas
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Definició de classes
class UnitatFormativa:
    nom = None
    qualificacio = None
    hores = None

    def __init__(self, nom, hores):
        self.nom = nom
        self.hores = hores


class ModulProfessional:
    nom = None
    unitats_formatives = []

    def __init__(self, nom):
        self.nom = nom

    def afegirUnitatFormativa(self, unitat_formativa):
        self.unitats_formatives.append(unitat_formativa);

    def getQualificacio(self):
        suma_hores = 0
        suma_qualificacio = 0

        for uf in self.unitats_formatives:
            suma_hores += uf.hores
            suma_qualificacio += (uf.qualificacio * uf.hores)

        return suma_qualificacio / suma_hores


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari", 20)
uf2 = UnitatFormativa("UF2. Optimització del programari", 20)
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes", 26)

uf1.qualificacio = 8
uf2.qualificacio = 10
uf3.qualificacio = 4

mp5 = ModulProfessional("MP05. Entorns de desenvolupament")

mp5.afegirUnitatFormativa(uf1)
mp5.afegirUnitatFormativa(uf2)
mp5.afegirUnitatFormativa(uf3)

print(uf1.nom, ":", uf1.qualificacio)
print(uf2.nom, ":", uf2.qualificacio)
print(uf3.nom, ":", uf3.qualificacio)
print(mp5.nom, ":", mp5.getQualificacio())
