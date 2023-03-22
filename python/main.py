from task import Task
from project import Project

def run():
    # inicio = Task("Inicio", 10, "2023-10-20")
    tomar_requisitos = Task("Toma de requisitos por medio de entrevista", 10, "2023-03-19")
    tomar_requerimientos_legales = Task("Tomar requerimientos definidos por la ley", 5, "2023-03-20")
    maquetacion = Task("Maquetar Frontend", 15, "2023-10-25")
    arqSoftware = Project("Tiendita de Barrio", [tomar_requisitos, tomar_requerimientos_legales, maquetacion])
    # gestionProyectos = Project("Plantillas Gubernamentales de Calidad", [tomar_requerimientos_legales, maquetacion])

    print(arqSoftware)

if __name__ == "__main__":
    run()