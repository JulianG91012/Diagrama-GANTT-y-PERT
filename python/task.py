from datetime import datetime
import re
class Task:
    """Este es el docstring de la clase"""
    _id_task = 0
    _current_tag = "A"
    def __init__(self, name: str, total_days: int = None, s_date: str = None):
        """
        TODO - Definir si habrá un método para obtener los datos desde excel o se hace desde el main
        """
        try:
            self._id: int = Task._id_task
            Task._id_task += 1

            self._dict_status = dict()
            self._name = name
            # _used_tags = {}
            self._tag = Task._current_tag
            Task._current_tag = chr(ord(Task._current_tag) + 1)

            self._total_days = total_days
            self._s_date = s_date 
            # self._f_date = s_date + self.total_days #TODO : Revisar que funcione
            self._f_date = None
            
            self.validateStatus()
            self.validateName(name)
            self.validateTag(self._tag)
            self.validateTDays(total_days)
            
            # status_date = self.valid_date(self, s_date)
            # if status_date == 1:
            #     self._valid = True
            # else:
            #     self._s_date = "undefined"
            #     self._valid = False
            #self.asign_date(self, s_date, status_date)
            

            #self._f_date = total_days + total_days

        except ValueError as e:
            print(f'Error: {e}')

    
    def get_id(self) -> int:
        """Retorna el ID asignado a la tarea"""
        return self._id


    def get_name(self) -> str:
        """Retorna el nombre de la tarea"""
        return self._name
    

    def set_name(self, name: str):
        """Cambia el nombre de la Tarea"""
        if name == self._name:
            return "El nombre no ha cambiado"
        # elif self.validateName(name) == False:
        #     self._dict_status["Nombre"] = False
        self.validateName(name)
        self._name = name
        return None


    def validateName(self, name):
        """Valida que el nombre de la tarea esté correcto"""
        min_length = 2
        max_length = 50 #TODO: Revisar la cantidad limite permitida y si es necesario un atributo "Descripción"
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
    

    def get_tag(self):
        """Retorna el Tag que tiene la tarea"""
        return self._tag


    def set_tag(self, new_tag):
        """Le agrega el Tag especificado a la tarea"""
        if self._tag == new_tag:
            return "El valor del Tag no ha cambiado"
        self.validateTag(new_tag)
        self._tag = new_tag
        return None


    def validateTag(self, tag):
        """Valida que el Tag que tenga la tarea sea correcto, agrega este valor al estado general de la tarea"""
        tag_status: bool
        if len(tag) != 1 or not tag.isalpha() or not tag.isupper():
            tag_status = False
            self._dict_status["Tag"] = tag_status
            #raise ValueError("El tag debe ser una letra mayúscula de la A a la Z")
        else:
            tag_status = True
            self._dict_status["Tag"] = tag_status
        return None


    def get_total_days(self) -> int:
        """Retorna la duración estimada de la tarea"""
        return self._total_days


    def set_total_days(self, total_days: int):
        """Asigna el valor especificado a la duración de la tarea"""
        if self._total_days == total_days:
            return "El valor del Tag no ha cambiado"
        self.validateTDays(total_days)
        self._total_days = total_days
        return None


    def validateTDays(self, total_days):
        t_days_msg = ""
        t_days_status:bool = False
        if not isinstance(total_days, int) and self.get_name() != "Inicio":
            t_days_msg = "La duración debe ser un número entero"
            self._dict_status["Duracion"] = t_days_status

        elif self.get_name() != "Inicio" and total_days < 0:
            t_days_msg = "La duración no puede ser cero"
            self._dict_status["Duracion"] = t_days_status

        else:
            t_days_status = True
            self._dict_status["Duracion"] = t_days_status
            t_days_msg = None
        # self._total_days = total_days
        return t_days_msg


    def get_s_date(self) -> str:
        return self._s_date


    def set_s_date(self, s_date: str):
        status = Task.valid_date(self, s_date) 
        Task.asign_date(self, s_date, status)


    def get_f_date(self):
        return self._f_date


    def set_f_date(self):
        pass


    def get_status(self):
        pass


    def get_atrr_status(self, attr:str):
        pass


    # def show(self) -> dict[str]:
    #     """Función que muestra la información de la tarea en cuestión"""
    #     try:
    #         if hasattr(self, "_name") == False:
    #             raise ValueError('La tarea no tiene Nombre asignado')
    #         elif hasattr(self, "_id") == False:
    #             raise ValueError(f' Interno, La tarea {self._name} no tiene ID asignado')
    #         elif hasattr(self, "_s_date") == False:
    #             raise ValueError(f'La tarea {self.name} no tiene Fecha asignada, por favor asignele una')    
    #         datos = { "Nombre": self._name, "ID": self._id, "Fecha Inicial": self._s_date, "Es Valido": self._valid}
    #         return datos
            
    #     except ValueError as e:
    #         print(f'Error: {e}')

    def __str__(self) -> str:
        return f'\nID: {self.get_id()}\nNombre:{self.get_name()}\nDuracion:{self.get_total_days()}\nDia de inicio: {self.get_s_date()}\nDia fin:{self.get_f_date()}\nEstado de la tarea:{self.validateStatus()}'

    # def valid_date(self, date: str):
    #     status: int
    #     if date is None:
    #         if self._id > 1:
    #             status = 2 #Ingrese una fecha
    #         else:
    #             status = 1 # Funciona
    #     else:
    #         try:
    #             datetime.strptime(date, '%Y-%m-%d')
    #             status = 1
    #         except ValueError:
    #             status = 0 #Ingrese fecha en formato correcto
    #     return status


    # def asign_date(self, s_date: str, status_date: int):
    #     try:
            
    #         if status_date == 1:
    #             self._s_date = s_date
    #         elif status_date == 2:
    #             raise ValueError("Ingrese una fecha")
    #         elif status_date == 0:
    #             raise ValueError("Ingrese una fecha en el formato correcto (YYYY-MM-DD)")
    #     except ValueError as e:
    #         print(f'Error: {e}, Status: {status_date} ')



    def validateDates(self):
        pass


    def validateStatus(self):
        """Valida que todos los componentes de la tarea sean correctos"""
        # tmp = True
        # for status in self._dict_status.values():
        #     tmp = tmp and status
        tmp = all(self._dict_status.values()) #Hace lo mismo que el for
        self._status = tmp
        return self._status

    id = property(get_id)
    name = property(get_name, set_name)
    tag = property(get_tag, set_tag)
    total_days = property(get_total_days, set_total_days)
    s_date = property(get_s_date, set_s_date)
    f_date = property(get_f_date, set_f_date)
    status = property(get_status)
    attr_status = property(get_atrr_status)
