from servicios.agenda_servicio import AgendaServicio
from ui.menu import MenuAgenda

def main():
    """
    Programa Principal - Agenda Telefónica
    Estructura de Datos - Unidad 1
    Universidad Estatal Amazónica (UEA)
    """
    print("="*40)
    print("   SISTEMA DE AGENDA TELEFÓNICA")
    print("   Estructura de Datos - UEA")
    print("="*40)
    
    # Inicializar servicio y menú
    servicio = AgendaServicio()
    menu = MenuAgenda(servicio)
    
    while True:
        menu.mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu.agregar_contacto()
        elif opcion == "2":
            menu.listar_contactos()
        elif opcion == "3":
            menu.buscar_contacto()
        elif opcion == "4":
            menu.buscar_contacto()
        elif opcion == "5":
            menu.eliminar_contacto()
        elif opcion == "6":
            menu.registrar_interaccion()
        elif opcion == "7":
            menu.ver_estadisticas_matriz()
        elif opcion == "8":
            print("\n¡Gracias por usar la Agenda Telefónica!")
            print("Hasta luego...")
            break
        else:
            print("\n✗ Opción inválida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()