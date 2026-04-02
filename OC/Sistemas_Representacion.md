# 💻 Sistemas de Representación Numérica (OC)

Apuntes teóricos y ejercicios prácticos sobre cómo la computadora interpreta los datos a nivel de bits.

---

## 🔢 Representación de Enteros

Para representar números con signo, utilizamos diferentes sistemas según la arquitectura:

### 1. Complemento a 1 (CA1)
* **Lógica:** Se invierten todos los bits del número original (0 pasa a 1, y 1 pasa a 0).
* **Problema:** Tiene dos representaciones para el cero (+0 y -0).

### 2. Complemento a 2 (CA2) - *El más utilizado*
* **Lógica:** Se obtiene sacando el CA1 y sumándole 1 al resultado.
* **Ventaja:** Solo existe una representación para el cero y facilita las operaciones aritméticas en la ALU.
* **Rango:** Con $n$ bits, el rango es $[-2^{n-1}, 2^{n-1}-1]$.

### 3. Exceso a $2^{n-1}$ (o Exceso K)
* Se utiliza principalmente para el **exponente** en Punto Flotante.
* **Lógica:** Al número decimal se le suma una constante $K$ (el exceso) y luego se pasa a binario sin signo.

---

## 🚩 Banderas de la ALU (Flags)

Indican el estado del resultado después de una operación aritmética:

* **Z (Zero):** Se activa (1) si el resultado es **todo ceros**.
* **C (Carry):** Se activa si hubo un "acarreo" (sobró un bit a la izquierda) en una suma sin signo.
* **V (Overflow):** Indica un error de rango en operaciones con signo (el resultado no entra en los bits disponibles).
* **N (Negative):** Se activa si el bit de mayor peso (el primero de la izquierda) es 1.

---

## 🚀 Punto Flotante (IEEE 754)

Estándar para representar números reales (con coma).
* **Signo:** 1 bit (0 positivo, 1 negativo).
* **Exponente:** Representado en **Exceso**.
* **Mantisa:** La parte fraccionaria del número normalizado.

---
> *Nota: Estos conceptos son fundamentales para entender cómo funciona el procesador antes de pasar a programar en Assembler (MSX88 / WinMIPS64).*
