class Task:
    tasks = 0  
    def __init__(self, name, s_date, total_days):
        """
        TODO - Buscar como hacer docstring en Python
        TODO - Completar el Objeto y revisar si es necesario un objeto "Proyecto"
        TODO - Manejar control de errores y getters + setters
        TODO - Definir si habrá un método para obtener los datos desde excel o se hace desde el main
            
        """
        try:
            Task.tasks += 1
            self._name = name
            self._id = Task.cant_tareas
            self._s_date = s_date
            self._total_days = total_days
            #self._f_date = total_days + total_days

        except ValueError as e:
            print(e)
    
    def show(self):
        return {"Nombre": self.nombre, "ID": self.id}
    
    def g_f_date(self):
        return self._f_date

    def set_f_date(self, f_date):
        self.set_f_date = f_date

    f_date = property(g_f_date)

    def get_dineroNecesario(self):
        return self._dineroNecesario

    dineroNecesario = property(get_dineroNecesario)

