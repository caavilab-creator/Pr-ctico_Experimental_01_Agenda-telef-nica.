from modelos.contacto import Contacto
from modelos.agenda import Agenda

class AgendaServicio:
    """
    Clase de servicio que maneja la lógica de negocio de la agenda
    """
    def __init__(self):
        self.agenda = Agenda()
    
    def crear_contacto(self, nombre, telefono, email="", direccion=""):
        """Crea un nuevo contacto y lo agrega a la agenda"""
        if not nombre or not telefono:
            return False, "Nombre y teléfono son obligatorios"
        
        contacto = Contacto(nombre, telefono, email, direccion)
        exito = self.agenda.agregar_contacto(contacto)
        
        if exito:
            return True, "Contacto agregado exitosamente"
        else:
            return False, "Agenda llena. No se puede agregar más contactos"
    
    def obtener_todos_los_contactos(self):
        """Obtiene todos los contactos"""
        return self.agenda.listar_todos()
    
    def buscar_contactos(self, criterio, tipo="nombre"):
        """Busca contactos según el criterio"""
        if tipo == "nombre":
            return self.agenda.buscar_por_nombre(criterio)
        elif tipo == "telefono":
            return self.agenda.buscar_por_telefono(criterio)
        return []
    
    def eliminar_contacto(self, telefono):
        """Elimina un contacto"""
        return self.agenda.eliminar_contacto(telefono)
    
    def contar_contactos(self):
        """Retorna el número de contactos"""
        return self.agenda.get_contador()