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