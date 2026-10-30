# 🚴 Sistema de Navegación y Optimización de Rutas Urbanas

Prototipo de arquitectura de software para la evaluación y optimización de rutas logísticas y de transporte inteligente en tiempo real, desarrollado como parte de la asignatura **Arquitectura de Software (Unidad 3)** bajo la metodología de Aprendizaje Basado en Proyectos (ABP).

---

## 👥 Equipo de Trabajo y Roles

* **David Chicino Zapata** – Líder de Proyecto & Arquitecto Principal
* **Stefanny Manrique** – Diseñadora UML y Analista de Requisitos
* **Daniel Posada** – Programador del Prototipo Backend
* **Daniel Iriarte** – Investigador de Patrones y Analista de Calidad (QA)

---

## 🎯 Descripción del Problema y Solución

En entornos urbanos congestionados, los sistemas de navegación tradicionales basados en algoritmos rígidos no logran adaptarse eficientemente a imprevistos viales (bloqueos, accidentes, tráfico elevado). 

Este proyecto implementa un modelo de **navegación adaptativa en tiempo real** utilizando un grafo ponderado dinámico y desacoplando la lógica de negocio a través de **cuatro patrones de diseño orientados a objetos**:

1. **Strategy Pattern:** Permite alternar dinámicamente entre distintas heurísticas de optimización (*Ruta Más Corta* en distancia vs. *Ruta Más Rápida* en tiempo) sin alterar el cliente.
2. **Observer Pattern:** Registra eventos de tráfico e incidentes viales, notificando al controlador para invalidar o reevaluar la ruta activa.
3. **Command Pattern:** Encapsula cada solicitud de navegación como una orden independiente, garantizando trazabilidad, auditoría e historial de operaciones.
4. **Iterator Pattern:** Ofrece un recorrido secuencial y desacoplado sobre los tramos e itinerarios resultantes para la interfaz.

---

## 📐 Modelado Arquitectónico (UML)

El diseño de la solución incluye los siguientes diagramas UML:
* **Diagrama de Componentes:** Organización en capas (*Presentación*, *Control y Orquestación*, *Lógica y Patrones*, *Datos y Red*).
* **Diagrama de Secuencia:** Flujo paso a paso de atención a solicitudes de cálculo de ruta.
* **Diagrama de Clases:** Estructura modular de interfaces y clases concretas (*EstrategiaNavegacion*, *NotificadorTrafico*, *ComandoNavegacion*).
* **Diagrama de Actividades:** Lógica de toma de decisiones para la asignación de heurísticas y resolución de contingencias.

---

## 🛠️ Requisitos e Instalación

### Prerrequisitos
* Python 3.10 o superior
* Git

### Configuración del Entorno
```bash
# 1. Clonar el repositorio
git clone [https://github.com/DavidNanis/Proyecto_Navegacion_Urbana.git](https://github.com/DavidNanis/Proyecto_Navegacion_Urbana.git)
cd Proyecto_Navegacion_Urbana

# 2. Crear y activar entorno virtual
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install networkx