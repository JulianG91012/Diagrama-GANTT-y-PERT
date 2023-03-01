class Task:
    tasks = 0  
    def __init__(self, name, s_date, total_days):
        try:
            Task.tasks += 1
            self._name = name
            self._id = Task.cant_tareas
            self._s_date = s_date
            self._total_days = total_days

        except ValueError as e:
            print(e)
    
    def show(self):
        return {"Nombre": self.nombre, "ID": self.id}