from task import Task
from project import Project

def run():
    lavarTrastes = Task("Lavar Trastes de la Cocina", 21, "2023-02-01")
    dict_task = dict({"1": "Inicio"})
    plantillaPagWeb = Project("Plantilla de Páginas Web para el gobierno", dict_task)
    print(plantillaPagWeb.showProject())
    # tareasUni = Task("Hacer tarea de Sistemas Empresariales", 1)
    # #print(lavarTrastes.s_date)
    # # examenUni = Task("Estudiar para examen ArqSoft", "2023-03-03", 2)
    # datos =lavarTrastes.show()
    # datos2 = tareasUni.show()
    # # datos3 = examenUni.show()
    # print(datos)
    # print(datos2)
    # # print(datos3)
    

if __name__ == "__main__":
    run()