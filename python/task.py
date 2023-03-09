from datetime import datetime
class Task:
    """Este es el docstring de la clase"""
    tasks = 0  
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


    def asign_date(self, s_date: str, status_date: int):
        try:
            
            if status_date == 1:
                self._s_date = s_date
            elif status_date == 2:
                raise ValueError("Ingrese una fecha")
            elif status_date == 0:
                raise ValueError("Ingrese una fecha en el formato correcto (YYYY-MM-DD)")
        except ValueError as e:
            print(f'Error: {e}, Status: {status_date} ')


    def __init__(self, name: str, total_days: int, s_date: str = None):
        """
        TODO - Completar el Objeto y revisar si es necesario un objeto "Proyecto"
        TODO - Manejar control de errores y getters + setters
        TODO - Definir si habrá un método para obtener los datos desde excel o se hace desde el main
        """
        try:
            Task.tasks += 1
            self._name = name
            self._id: int = Task.tasks
            self._total_days = total_days
            #self._s_date = s_date
            status_date = Task.valid_date(self, s_date)
            if status_date == 1:
                self._valid = True
            else:
                self._s_date = "undefined"
                self._valid = False
            Task.asign_date(self, s_date, status_date)
            

            #self._f_date = total_days + total_days

        except ValueError as e:
            print(f'Error: {e}')

    

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str):
        self._name = name

    
    def get_f_date(self):
        return self._f_date
    

    def get_id(self) -> int:
        return self._id
    

    def get_total_days(self) -> int:
        return self._total_days
    
    def set_total_days(self, total_days: int):
        self._total_days = total_days


    def get_s_date(self) -> str:
        return self._s_date

    def set_s_date(self, s_date: str):
        status = Task.valid_date(self, s_date) 
        Task.asign_date(self, s_date, status)

    def show(self) -> dict[str]:
        """Función que muestra la información de la tarea en cuestión"""
        try:
            if hasattr(self, "_name") == False:
                raise ValueError('La tarea no tiene Nombre asignado')
            elif hasattr(self, "_id") == False:
                raise ValueError(f' Interno, La tarea {self._name} no tiene ID asignado')
            elif hasattr(self, "_s_date") == False:
                raise ValueError(f'La tarea {self.name} no tiene Fecha asignada, por favor asignele una')    
            datos = { "Nombre": self._name, "ID": self._id, "Fecha Inicial": self._s_date, "Es Valido": self._valid}
            return datos
            
        except ValueError as e:
            print(f'Error: {e}')






    s_date = property(get_s_date, set_s_date)
    f_date = property(get_f_date)
    name = property(get_name, set_name)
    id = property(get_id)
    total_days = property(get_total_days, set_total_days)
