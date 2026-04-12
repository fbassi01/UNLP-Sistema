def float_to_ieee754(n):
    """
    Convierte un número decimal a su representación en punto flotante 
    de precisión simple (IEEE 754 - 32 bits).
    """
    if n == 0:
        return "0" * 32

    # 1. Signo
    signo = "0" if n > 0 else "1"
    n = abs(n)

    # 2. Convertir a binario
    entero = int(n)
    decimal = n - entero
    
    bin_entero = bin(entero).lstrip("0b")
    
    # Parte fraccionaria
    bin_decimal = ""
    while decimal > 0 and len(bin_decimal) < 32:
        decimal *= 2
        if decimal >= 1:
            bin_decimal += "1"
            decimal -= 1
        else:
            bin_decimal += "0"

    # 3. Normalización (1.mantisa * 2^exponente)
    if entero > 0:
        exponente_real = len(bin_entero) - 1
        mantisa = (bin_entero + bin_decimal)[1:24]
    else:
        # Caso de números < 1
        primer_uno = bin_decimal.find("1")
        exponente_real = -(primer_uno + 1)
        mantisa = bin_decimal[primer_uno + 1 : primer_uno + 24]

    # 4. Exponente con exceso (Bias 127)
    exponente_exceso = exponente_real + 127
    bin_exponente = bin(exponente_exceso).lstrip("0b").zfill(8)

    # 5. Ajustar mantisa a 23 bits
    mantisa = mantisa.ljust(23, "0")

    return f"{signo} | {bin_exponente} | {mantisa}"

# Ejemplo de uso
if __name__ == "__main__":
    numero = 12.625
    resultado = float_to_ieee754(numero)
    
    print(f"Conversor IEEE 754 (Precisión Simple)")
    print(f"Decimal: {numero}")
    print(f"Representación (Signo | Exponente | Mantisa):")
    print(resultado)
