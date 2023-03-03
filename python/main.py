from task import Task

def run():
    lavarTrastes = Task("Lavar Trastes de la Cocina", 21, "01-02-2023")
    # tareasUni = Task("Hacer tarea de Sistemas Empresariales", 1, "2023-02-01")
    lavarTrastes.s_date("2022-27-02")
    # examenUni = Task("Estudiar para examen ArqSoft", "2023-03-03", 2)
    datos =lavarTrastes.show()
    # datos2 = tareasUni.show()
    # datos3 = examenUni.show()
    print(datos)
    # print(datos2)
    # print(datos3)
    

if __name__ == "__main__":
    run()