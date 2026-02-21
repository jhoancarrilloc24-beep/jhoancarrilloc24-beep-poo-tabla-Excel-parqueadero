import random

class parqueadero:
    def __init__(self,fecha_entrada,hora_entrada,hora_salida,estado):
        self.fecha_entrada = fecha_entrada
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.estado = estado
       
        puesto = ["A-01","B-05","C-12","A-03"]
        self.puesto = random.choice(puesto)
        
    def get_puesto(self):
        return self.puesto
    
    def set_nuevo_puesto(self,nuevo_puesto):
        self.puesto = nuevo_puesto 
        
    def get_puesto(self):
        return self.puesto
    
    def set_puesto_nuevo(self,nuevo_puesto):
        self.puesto = nuevo_puesto
        
    def get_fecha_entrada(self):
        return self.fecha_entrada
    
    def set_nueva_fecha_entrada(self,nueva_fecha_entrada):
        self.fecha_entrada = nueva_fecha_entrada
        
    def get_hora_entrada(self):
        return self.hora_entrada
    
    def set_nueva_hora_entrada(self,nueva_hora_entrada):
        self.hora_entrada = nueva_hora_entrada
        
    def get_hora_salida(self):
        return self.hora_salida
    
    def set_nueva_hora_salida(self,nueva_hora_salida):
        self.hora_salida = nueva_hora_salida
        
    def get_estado(self):
        return self.estado
    
    def set_nuevo_estado(self,nuevo_estado):
        self.estado = nuevo_estado
        
    def asignar_puesto(self, puestos_disponibles):
        if self.estado == "disponible":
            self.puesto = input("ingrese el numero del puesto que desea asignar:")
        else:
            print("el paqueadero esta ocupado no se puede signar un puesto")
        
        
    def mostrar_info(self):
        print()
        print("datos del parqueadero 🅿️")
        print(f"puesto 🚗: {self.puesto}")
        print(f"fecha de entrada: {self.fecha_entrada}")
        print(f"hora de entreda: {self.hora_entrada}")
        print(f"hora de salida: {self.hora_salida}")
        print(f"estado: {self.estado}")