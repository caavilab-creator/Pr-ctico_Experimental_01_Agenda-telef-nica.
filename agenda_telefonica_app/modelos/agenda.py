class Agenda:
    """
    Clase que representa la agenda telefónica
    Usa un vector (lista) como estructura de datos principal
    """
    def __init__(self):
        self.contactos = []  # Estructura 1: Vector/Lista
        self.capacidad = 100  # Capacidad máxima
        self.contador = 0  # Contador de contactos
    
    def get_contactos(self):
        return self.contactos
    
    def get_contador(self):
        return self.contador
    
    def agregar_contacto(self, contacto):
        """Agrega un contacto a la agenda"""
        if self.contador < self.capacidad:
            self.contactos.append(contacto)
            self.contador += 1
            return True
        return False
    
    def buscar_por_nombre(self, nombre):
        """Busca contactos por nombre"""
        resultados = []
        for contacto in self.contactos:
            if nombre.lower() in contacto.get_nombre().lower():
                resultados.append(contacto)
        return resultados
    
    def buscar_por_telefono(self, telefono):
        """Busca contactos por teléfono"""
        resultados = []
        for contacto in self.contactos:
            if telefono in contacto.get_telefono():
                resultados.append(contacto)
        return resultados
    
    def listar_todos(self):
        """Retorna todos los contactos"""
        return self.contactos
    
    def eliminar_contacto(self, telefono):
        """Elimina un contacto por teléfono"""
        for i, contacto in enumerate(self.contactos):
            if contacto.get_telefono() == telefono:
                self.contactos.pop(i)
                self.contador -= 1
                return True
        return False