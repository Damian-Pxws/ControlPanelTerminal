#!/usr/bin/env python3
from utils.db import añadir_tarea, listar_tareas, eliminar_tarea
from rich.console import Console
from rich.prompt import Prompt
import psutil
import os
import json
import subprocess

console = Console()

def ver_estado_sistema():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disco = psutil.disk_usage("/").percent

    console.print(f"\n[bold yellow]Estado del Sistema:[/bold yellow]")
    console.print(f"[cyan]CPU:[/cyan] {cpu}%")
    console.print(f"[cyan]RAM:[/cyan] {ram}%")
    console.print(f"[cyan]Disco:[/cyan] {disco}%")

def ejecutar_script():
    if not os.path.exists("scripts.json"):
        console.print("[red]No se encontró scripts.json[/red]")
        return

    with open("scripts.json", "r") as f:
        scripts = json.load(f)

    console.print("\n[bold cyan]Scripts disponibles:[/bold cyan]")
    for nombre in scripts:
        console.print(f"- {nombre}")

    nombre = Prompt.ask("¿Qué script deseas ejecutar?")
    comando = scripts.get(nombre)

    if comando:
        console.print(f"[blue]Ejecutando:[/blue] {comando}")
        subprocess.run(comando, shell=True)
    else:
        console.print(f"[yellow]Script no encontrado en la lista, intentando ejecutar directamente: {nombre}[/yellow]")
        subprocess.run(nombre, shell=True)

def main():
    while True:
        console.print("\n[bold cyan]Panel CLI - Control Rápido[/bold cyan]")
        console.print("1. Ver estado del sistema")
        console.print("2. Añadir tarea")
        console.print("3. Ver tareas")
        console.print("4. Eliminar tarea")
        console.print("5. Ejecutar script favorito")
        console.print("6. Añadir nuevo script favorito")
        console.print("7. Eliminar script favorito")
        console.print("8. Salir")

        opcion = Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4", "5", "6", "7", "8"])

        if opcion == "1":
            ver_estado_sistema()

        elif opcion == "2":
            tarea = Prompt.ask("Escribe la nueva tarea")
            añadir_tarea(tarea)
            console.print("[green]Tarea añadida correctamente[/green]")

        elif opcion == "3":
            tareas = listar_tareas()
            if not tareas:
                console.print("[yellow]No hay tareas[/yellow]")
            else:
                for i, t in enumerate(tareas):
                    console.print(f"[{i}] {t}")

        elif opcion == "4":
            tareas = listar_tareas()
            if not tareas:
                console.print("[yellow]No hay tareas para eliminar[/yellow]")
            else:
                for i, t in enumerate(tareas):
                    console.print(f"[{i}] {t}")
                idx = int(Prompt.ask("Elige el número de tarea a eliminar"))
                if eliminar_tarea(idx):
                    console.print("[green]Tarea eliminada[/green]")
                else:
                    console.print("[red]Índice inválido[/red]")

        elif opcion == "5":
            ejecutar_script()

        elif opcion == "6":
            nombre = Prompt.ask("Nombre del script (como lo verás en la lista)")
            comando = Prompt.ask("Comando a ejecutar")

            if not os.path.exists("scripts.json"):
                with open("scripts.json", "w") as f:
                    json.dump({}, f, indent=2)

            with open("scripts.json", "r") as f:
                data = json.load(f)

            data[nombre] = comando

            with open("scripts.json", "w") as f:
                json.dump(data, f, indent=2)

            console.print("[green]Script añadido correctamente[/green]")

        elif opcion == "7":
            if not os.path.exists("scripts.json"):
                console.print("[red]No hay scripts para eliminar[/red]")
            else:
                with open("scripts.json", "r") as f:
                    data = json.load(f)

                if not data:
                    console.print("[yellow]La lista de scripts está vacía[/yellow]")
                else:
                    console.print("\n[bold cyan]Scripts disponibles:[/bold cyan]")
                    keys = list(data.keys())
                    for i, name in enumerate(keys):
                        console.print(f"[{i}] {name}")

                    idx = int(Prompt.ask("Índice del script a eliminar"))
                    if 0 <= idx < len(keys):
                        eliminado = keys[idx]
                        del data[eliminado]
                        with open("scripts.json", "w") as f:
                            json.dump(data, f, indent=2)
                        console.print(f"[green]Script '{eliminado}' eliminado correctamente[/green]")
                    else:
                        console.print("[red]Índice no válido[/red]")

        elif opcion == "8":
            console.print("\n[green]Saliendo del panel...[/green]")
            break

if __name__ == "__main__":
    main()