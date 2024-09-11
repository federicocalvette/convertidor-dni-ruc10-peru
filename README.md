# Convertidor de DNI a RUC 10 - Perú

Este proyecto permite convertir un DNI peruano en su correspondiente RUC 10, utilizando un algoritmo que incluye el cálculo de su dígito verificador.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/federicocalvette/convertidor-dni-ruc10-peru.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd convertidor-dni-ruc10-peru
    ```

## Uso

Para ejecutar el script y convertir un DNI en un RUC 10, simplemente corre el archivo `main.py`:

```bash
python3 main.py
```

El script solicitará ingresar un DNI de 8 dígitos. A continuación, calculará y mostrará el RUC 10 correspondiente.

### Ejemplo

```bash
python3 main.py 
Ingrese su DNI: 12345678
El RUC 10 correspondiente al DNI 12345678 es: 10123456781
```


## Algoritmo

1. Se le añade el prefijo `10` al DNI ingresado.
2. Se utiliza una serie de coeficientes para calcular el dígito verificador.
3. El RUC 10 es la concatenación del prefijo, el DNI, y el dígito verificador.


