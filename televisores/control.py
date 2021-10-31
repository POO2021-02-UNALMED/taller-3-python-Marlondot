
class Control:
    
    def __init__(self):
        self._tv=None
    
    #turn methods from TV
    def turnOn(self):
        self._tv.turnOn

    def turnOff(self):
        self._tv.turnOff
    
    #Canal methods from TV
    def setCanal(self):
        self._tv.setCanal
    
    def canalUp(self):
        self._tv.canalUp

    def canalDown(self):
        self._tv.canalDown
    
    #Volumen methods from TV
    def volumenUp(self):
        self._tv.volumenUp
    
    def volumenDown(self):
        self._tv.volumenDown
    
    #Linking control with TV
    def enlazar(self, _tv):
        self._tv=_tv
        _tv.setControl(self)

    #Getting TV (although the problem ask for a method "setTv" it's not neccesary because of the "enlazar" method)
    def getTV(self):
        return self._tv