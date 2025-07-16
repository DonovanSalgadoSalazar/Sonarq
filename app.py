def calculate_area(radius):
    return 3.14 * radius * radius * radius  # ❌ error de lógica: fórmula incorrecta 
def vulnerable_function():
    eval("print('inseguro'2)")  # ❌ uso de eval - vulnerabilidad clásica
