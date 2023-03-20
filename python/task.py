from datetime import datetime
import re
class Task:
    """Este es el docstring de la clase"""
    id_task = 0  
    def __init__(self, name: str, tag:str = "A", total_days: int = 0, s_date: str = None):
        """
        TODO - Definir si habrá un método para obtener los datos desde excel o se hace desde el main
        """
        try:
            self._id: int = Task.id_task
            Task.id_task += 1

            self._dict_status = dict()
            self._name = self.set_name(name)
            self._tag = tag #TODO : Revisar y crear método para aumentar periódicamente
            self._total_days = total_days
            self._s_date = s_date 
            self._f_date = s_date + self.total_days #TODO : Revisar que funcione
            self.validateName()
            self.validateTag()
            self.validateTDays()
            self.validateDates()
            self.validateStatus()

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
        return self._id


    def get_name(self) -> str:
        return self._name
    

    def set_name(self, name: str):
        """Cambia el nombre de la Tarea"""
        if name == self._name:
            raise ValueError("El nombre no ha cambiado")
        elif self.validateName(name) == False:
            self._dict_status["Nombre"] = False
        self._name = name
        return None


    def validateName(self, name):
        """Valida que el nombre de la tarea esté correcto"""
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
    

    def get_tag(self):
        return self._tag


    def set_tag(self, new_tag):
        pass


    def get_total_days(self) -> int:
        return self._total_days


    def set_total_days(self, total_days: int):
        self._total_days = total_days


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
        return f'\nID: {self.get_id()}\nNAME:{self.get_name()}\nTotal Days:{self.get_total_days()}\nStarter Day: {self.get_s_date()}'

    def valid_date(self, date: str):
        status: int
        if date is None:
            if self._id > 1:
                status = 2 #Ingrese una fecha
            else:
                status = 1 # Funciona
        else:
            try:
                datetime.strptime(date, '%Y-%m-%d')
                status = 1
            except ValueError:
                status = 0 #Ingrese fecha en formato correcto
        return status


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

    def validateTag(self):
        pass


    def validateTDays(self):
        pass


    def validateDates(self):
        pass


    def validateStatus(self):
        """Valida que todos los componentes de la tarea sean correctos"""
        # tmp = True
        # for status in self._dict_status.values():
        #     tmp = tmp and status
        tmp = all(self._dict_status.values()) #Hace lo mismo que el for
        self._status = tmp
        return None

    id = property(get_id)
    name = property(get_name, set_name)
    tag = property(get_tag, set_tag)
    total_days = property(get_total_days, set_total_days)
    s_date = property(get_s_date, set_s_date)
    f_date = property(get_f_date, set_f_date)
    status = property(get_status)
    attr_status = property(get_atrr_status)
