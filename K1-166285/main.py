from car import Car
from vehicle import Vehicle

v_1 = Vehicle()
print(v_1)
v_2 = Vehicle('12345', 125, 1990)
print(v_2)
print(v_1.model)
v_1.prod_year = 1990
print(v_1)
c_1 = Car()
print(c_1)
c_2 = Car(20000, 'czerwony', 3, 'XYZ12345', 3, 2019)
print(c_2)
print(c_1 == c_2)
