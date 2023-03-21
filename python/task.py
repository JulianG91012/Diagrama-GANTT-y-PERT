from datetime import datetime
from datetime import timedelta
import re
class Task:
    """Este es el docstring de la clase"""
    _id_task = 0
    _current_tag = "A"
    def __init__(self, name: str, total_days: int = None, s_date: str = None):
        """
        TODO - Definir si habrá un método para obtener los datos desde excel o se hace desde el main
        TODO: Definir si es necesario un método "UpdateStatus" para actualizar el estado (Correcto o Falso) al actualizar un atributo
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
            self._f_date = None
            self.calculate_f_date()
            
            self.validateName(name)
            self.validateTag(self._tag)
            self.validateTDays(total_days)
            self.validateSDate(s_date)
            self.validateFDate(self._f_date)
            self.validateStatus()
            # print("Al crear el metodo:")
            # print(self.get_s_date())
            # print(self.get_f_date())
            # print()

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


    def set_total_days(self, new_total_days: int):
        """Asigna el valor especificado a la duración de la tarea"""
        if self._total_days == new_total_days:
            return "El valor del Tag no ha cambiado"
        self.validateTDays(new_total_days)
        self._total_days = new_total_days
        return None


    def validateTDays(self, total_days):
        t_days_msg = ""
        t_days_status:bool = False
        if not isinstance(total_days, int) and self.get_name() != "Inicio":
            t_days_msg = "La duración debe ser un número entero"
            self._dict_status["Duracion"] = t_days_status

        elif self.get_name() != "Inicio" and total_days <= 0:
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


    def set_s_date(self, new_s_date: str):
        if self._s_date == new_s_date:
            return "La fecha de inicio no ha cambiado"
        self.validateSDate(new_s_date)
        self._s_date = new_s_date
        return None


    def validateSDate(self, date):
        try:
            s_date_status: bool
            if date is None and self.get_name() != "Inicio":
                s_date_status = False
            elif date is None and self.get_name() == "Inicio":
                s_date_status = True
            elif date is not None:
                datetime.strptime(date, '%Y-%m-%d')
                s_date_status = True
            self._dict_status["Fecha Inicio"] = s_date_status
            self._s_date = date
            return None

        except ValueError:
            self._dict_status["Fecha Inicio"] = False


    def get_f_date(self):
        return self._f_date


    def set_f_date(self, new_f_date: str):
        if self.f_date and self.f_date == new_f_date:
            return "La fecha ingresada es la misma"
        self.validateFDate(new_f_date)
        self._f_date = new_f_date
        return None


    def calculate_f_date(self):
        """Calcula la fecha final a partir de la fecha inicial y la duración"""
        if self._s_date is not None and self._total_days is not None:
            s_date = datetime.strptime(self._s_date, '%Y-%m-%d')
            f_date = s_date + timedelta(days=self._total_days)
            # self.set_f_date(f_date.strftime('%Y-%m-%d'))
            self._f_date = f_date.strftime('%Y-%m-%d')
            # print("Al calcular el valor:")
            # print(f'Fecha inicio: {self.get_s_date()}')
            # print(self.get_f_date())
            # print()
        else:
            return None


    def validateFDate(self, date):
            try:
                s_date_status: bool
                if date is None and self.get_name() != "Inicio":
                    s_date_status = False
                #Validar caso de que la tarea sea "Inicio" y no tenga fecha inicial
                elif date is None and self.get_name() == "Inicio" and self.get_s_date() == None:
                    s_date_status = True
                elif date is not None:
                    datetime.strptime(date, '%Y-%m-%d')
                    s_date_status = True
                self._f_date = date
                self._dict_status["Fecha Final"] = s_date_status
                return None

            except ValueError:
                self._dict_status["Fecha Final"] = False


    def get_status(self):
        return self._status


    def get_atrr_status(self, attr:str):
        try:
            if attr not in self._dict_status and attr not in ["Nombre", "Duracion", "Fecha Inicio", "Fecha Final", "Status"]:
                raise ValueError("Ingrese el nombre correcto de un atributo")
            else:
                return self._dict_status[attr]
        except ValueError as e:
            print(e)


    def __str__(self) -> str:
        return f'\nID: {self.get_id()}\nNombre:{self.get_name()}\nDuracion:{self.get_total_days()}\nFecha Inicio: {self.get_s_date()}\nFecha Final: {self.get_f_date()} \nEstado de la tarea:{self.validateStatus()}'


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
