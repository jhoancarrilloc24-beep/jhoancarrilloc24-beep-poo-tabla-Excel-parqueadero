class Carro:
    def __init__(self,placa,marca,color):
        self.placa = placa
        self.marca = marca
        self.color = color
        
    def get_placa(self):
        return self.placa
    
    def set_placa_nueva(self,nueva_placa):
        self.placa = nueva_placa
        
    def get_marca(self):
        return self.marca
    
    def  set_marca_nueva(self,marca_nueva):
        self.marca = marca_nueva
        
    def get_color(self):
        return self.color
    
    def set_color_nuevo(self,color_nuevo):
        self.color = color_nuevo
        
    def mostrar_info(self):
        print()
        print("datos del carro 🚘")
        print(f"placa: {self.placa}")
        print(f"marca: {self.marca}")
        print(f"color: {self.color}")
        