import time
import networkx as nx

# --- PATRÓN OBSERVER ---
class ObservadorTráfico:
    def actualizar(self, origen, destino, nuevo_peso):
        print(f"  [ALERTA TRÁFICO] Vía {origen} -> {destino} actualizada a costo: {nuevo_peso}")

class NotificadorTrafico:
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, obs):
        self._observadores.append(obs)

    def notificar(self, u, v, peso):
        for obs in self._observadores:
            obs.actualizar(u, v, peso)

# --- PATRÓN STRATEGY ---
class EstrategiaNavegacion:
    def calcular_ruta(self, grafo, origen, destino):
        pass

class EstrategiaRutaMasCorta(EstrategiaNavegacion):
    def calcular_ruta(self, grafo, origen, destino):
        try:
            return nx.dijkstra_path(grafo, origen, destino, weight='distancia')
        except nx.NetworkXNoPath:
            return None

class EstrategiaRutaMasRapida(EstrategiaNavegacion):
    def calcular_ruta(self, grafo, origen, destino):
        try:
            return nx.dijkstra_path(grafo, origen, destino, weight='tiempo')
        except nx.NetworkXNoPath:
            return None

# --- PATRÓN COMMAND ---
class ComandoNavegacion:
    def __init__(self, estrategia, grafo, origen, destino):
        self.estrategia = estrategia
        self.grafo = grafo
        self.origen = origen
        self.destino = destino
        self.resultado_ruta = None

    def ejecutar(self):
        inicio = time.perf_counter()
        self.resultado_ruta = self.estrategia.calcular_ruta(self.grafo, self.origen, self.destino)
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        return self.resultado_ruta, tiempo_ms

# --- PATRÓN ITERATOR ---
class IteradorRuta:
    def __init__(self, ruta):
        self._ruta = ruta if ruta else []
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._ruta):
            nodo = self._ruta[self._index]
            self._index += 1
            return nodo
        else:
            raise StopIteration

# --- PROGRAMA PRINCIPAL Y BATERÍA EXTENDIDA DE PRUEBAS ---
if __name__ == "__main__":
    print("==================================================")
    print("  SISTEMA DE NAVEGACIÓN Y OPTIMIZACIÓN URBANA   ")
    print("  Batería Completa de Pruebas Arquitectónicas  ")
    print("==================================================\n")

    # Construcción del Grafo Urbano
    G = nx.DiGraph()
    vias = [
        ("Nodo_A", "Nodo_B", 5, 10),
        ("Nodo_B", "Nodo_C", 3, 15),
        ("Nodo_A", "Nodo_D", 8, 8),
        ("Nodo_D", "Nodo_C", 4, 6),
        ("Nodo_B", "Nodo_D", 2, 4)
    ]
    for u, v, d, t in vias:
        G.add_edge(u, v, distancia=d, tiempo=t)

    notificador = NotificadorTrafico()
    notificador.agregar_observador(ObservadorTráfico())

    # --- PRUEBA 1: Ruta Más Corta (Distancia) ---
    print(">>> PRUEBA 1: Evaluación con Estrategia Ruta Más Corta (Distancia)")
    cmd1 = ComandoNavegacion(EstrategiaRutaMasCorta(), G, "Nodo_A", "Nodo_C")
    ruta1, t1 = cmd1.ejecutar()
    print(f"  Ruta generada: {' -> '.join(IteradorRuta(ruta1))}")
    print(f"  Tiempo de ejecución del algoritmo: {t1:.4f} ms\n")

    # --- PRUEBA 2: Ruta Más Rápida (Tiempo) ---
    print(">>> PRUEBA 2: Evaluación con Estrategia Ruta Más Rápida (Tiempo)")
    cmd2 = ComandoNavegacion(EstrategiaRutaMasRapida(), G, "Nodo_A", "Nodo_C")
    ruta2, t2 = cmd2.ejecutar()
    print(f"  Ruta generada: {' -> '.join(IteradorRuta(ruta2))}")
    print(f"  Tiempo de ejecución del algoritmo: {t2:.4f} ms\n")

    # --- PRUEBA 3: Evento de Tráfico Dinámico ---
    print(">>> PRUEBA 3: Simulación de Incidente de Tráfico Dinámico en Tiempo Real")
    G["Nodo_A"]["Nodo_D"]["tiempo"] = 45 
    notificador.notificar("Nodo_A", "Nodo_D", 45)

    print("  Recalculando ruta en tiempo real...")
    cmd3 = ComandoNavegacion(EstrategiaRutaMasRapida(), G, "Nodo_A", "Nodo_C")
    ruta3, t3 = cmd3.ejecutar()
    print(f"  Ruta adaptativa óptima: {' -> '.join(IteradorRuta(ruta3))}")
    print(f"  Tiempo de recálculo: {t3:.4f} ms\n")

    # --- PRUEBA 4 (NUEVA): Manejo de Excepciones por Destino Inalcanzable ---
    print(">>> PRUEBA 4: Manejo de Excepciones y Resiliencia (Destino Inalcanzable)")
    G.add_node("Nodo_Aislado")
    cmd4 = ComandoNavegacion(EstrategiaRutaMasRapida(), G, "Nodo_A", "Nodo_Aislado")
    ruta4, t4 = cmd4.ejecutar()
    if ruta4 is None:
        print("  [RESULTADO EXPECTATIVO]: El sistema detectó correctamente que no existe ruta hacia 'Nodo_Aislado'.")
    print(f"  Tiempo de verificación de no-conectividad: {t4:.4f} ms\n")

    # --- PRUEBA 5 (NUEVA): Prueba de Carga / Estrés de Navegación ---
    print(">>> PRUEBA 5: Evaluación de Escalabilidad (Prueba de Estrés: 1,000 Consultas)")
    inicio_estres = time.perf_counter()
    for _ in range(1000):
        cmd_estres = ComandoNavegacion(EstrategiaRutaMasRapida(), G, "Nodo_A", "Nodo_C")
        cmd_estres.ejecutar()
    fin_estres = time.perf_counter()
    tiempo_total_estres = (fin_estres - inicio_estres) * 1000
    promedio_estres = tiempo_total_estres / 1000
    print(f"  Tiempo acumulado para 1,000 peticiones: {tiempo_total_estres:.2f} ms")
    print(f"  Promedio por consulta bajo alta concurrencia: {promedio_estres:.4f} ms\n")

    # --- PRUEBA 6 (NUEVA): Trazabilidad e Historial con Patrón Command ---
    print(">>> PRUEBA 6: Auditoría y Historial de Órdenes Ejecutadas (Patrón Command)")
    historial_comandos = [cmd1, cmd2, cmd3, cmd4]
    print("  [REGISTRO DE AUDITORÍA DE NAVEGACIÓN]:")
    for i, cmd in enumerate(historial_comandos, 1):
        estado_desc = "Exitosa" if cmd.resultado_ruta else "Ruta No Encontrada"
        ruta_str = ' -> '.join(cmd.resultado_ruta) if cmd.resultado_ruta else "N/A"
        print(f"    Comando #{i}: Origen={cmd.origen} | Destino={cmd.destino} | Estado={estado_desc} | Ruta=[{ruta_str}]")

    print("\n==================================================")