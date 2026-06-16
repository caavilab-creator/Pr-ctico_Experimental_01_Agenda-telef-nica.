class MenuAgenda:
    """
    Clase que maneja la interfaz de usuario en consola
    """
    def __init__(self, servicio):
        self.servicio = servicio
    
    def mostrar_menu(self):
        """Muestra el menú principal"""
        print("\n" + "="*40)
        print("       AGENDA TELEFÓNICA")
        print("="*40)
        print("1. Agregar contacto")
        print("2. Listar todos los contactos")
        print("3. Buscar por nombre")
        print("4. Buscar por teléfono")
        print("5. Eliminar contacto")
        print("6. Ver cantidad de contactos")
        print("7. Salir")
        print("="*40)
    
    def agregar_contacto(self):
        """Interfaz para agregar contacto"""
        print("\n--- AGREGAR NUEVO CONTACTO ---")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email (opcional): ")
        direccion = input("Dirección (opcional): ")
        
        exito, mensaje = self.servicio.crear_contacto(nombre, telefono, email, direccion)
        print(f"\n{'✓' if exito else '✗'} {mensaje}")
    
    def listar_contactos(self):
        """Interfaz para listar contactos"""
        print("\n--- LISTA DE CONTACTOS ---")
        contactos = self.servicio.obtener_todos_los_contactos()
        
        if len(contactos) == 0:
            print("No hay contactos registrados")
        else:
            print(f"Total de contactos: {len(contactos)}\n")
            for i, contacto in enumerate(contactos, 1):
                print(f"Contacto #{i}")
                print(contacto)
                print("-" * 30)
    
    def buscar_contacto(self):
        """Interfaz para buscar contacto"""
        print("\n--- BUSCAR CONTACTO ---")
        print("1. Buscar por nombre")
        print("2. Buscar por teléfono")
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            criterio = input("Ingrese nombre a buscar: ")
            resultados = self.servicio.buscar_contactos(criterio, "nombre")
        elif opcion == "2":
            criterio = input("Ingrese teléfono a buscar: ")
            resultados = self.servicio.buscar_contactos(criterio, "telefono")
        else:
            print("Opción inválida")
            return
        
        if len(resultados) == 0:
            print("No se encontraron contactos")
        else:
            print(f"\nSe encontraron {len(resultados)} contacto(s):\n")
            for contacto in resultados:
                print(contacto)
                print("-" * 30)
    
    def eliminar_contacto(self):
        """Interfaz para eliminar contacto"""
        print("\n--- ELIMINAR CONTACTO ---")
        telefono = input("Ingrese el teléfono del contacto a eliminar: ")
        exito = self.servicio.eliminar_contacto(telefono)
        print(f"\n{'✓ Contacto eliminado' if exito else '✗ Contacto no encontrado'}")
    
    def ver_cantidad(self):
        """Muestra la cantidad de contactos"""
        cantidad = self.servicio.contar_contactos()
        print(f"\nTotal de contactos en la agenda: {cantidad}")