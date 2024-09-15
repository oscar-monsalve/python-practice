# 1. DONE (02_classes.py) Crear un archivo de texto donde se almacenen los datos de t,x,y con cada simulación realizada.

# 2. (04_files.py):
# Crear un programa que:
# - Abra el archivo ideam.txt
# - Requiera una fecha al usuario entre el 27 de abril y el 3 de mayo
# - Despliegue en terminal la temperatura máxima alcanzada
# - Registre el número de consultas realizadas a el archivo escribiendo una línea final que diga “Este documento ha sido consultado XX veces”
# - Sacar excepción cuando la temperatura sea mayor a 27.6 grados.

class UserWarning(Exception):
    def __init__(self, mensaje: str):
        self.mensaje = mensaje


valid_dates = [27, 28, 29, 30, 1, 2, 3]
date = int(input("Enter a date from april 27 to may 3 find the maximum temperature: "))

if date not in valid_dates:
    raise UserWarning("The provided date is not between april 27 and may 3. Enter a valid date.\n")

dates_temp = dict()
open_count = 0

with open("reto2_ideam.txt", "r+") as file:
    open_count += 1

    for i in file:

        if i.find("2023") == -1:
            continue
        else:
            year_index = i.find("2023")
            temp_index = i.find("00,2")

            date_str = i[year_index:year_index+10]
            days_int = int(date_str[-2:])

            temp_str = i[temp_index:temp_index+7].split(",")
            temp_int = float(temp_str[1])

            dates_temp[days_int] = dates_temp.get(days_int, temp_int)

    temp_on_day = dates_temp.get(date)
    print(f"The maximum temperature on the {date}th is: {temp_on_day}°C\n")
    if temp_on_day > 27.6:
        raise UserWarning("The temperature on this day is greater than 27.6 °C")

    file.write(f"The file has been used {open_count} times\n")
