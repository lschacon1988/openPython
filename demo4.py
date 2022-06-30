import math

nombre='Luis'
apellido='Chacon'
edad=34
email='lschacon26@gmail.com'
casado=True
conHijos=True
amigos=['Julmary', 'Jhon']
peliculasVistas={
    'titulo': 'Sherk',
    'titulo':'iron man'
}


peso = float(input("Ingrese su peso en Kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

IMC = round(peso/math.pow(estatura, 2), 1)

print("Su IMC es de "+str(IMC))
