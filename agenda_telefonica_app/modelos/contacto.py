class Contacto:
    """
    Clase que representa un contacto de la agenda telefónica
    """
    def __init__(self, nombre="", telefono="", email="", direccion=""):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_telefono(self):
        return self.telefono
    
    def set_telefono(self, telefono):
        self.telefono = telefono
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
    
    def get_direccion(self):
        return self.direccion
    
    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nTeléfono: {self.telefono}\nEmail: {self.email}\nDirección: {self.direccion}\n"