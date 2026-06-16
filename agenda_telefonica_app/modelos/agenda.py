class Agenda:
    """
    Clase que representa la agenda telefónica
    Estructuras de datos:
    1. Vector/Array: self.contactos
    2. Matriz: self.matriz_interacciones
    """
    def __init__(self):
        # ESTRUCTURA 1: VECTOR (Lista de objetos Contacto)
        self.contactos = []
        
        # ESTRUCTURA 2: MATRIZ (Array bidimensional)
        # Filas: contactos | Columnas: [Llamadas, Mensajes, Emails]
        self.matriz_interacciones = []
        
        self.capacidad = 100
        self.contador = 0
    
    def get_contactos(self):
        return self.contactos
    
    def get_contador(self):
        return self.contador
    
    def agregar_contacto(self, contacto):
        """Agrega un contacto e inicializa su fila en la matriz"""
        if self.contador < self.capacidad:
            self.contactos.append(contacto)
            # Inicializar fila de matriz con ceros [0, 0, 0]
            self.matriz_interacciones.append([0, 0, 0])
            self.contador += 1
            return True
        return False
    
    def actualizar_interaccion(self, indice_contacto, tipo_interaccion):
        """
        Actualiza la matriz de interacciones
        tipo_interaccion: 0=Llamada, 1=Mensaje, 2=Email
        """
        if 0 <= indice_contacto < len(self.matriz_interacciones):
            self.matriz_interacciones[indice_contacto][tipo_interaccion] += 1
            return True
        return False
    
    def obtener_matriz(self):
        """Retorna la matriz completa"""
        return self.matriz_interacciones
    
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
        """Elimina un contacto y su fila en la matriz"""
        for i, contacto in enumerate(self.contactos):
            if contacto.get_telefono() == telefono:
                self.contactos.pop(i)
                self.matriz_interacciones.pop(i)
                self.contador -= 1
                return True
        return False