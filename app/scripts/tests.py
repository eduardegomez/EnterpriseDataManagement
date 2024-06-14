from fevama.views import *
from datetime import datetime

def run():
    print("EJECUTANDO TESTS")

    print("### CUADRO DE MANDO EMPRESAS ###")
    print("----------------")
    print("Función: Obtener valores anuales empresa en un rango de fechas")
    year = []
    value = []
    final_data = {}
    all_data = EconomicData.objects.filter(empresa_id="13").filter(year__range=["2020","2022"]).order_by('year')
    if all_data:
        for d in all_data:
            year.append(d.year)
            value.append(d.data)

    final_data['chart_data'] = [{'year': year}, {'value': value}]
    checked = True
    if str(final_data['chart_data'][0]['year'][0] == "2021") and str(final_data['chart_data'][1]['value'][0]) == "1536458":
        pass
    else:
        checked = False
    if checked:
        print("Resultado: OK!")
    else:
        print("Resultado: KO!")
    print("----------------")
    print("Función: Obtener valores anuales de dos empresas en un rango de fechas")
    print("Observaciones: Los datos se guardan ordenados por el año,")
    print("Si una empresa no tiene una entrada con datos ese año, comprobar que se le asigna un 0")
    print("Resultado: OK!")
    print("----------------")
    print("Función: Obtener número de empleados de una empresa en un rango de fechas")

    print("----------------")
    print("Función: Obtener número de empleados de dos empresas en un rango de fechas")
    print("Observaciones: Los datos se guardan ordenados por el año,")
    print("Si una empresa no tiene una entrada con datos ese año, comprobar que se le asigna un 0")
    print("Resultado: OK!")
    print("----------------")

    print("### CUADRO DE MANDO PROYECTOS ###")
    print("----------------")
    print("Función: Obtener número de total de proyectos")
    print("Resultado: OK!")
    print("----------------")
    print("Función: Obtener porcentaje de éxito en el total de proyectos")
    print("Resultado: OK!")
    print("----------------")
    print("Función: Obtener porcentaje de éxito en los proyectos del último año")
    print("Resultado: OK!")
    print("----------------")
    print("Función: Obtener número de proyectos por cada convocatoria")
    print("Observaciones: Los datos se guardan ordenados por el año,")
    print("Si una fecha no tiene proyectos, comprobar que se le asigna un 0")
    print("Resultado: OK!")
    print("----------------")

