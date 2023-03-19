from task import Task
import re
class Project:
    """Objeto Proyecto, almacena las tareas que le competen con sus respectivos datos"""
    id_project: int = 0
    inicio = Task("Inicio", 0)

    def __init__(self, name, arr_task: list = [inicio], ):
        """Inicializa un Objeto Proyecto"""
        try:
            self._id = Project.id_project
            Project.id_project += 1

            self._dict_status = dict()

            self._name = name
            
            self._arr_task = arr_task

            if arr_task[0].get_name() != "Inicio":
                self._arr_task.insert(0, Project.inicio)
            
            self._quant_task = len(self._arr_task)
            self.validateName(self._name)
            self.validateTasks()
            self.validateStatus()


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
        if self.validateName(name) == False:
            self._dict_status["Nombre"] = False
        self._name = name


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
        
        return name_status


    def get_tasks(self):
        """Muestra la cantidad de tareas que tenga el proyecto"""
        return self._arr_task

    
    def set_task(self, task: Task):
        """Agrega una tarea al proyecto"""
        pass


    def remove_task(self, task: Task):
        """Elimina una tarea del proyecto"""
        pass


    def changeOrderTasks(self, task: Task, new_place: int):
        """Cambia el orden de las tareas"""
        pass


    def get_quant_tasks(self):
        """Devuelve la cantidad de tareas que tenga el proyecto"""
        return self._quant_task


    def get_status(self) -> bool:
        """Devuelve el estado (Correcto o Erróneo) de las tareas que tenga el Proyecto"""
        return self._status


    def validateTasks(self):
        """Método que valida que exista una tarea Inicio y una final
        TODO Hacer que valide tarea por tarea"""
        if self.get_quant_tasks() == 1:
            task_status = False
            self._dict_status["Tareas"] = task_status
        else:
            task_status = True
            self._dict_status["Tareas"] = task_status
        return 0
    

    def validateStatus(self):
        """Valida que todos los componentes del proyecto sean correctos"""
        # tmp = True
        # for status in self._dict_status.values():
        #     tmp = tmp and status
        tmp = all(self._dict_status.values()) #Hace lo mismo que el for
        self._status = tmp
        return 0


    def getCompStatus(self, component:str):
        """Devuelve el estado (Correcto o Incorrecto) de la componente del proyecto solicitada
        Opciones:
        - Nombre -> Devuelve el estado del Nombre dado
        - Tareas -> Devuelve el estado de la tarea especificada"""
        try:
            if component not in self._dict_status:
                raise ValueError("Ingrese el nombre correcto de una componente")
            else:
                return self._dict_status[component]
        except ValueError as e:
            print(e)


    def __str__(self):
        """Devuelve el Proyecto en formato String"""
        arr_tasks = []
        for task in self.get_tasks():
            arr_tasks.append(task.get_name()) #Por revisar si sólo se quiere el nombre al representar el objeto
        return f"ID Proyecto: {self.get_id()}\nNombre: {self.get_name()}\nCantidad de Tareas: {self.get_quant_tasks()} \nTareas: {arr_tasks}\nEstado del proyecto: {self.get_status()}"


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
    status = property(get_status)
    comp_status = property(getCompStatus)