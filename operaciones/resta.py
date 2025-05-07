def restar(a,b):
    try:
        return a - b
    except Exception as e:
        print(f"Error en la resta: {e}")
        return None
    