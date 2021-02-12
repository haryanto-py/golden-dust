class Bus:

    __jumlah = 0

    def __init__(self, supir, trayek, kas, penumpang):
        self.supir = supir
        self.trayek = trayek
        self.kas = kas
        self.penumpang = penumpang
        Bus.__jumlah += 1
    
    def penumpangNaik(self, nama):
        self.penumpang.append(nama)
        return self.penumpang
    
    def penumpangTurun(self, nama, bayar):
        if len(self.penumpang) == 0:
            print("bus kosong!")
            return False

        for i in self.penumpang:
            if i == nama:
                self.penumpang.remove(nama)
                self.kas += bayar
                return self.penumpang
    
    @classmethod
    def getJumlah(cls):
        return cls.__jumlah

    @staticmethod
    def getJumlah2():
        return Bus.__jumlah

#bus1 = Bus("Haryanto", "Caringin - Sd. Serang", 0, [])
