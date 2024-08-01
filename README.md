# Calculadora de Engranajes

Esta es una aplicación de escritorio simple pero potente para realizar cálculos de engranajes. Utiliza PyQt5 para la interfaz gráfica y proporciona cálculos precisos basados en el módulo o el paso diametral.

## Características

- Cálculos basados en el módulo del engranaje
- Cálculos basados en el paso diametral
- Interfaz gráfica intuitiva
- Resultados detallados incluyendo diámetros, addendum, dedendum, y más

## Requisitos

- Python 3.6+
- PyQt5

## Instalación

1. Clone este repositorio:

   ```bash
   git clone https://github.com/su-usuario/calculadora-engranajes.git
   ```

2. Navegue al directorio del proyecto:

   ```bash
   cd calculadora-engranajes
   ```

3. Instale las dependencias:
   ```bash
   pip install PyQt5
   ```

## Uso

Para ejecutar la aplicación, use el siguiente comando en el directorio del proyecto:

```bash
python main.py
```

### Cálculo basado en el Módulo

1. Ingrese el valor del módulo en el campo "Módulo".
2. Ingrese el número de dientes en el campo correspondiente.
3. Haga clic en "Calcular".

### Cálculo basado en el Paso Diametral

1. Ingrese el valor del paso diametral en el campo "Paso Diametral".
2. Ingrese el número de dientes en el campo correspondiente.
3. Haga clic en "Calcular".

## Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación y definición de la interfaz gráfica.
- `calculations/calculations.py`: Funciones de cálculo principales.
- `gears/gear_module.py`: Clase para cálculos basados en el módulo.
- `gears/gear_diametral_pitch.py`: Clase para cálculos basados en el paso diametral.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de crear un pull request.

## Licencia

Este proyecto está licenciado bajo los términos de la Licencia Pública General de GNU. Consulta el archivo LICENSE para obtener más detalles.
