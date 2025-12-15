class Vehicule:
    def move(self):
        return "Le véhicule se déplace"

class Voiture(Vehicule):
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def accelerer(self):
        print(f"{self.marque} {self.modele} accélère.")

mercedes = Voiture("Mercedes", "Classe A")
print(mercedes.move())
mercedes.accelerer()
# ...existing code...