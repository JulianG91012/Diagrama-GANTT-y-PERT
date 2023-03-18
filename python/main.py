from task import Task
from project import Project

def run():
    tomar_requisitos = Task("Toma de requisitos por medio de entrevista", 5, "2023-03-19")


    arqSoftware = Project("Tiendita de Barrio", [tomar_requisitos])
    gestionProyectos = Project("Plantillas Gubernamentales de Calidad")

    print(arqSoftware)
    print(tomar_requisitos.get_total_days())


if __name__ == "__main__":
    run()