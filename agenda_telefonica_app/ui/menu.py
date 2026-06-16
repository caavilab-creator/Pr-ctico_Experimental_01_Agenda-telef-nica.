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
        print("6. Registrar interacción (Matriz)")
        print("7. Ver estadísticas (Matriz)")
        print("8. Salir")
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
                print(f"[{i}] {contacto}")
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
    
    def registrar_interaccion(self):
        """Permite registrar una interacción en la matriz"""
        print("\n--- REGISTRAR INTERACCIÓN (MATRIZ) ---")
        contactos = self.servicio.obtener_todos_los_contactos()
        
        if len(contactos) == 0:
            print("No hay contactos. Agregue uno primero.")
            return

        print("Seleccione el contacto:")
        for i, c in enumerate(contactos, 1):
            print(f"[{i}] {c.get_nombre()}")
        
        try:
            indice = int(input("Número de contacto: ")) - 1
            if 0 <= indice < len(contactos):
                print("\nTipo de interacción:")
                print("0. Llamada")
                print("1. Mensaje")
                print("2. Email")
                tipo = int(input("Seleccione (0, 1 o 2): "))
                
                if tipo in [0, 1, 2]:
                    self.servicio.registrar_interaccion(indice, tipo)
                    print("✓ Interacción registrada en la matriz.")
                else:
                    print("✗ Tipo de interacción inválido.")
            else:
                print("✗ Índice de contacto inválido.")
        except ValueError:
            print("✗ Entrada inválida.")
    
    def ver_estadisticas_matriz(self):
        """Muestra el recorrido de la matriz"""
        print("\n" + "="*60)
        print("           MATRIZ DE INTERACCIONES")
        print("="*60)
        print(f"{'Contacto':<20} | {'Llamadas':<10} | {'Mensajes':<10} | {'Emails':<10}")
        print("-"*60)
        
        estadisticas = self.servicio.obtener_estadisticas_matriz()
        matriz = self.servicio.agenda.obtener_matriz()
        
        if len(estadisticas) == 0:
            print("La matriz está vacía.")
            print("="*60)
            return

        # Recorrido de la matriz con bucles anidados
        for i in range(len(estadisticas)):
            nombre = estadisticas[i]['nombre'][:18]
            print(f"{nombre:<20} | {matriz[i][0]:<10} | {matriz[i][1]:<10} | {matriz[i][2]:<10}")
        
        print("="*60)
        print("\nLeyenda: Cada fila = un contacto")
        print("Columnas: [0]=Llamadas, [1]=Mensajes, [2]=Emails")