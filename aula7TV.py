class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def canalAumenta(self):
        if self.ligada:
            self.canal += 1
            if self.canal > 25:
                self.canal = 1
        else:
            self.ligada = True
    def canalDiminui(self):
        if self.ligada:
            self.canal -= 1
            if self.canal < 1:
                self.canal = 25
        else:
            self.ligada

if __name__ == '__main__':
    tv = Televisao()

    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)

    for x in range(50):
        tv.canalAumenta()
        print(tv.canal)
    for x in range(50):
        tv.canalDiminui()
        print(tv.canal)