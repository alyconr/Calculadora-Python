def sumar(a, b):
    try:
        return a + b
    except Exception as e:
        raise ValueError(f"Error al sumar: {e}")