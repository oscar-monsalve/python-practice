import pandas as pd


# --------------------------------------------------------------------------------

# inicio = int(input("Ingrese el año inicial: "))
# final = int(input("Ingrese el año final: "))
# ventas = {}
#
# for i in range(inicio, final+1):
#     ventas[i] = float(input(f"Ventas del año {str(i)}: "))
#
# ventas = pd.Series(ventas)
#
# print("Ventas\n", ventas)
#
# # calcular descuento de ventas
# print("Descuento\n", ventas*0.45)

# --------------------------------------------------------------------------------

# def notas_estudiantes(notas: float):
#     notas = pd.Series(notas)
#     estadisticas = pd.Series(
#         [notas.min(),
#          notas.max(),
#          notas.median(),
#          notas.std()],
#         index=["min", "max", "media", "desviación estandar"]
#     )
#     return estadisticas
#
#
# def notas_estudiantes2(notas):
#     notas = pd.Series(notas)
#     return notas.describe()
#
#
# def ganan_materia(notas):
#     notas = pd.Series(notas)
#     return notas[notas >= 3].sort_values(ascending=False)
#
#
# notas = {"Carlos": 3.4, "German": 2, "Lina": 3, "Luis": 5, "Manuel": 4.8}
# print(ganan_materia(notas))

# --------------------------------------------------------------------------------

# datos = {
#     "Mes": ["Enero", "Febrero", "Marzo"],
#     "Ventas": [300, 200, 50],
#     "Costos": [50, 20, 40],
# }
#
# cuentas = pd.DataFrame(datos)
#
#
# def balance(cuentas, meses):
#     cuentas["Balance"] = cuentas.Ventas - cuentas.Costos
#     return cuentas[cuentas.Mes.isin(meses)].Balance.sum()
#
#
# print(balance(cuentas, meses=["Enero", "Febrero"]))
# print(cuentas)

# --------------------------------------------------------------------------------
# Leer .csv


def resumen_notas(file):
    rn = pd.read_csv(file, sep=",", decimal=".", index_col=0)
    return pd.DataFrame(
        [rn.min(), rn.max()],
        index=["Máxima", "Mínima"]
    )


print(resumen_notas("notas.csv"))
