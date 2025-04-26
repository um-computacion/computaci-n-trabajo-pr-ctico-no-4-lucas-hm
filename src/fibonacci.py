def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma recursiva.
    
    Args:
        n (int): El índice del número de Fibonacci a calcular.
        
    Returns:
        int: El n-ésimo número de Fibonacci.
        
    Raises:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número de Fibonacci no está definido para índices negativos.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma iterativa.
    
    Args:
        n (int): El índice del número de Fibonacci a calcular.
        
    Returns:
        int: El n-ésimo número de Fibonacci.
        
    Raises:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número de Fibonacci no está definido para índices negativos.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a