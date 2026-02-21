from usuario import Usuario
from carro import Carro
from parqueadero import parqueadero

oj_us = Usuario
oj_ca = Carro
oj_pa = parqueadero

obj_usuario = Usuario("1294832949","andy","cliente")
obj_usuario2 = Usuario("132498734","mike","cliente")
obj_carro = Carro("12ty53","toyota","rojo")
obj_carro2 = Carro("12df24","subaru","naranja")
obj_parqueadero = parqueadero("12/06/2024","10:00","18:12","exelente")
obj_parqueadero2 = parqueadero("12/06/2024","13:49","16:00","normal")

#tabla de datos
print("\nTABLA DE DATOS")
print("-"*160)
print("    ID       nombre    tipo de usuario     placa     marca     color     puesto     fecha de entrada     hora de entrada     hora de salida     estado")
print("-"*160)

#zona de filas de la tabla(datos)
print(f"{obj_usuario.ID}   {obj_usuario.nombre}         {obj_usuario.tipo_usuario}          {obj_carro.placa}    {obj_carro.marca}    {obj_carro.color}       {obj_parqueadero.get_puesto()}       {obj_parqueadero.get_fecha_entrada()}          {obj_parqueadero.get_hora_entrada()}               {obj_parqueadero.get_hora_salida()}              {obj_parqueadero.get_estado()}")
print(f"{obj_usuario2.ID}    {obj_usuario2.nombre}         {obj_usuario2.tipo_usuario}          {obj_carro2.placa}    {obj_carro2.marca}    {obj_carro2.color}    {obj_parqueadero2.get_puesto()}       {obj_parqueadero2.get_fecha_entrada()}          {obj_parqueadero2.get_hora_entrada()}               {obj_parqueadero2.get_hora_salida()}              {obj_parqueadero2.get_estado()}")