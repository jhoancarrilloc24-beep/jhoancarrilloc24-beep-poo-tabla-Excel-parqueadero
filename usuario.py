class Usuario:
    def __init__(self,ID,nombre,tipo_usuario):
        self.ID = ID
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario
        
    def get_ID(self):
        return self.nombre
    
    def set_ID_nueva(self,nueva_ID):
        self.ID = nueva_ID
        
    def get_nombre(self):
        return self.nombre
    
    def set_nombre_nuevo(self,nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def get_tipo_usuario(self):
        return self.tipo_usuario
    
    def set_nuevo_tipo__usuario(self,nuevo_tipo_usuario):
        self.tipo_usuario = nuevo_tipo_usuario
        
    def mostrar_info(self):
        print()
        print(f"datos del usaurio 💻")
        print(f"ID: {self.ID}")
        print(f"nombre: {self.nombre}")
        print(f"tipo de usuario: {self.tipo_usuario}")
        
    