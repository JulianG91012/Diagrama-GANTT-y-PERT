from task import Task
class Project:
    id_project = 0
    inicio = Task("Inicio", 0)
    def __init__(self, name, dict_task: dict = {1: inicio}, ):
        try:
            self._id = Project.id_project
            Project.id_project += 1

            self.set_name(name)
            self._dict_task = dict_task
            
            #if not (1 in self._dict_task) and not (self._dict_task[1] == self.inicio.name):
            if "1" in self._dict_task and self._dict_task["1"] != 'Inicio':
                i = 2
                while str(i) in self._dict_task:
                    # Si ya hay una tarea con el mismo número, incrementar el número y seguir buscando
                    i += 1
                    self._dict_task[str(i)] = self._dict_task["1"]  # Agregar una nueva tarea con el nuevo número
                    del self._dict_task["1"]  # Eliminar la tarea anterior con el número 1
                    self._dict_task["1"] = 'Inicio'  # Agregar la nueva tarea #1 con el nombre correcto
            elif '1' not in self._dict_task:
                # Si la tarea #1 no existe, agregarla con el nombre correcto
                self._dict_task["1"] = 'Inicio'

            self._quant_task = len(self._dict_task)


        except ValueError as e:
            print(f'Error: {e}')

    def get_id(self):
        """Muestra el ID relacionado con el proyecto"""
        return self.id


    def get_name():
        """Muestra el Nombre del proyecto"""
        pass


    def set_name(self, name):
        """Cambia el nombre del Proyecto"""
        pass


    def get_tasks(self):
        """Muestra la cantidad de tareas que tenga el proyecto"""
        return self._dict_task

    
    def set_task(self, task):
        """Agrega una tarea al proyecto"""
        pass


    def remove_task(self, task: Task):
        """Elimina una tarea del proyecto"""
        pass


    def changeOrderTasks(self, task: Task, new_place: int):
        pass


    def get_quant_tasks(self):
        return self._quant_task


    def get_status(self):
        pass


    def get_validated(self):
        pass
    
    def showProject(self):
        return f"ID Proyecto: {self.get_id}\n Nombre: {self.get_name}\n Cantidad de Tareas: {self} \n Tareas: #{self._dict_task.values}: {self._dict_task.keys}"

    id = property(get_id)
    name = property(get_name, set_name)
    tasks = property(get_tasks, set_task, remove_task)
    quant_task = property(get_quant_tasks)

