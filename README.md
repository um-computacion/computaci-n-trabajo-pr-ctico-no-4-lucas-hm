# Trabajo Práctico 4: Recursividad

## Información del Alumno
- Nombre: Lucas
- Apellido: Moran
- Legajo: 64043

## Objetivos
- Comprender y aplicar el concepto de recursividad
- Implementar soluciones iterativas y recursivas para problemas clásicos
- Practicar el desarrollo guiado por pruebas (TDD)
- Trabajar con estructuras de datos anidadas
- Utilizar el framework de testing unittest de Python

## Requisitos Previos
- Python 3.x
- Conocimientos básicos de programación
- Git y GitHub
- unittest (incluido en la biblioteca estándar de Python)

## Estructura del Trabajo
El trabajo está dividido en etapas, cada una debe ser implementada en commits separados dentro del mismo repositorio:

### Etapa 1: Factorial
Implementar dos versiones de la función factorial:
1. Versión iterativa
2. Versión recursiva

**Requisitos:**
- Crear un archivo `factorial.py` con las implementaciones
- Crear un archivo `test_factorial.py` con los casos de prueba
- Implementar manejo de casos especiales (números negativos, cero)
- Documentar las funciones con docstrings

### Etapa 2: Fibonacci
Implementar dos versiones de la función fibonacci:
1. Versión iterativa
2. Versión recursiva

**Requisitos:**
- Crear un archivo `fibonacci.py` con las implementaciones
- Crear un archivo `test_fibonacci.py` con los casos de prueba
- Implementar manejo de casos especiales (números negativos, cero)
- Documentar las funciones con docstrings

### Etapa 3: Aplanar Listas
Implementar una función recursiva que aplane listas anidadas.

**Requisitos:**
- Crear un archivo `flatten.py` con la implementación
- Crear un archivo `test_flatten.py` con los casos de prueba
- Manejar diferentes tipos de estructuras de datos anidadas

## Casos de Prueba

### Caso 1: Lista Simple
```python
lista = [1, 2, 3, 4]
resultado_esperado = [1, 2, 3, 4]
```

### Caso 2: Lista con Listas Anidadas
```python
lista = [1, [2, 3], [4, [5, 6]]]
resultado_esperado = [1, 2, 3, 4, 5, 6]
```

### Caso 3: Lista con Diferentes Estructuras
```python
lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
resultado_esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
```

## Criterios de Evaluación
1. Correctitud de las implementaciones
2. Cobertura de casos de prueba
3. Calidad del código (legibilidad, documentación)
4. Uso correcto de TDD
5. Manejo de casos especiales
6. Organización del repositorio

## Entrega
Para cada etapa:
1. Realizar un commit con los cambios correspondientes
2. Incluir los archivos de implementación y pruebas
3. Incluir un README.md con:
   - Descripción del problema
   - Instrucciones de ejecución
   - Ejemplos de uso
   - Capturas de pantalla de los tests ejecutados

## Notas Importantes
- Cada etapa debe ser implementada en commits separados
- Los tests deben ejecutarse correctamente
- El código debe estar documentado
- Se debe seguir el enfoque TDD
