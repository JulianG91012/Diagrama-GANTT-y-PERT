from task import Task
import re
class Project:
    """Clase que representa a un proyecto con sus respectivas tareas y datos.
    
    Atributos:
        id_project (int): Identificador único del proyecto.
        inicio (task): Tarea de inicio de un proyecto, es el valor por defecto en caso de no incluirse ninguna.
    """
    id_project: int = 0
    inicio = Task("Inicio", 0)

    def __init__(self, name, arr_task: list = [inicio], ):
        """Inicializa un Objeto Proyecto
        """
        try:
            self._id = Project.id_project
            Project.id_project += 1

            self._dict_status = dict()
            self._name = name
            self._arr_task = arr_task

            if arr_task[0].get_name() != "Inicio":
                self._arr_task.insert(0, Project.inicio)
            
            self._quant_task = len(self._arr_task)
            
            self._updateStatus()


        except ValueError as e:
            print(f'Error: {e}')


    def get_id(self):
        """Muestra el ID relacionado con el proyecto"""
        return self._id


    def get_name(self):
        """Muestra el Nombre del proyecto"""
        return self._name


    def set_name(self, name):
        """Cambia el nombre del Proyecto"""
        if name == self._name:
            return "El nombre no ha cambiado"
        self.validateName(name)
        # elif self.validateName(name) == False:
            # self._dict_status["Nombre"] = False
        self._name = name
        self._updateStatus("Name")
        return None


    def validateName(self, name):
        """Valida que el nombre del proyecto esté correcto"""
        min_length = 2
        max_length = 40
        regex_pattern =  "^[a-zA-Z0-9 ]+$"
        name_status: bool
        regex = re.compile(regex_pattern)
        if (len(name) < min_length) or (len(name) > max_length) or not regex.match(name):
            name_status = False
            self._dict_status["Nombre"] = name_status
        else:
            name_status = True
            self._dict_status["Nombre"] = name_status 
        
        return None


    def get_tasks(self):
        """Muestra la cantidad de tareas que tenga el proyecto"""
        dic_tasks = dict()
        for task in self._arr_task:
            dic_tasks[task.get_name()] = {"ID": task.get_id(), "Tag": task.get_tag() ,"Duración": task.get_total_days(), "Fecha Inicio": task.get_s_date(), "Fecha Final" : task.get_f_date()}
        return dic_tasks


    def set_task(self, task: Task, order:int = None):
        """Agrega una tarea al proyecto
        TODO - Validar el status de la tarea, en caso de ser erróneo especificarlo en el dict_status y en el estado de la tarea específica"""
        if task.get_status() == False:
            self._dict_status["Tareas"][task.name] = False
            self._arr_task.append(task)
        elif order is not None and task.get_status() == True:
            self._arr_task.insert(order, task)
        else:
            self._arr_task.append(task)

        self._updateStatus("Tasks")
        return None


    def remove_task(self, task: Task):
        """Elimina una tarea del proyecto"""
        pass


    def changeOrderTasks(self, task: Task, new_place: int):
        """Cambia el orden de las tareas"""
        pass


    def get_quant_tasks(self):
        """Devuelve la cantidad de tareas que tenga el proyecto"""
        return self._quant_task


    def get_status(self) -> bool: #TODO: Verificar que si sea necesario
        """Devuelve el estado (Correcto o Erróneo) de las tareas que tenga el Proyecto"""
        return self._status


    def validateTasks(self):
        """Método que valida que exista una tarea Inicio y una final"""
        task_status:bool
        self._dict_status["Tareas"] = {}
        dict_tmp = {}
        #Caso de que hay una o menos tareas en el Proyecto
        if self.get_quant_tasks() <= 1:
            task_status = False
            self._dict_status["Tareas"] = task_status
            return "Solo hay una tarea en el proyecto"
        #En caso de que haya más de una, empiezo a recorrer cada tarea
        else:
            for task in self._arr_task:
                #Si hay más de una tarea, se valida el estado una por una
                if task.status == False:
                    task_status = False
                    dict_tmp.update({task.name:task_status})
                else:
                    task_status = True
                    dict_tmp.update({task.name:task.status})
            self._dict_status["Tareas"] |= dict_tmp
        return None


    def validateStatus(self):
        """Valida que todos los componentes del proyecto sean correctos"""
        tmp = all(self._dict_status.values()) # Valida todos los elementos del dict
        for task in self._arr_task:
            # Si una tarea no está completa, entonces todo el proyecto está incompleto
            if not task.status:
                tmp = False
                break
        self._status = tmp
        return None


    def getCompStatus(self, component: str) -> dict:
        """Devuelve el estado (Correcto o Incorrecto) de la componente del proyecto solicitada
        Opciones:
        - Nombre -> Devuelve el estado del Nombre dado
        - Tareas -> Devuelve el estado de todas las tareas
        TODO: Añadir funcion de escribir el nombre de una tarea y devolver solo el estado de esta
        TODO: Si no se ingresa una componente -> Mostrar el estado de todas"""
        try:
            if component not in self._dict_status and component != "Tareas":
                raise ValueError("Ingrese el nombre correcto de una componente")
            else:
                if component == "Tareas":
                    tasks = {}
                    for task in self._arr_task:
                        tasks[task.get_name()] = task.status
                    return tasks
                elif component in [task.get_name() for task in self._arr_task]:
                    for task in self._arr_task:
                        if task.get_name() == component:
                            return task.status
                else:
                    return self._dict_status[component]
        except ValueError as e:
            print(e)


    def _updateStatus(self, comp:str = None):
        if comp == "Name":
            self.validateName(self.get_name())
        elif comp == "Tasks":
            self.validateTasks()
        elif comp == None:
            self.validateName(self.get_name())
            self.validateTasks()
        self.validateStatus()
        return None


    def __str__(self):
        """Devuelve el Proyecto en formato String"""
        return f"ID Proyecto: {self.get_id()}\nNombre: {self.get_name()}\nCantidad de Tareas: {self.get_quant_tasks()} \nTareas: {self.get_tasks()}\nEstado del proyecto: {self.get_status()}"


    def graphGantt(self):
        """Realiza una Gráfica de Gantt sobre los datos que se tengan del proyecto"""
        pass


    def graphPert(self):
        """Realiza una gráfica de Pert sobre los datos que se tengan del proyecto"""
        pass



    id = property(get_id)
    name = property(get_name, set_name)
    tasks = property(get_tasks, set_task, remove_task)
    quant_task = property(get_quant_tasks)
    status = property(get_status) #TODO : verificar que esto si haga algo
    comp_status = property(getCompStatus)