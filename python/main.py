from task import Task
from project import Project

def run():
    #inicio = Task("Inicio", 5, "2023-03-19")
    tomar_requisitos = Task("Toma de requisitos por medio de entrevista", 5, "2023-03-19")
    tomar_requerimientos_legales = Task("Tomar requerimientos definidos por la ley", 5, "2023-03-20")

    arqSoftware = Project("Tiendita de Barrio", [tomar_requisitos])
    gestionProyectos = Project("Plantillas Gubernamentales de Calidad", [tomar_requerimientos_legales])

    


if __name__ == "__main__":
    run()