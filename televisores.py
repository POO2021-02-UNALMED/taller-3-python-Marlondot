class Marca:
    def __init__(self,nombre):
        self._nombre=nombre
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre=nombre

class TV:
    _numTV=0
    def __init__(self,_marca,_estado):
        self._marca=_marca
        self._estado=_estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self._control=None
        TV._numTV+=1

    #setting and getting marca
    def setMarca(self,_marca):
        self._marca=_marca

    def getMarca(self):
        return self._marca
    
    #Setting and getting canal
    def setCanal(self,_canal):
        if (_canal<=120 and _canal>0 and self._estado):
            self._canal=_canal
    
    def getCanal(self):
        return self._canal

    #Setting and getting volumen
    def setVolumen(self, _volumen):
        if (_volumen>-1 and _volumen<8 and self._estado):
            self._volumen=_volumen
    
    def getVolumen(self):
        return self._volumen

    #Setting and getting precio
    def setPrecio(self, _precio):
        self._precio=_precio

    def getPrecio(self):
        return self._precio
    
    #Setting and getting control
    def setControl(self, _control):
        self._control=_control
    
    def getControl(self):
        return self._control
    
    #Setting and getting numTv
    @classmethod
    def setNumTv(cls,_numTV):
        cls._numTV=_numTV
    
    @classmethod
    def getNumTv(cls):
        return cls._numTV
    
    #Turning on and off and getting Estado
    def turnOn(self):
        self._estado=True

    def turnOff(self):
        self._estado=False

    def getEstado(self):
        return self._estado

    #Canal down and up
    def canalUp(self):
        if (self._canal<120):
            self._canal+=1
    
    def canalDown(self):
        if (self._canal>1):
            self._canal-=1
    
    #volumen down and up
    def volumenUp(self):
        if (self._volumen<7):
            self._volumen+=1
    
    def volumenDown(self):
        if (self._volumen>0):
            self._volumen-=1

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
if __name__=="__main__":
    marca = Marca("Semsung")
    tv1 = TV(marca, True)
    tv1.setVolumen(5)
    tv1.volumenUp()
    tv2 = TV(marca, False)
    control = Control()
    control.enlazar(tv2)
    print(control.getTV()==tv2)
    control.turnOn()
    print(tv2.getEstado())
    control.volumenUp()
    print(tv2.getVolumen())
    tv3 = TV(marca, True)
    tv3.setVolumen(7)
    tv3.volumenUp()
    print(tv1.getVolumen() == 6)
    print(tv2.getVolumen() == 2)
    print(tv3.getVolumen() == 7)

    