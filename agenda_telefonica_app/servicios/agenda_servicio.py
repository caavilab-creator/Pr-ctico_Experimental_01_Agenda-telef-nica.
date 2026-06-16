from modelos.contacto import Contacto
from modelos.agenda import Agenda

class AgendaServicio:
    """
    Clase de servicio que maneja la lógica de negocio
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
    
    def registrar_interaccion(self, indice, tipo):
        """
        Registra una interacción en la matriz
        tipo: 0=Llamada, 1=Mensaje, 2=Email
        """
        return self.agenda.actualizar_interaccion(indice, tipo)
    
    def obtener_estadisticas_matriz(self):
        """Retorna los contactos con sus estadísticas de la matriz"""
        contactos = self.agenda.get_contactos()
        matriz = self.agenda.obtener_matriz()
        
        estadisticas = []
        for i in range(len(contactos)):
            estadisticas.append({
                'nombre': contactos[i].get_nombre(),
                'llamadas': matriz[i][0],
                'mensajes': matriz[i][1],
                'emails': matriz[i][2]
            })
        return estadisticas