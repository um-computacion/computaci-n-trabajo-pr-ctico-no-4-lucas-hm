def factorial_iterativo(n):
    """
    Calcula el factorial de un número de forma iterativa.
    
    Args:
        n (int): Número entero no negativo.
    
    Returns:
        int: Factorial de n.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_iterativo_while(n):
    """
    Calcula el factorial de un número usando un bucle while.
    
    Args:
        n (int): Número entero no negativo.
    
    Returns:
        int: Factorial de n.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

def factorial_recursivo(n):
    """
    Calcula el factorial de un número de forma recursiva.
    
    Args:
        n (int): Número entero no negativo.
    
    Returns:
        int: Factorial de n.
    
    Raises:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)

def factorial_recursivo_ternario(n):
    """
    Calcula el factorial de un número usando recursión con operador ternario.
    
    Args:
        n (int): Número entero no negativo.
    
    Returns:
        int: Factorial de n.
    
    Raises:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    return 1 if n == 0 else n * factorial_recursivo_ternario(n - 1)