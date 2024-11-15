# Proyecto de Análisis de Contratos Inteligentes

Este repositorio permite realizar un análisis de contratos inteligentes escritos en Solidity mediante un workflow en GitHub Actions. Los contratos se analizan automáticamente al hacer un push al repositorio, lo que permite detectar posibles vulnerabilidades y problemas de seguridad.

## Descripción General

Este proyecto está diseñado para analizar contratos inteligentes y detectar posibles vulnerabilidades y problemas comunes de seguridad en contratos escritos en Solidity. Utiliza [Mythril](https://github.com/ConsenSys/mythril), una herramienta de análisis estático y simbólico para detectar fallos en contratos inteligentes.

El proyecto utiliza GitHub Actions para integrar el análisis en el flujo de trabajo de GitHub, ideal para desarrolladores que deseen analizar sus contratos al hacer cambios en el repositorio.

---

## Análisis en GitHub CI/CD

### Requisitos

- **GitHub Account**: Se necesita una cuenta en GitHub para clonar el repositorio y configurar el workflow de CI/CD.
- **Mythril**: El workflow instala Mythril automáticamente para realizar el análisis de los contratos.

### Configuración del Workflow

El workflow de GitHub Actions está configurado para ejecutarse automáticamente cuando se realiza un push o pull request en la rama `main`. El archivo de configuración del workflow se encuentra en `.github/workflows/main.yml`.

### Instrucciones para Usuarios

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/TuUsuario/TuRepositorio.git
   cd TuRepositorio
   
2. **Añadir contratos**: Coloca los contratos que deseas analizar en la carpeta tests/contracts/. Asegúrate de que los archivos tengan la extensión .sol.

3. **Subir los cambios**: Realiza un commit y un push de los cambios:
   ```bash
   git add .
   git commit -m "Añadir contratos para análisis"
   git push origin main

4. **Revisar el Workflow**: Una vez que el push esté completo, ve a la pestaña "Actions" en GitHub para ver el progreso del análisis. El workflow se ejecutará automáticamente y analizará los contratos en la carpeta tests/contracts.

**Acceso a los Reportes**
Los reportes generados se almacenan como artefactos en GitHub Actions y están disponibles para su descarga después de cada ejecución del workflow. Para acceder a ellos:
  1. Ve a la pestaña "Actions" de tu repositorio en GitHub.
  2. Selecciona el workflow más reciente en la lista.
  3. En la sección de "Artifacts", encontrarás un archivo llamado `reports` que contiene los reportes generados para cada contrato analizado.
     
**Funcionalidades**
-  **Detección de vulnerabilidades**: Mythril detecta automáticamente problemas de seguridad como reentrancias, desbordamientos de enteros, y uso inseguro de `tx.origin`.
-  **Generación de reportes**: Los reportes se guardan como artefactos de GitHub Actions con nombres únicos basados en el nombre del contrato y la fecha de análisis, para evitar sobreescrituras.
  
**Configuración y Personalización**
Puedes ajustar configuraciones de análisis editando el archivo `config/config.json`. Aquí se pueden definir opciones como el formato del reporte `(JSON, CSV, HTML)` y otros parámetros del análisis.

**Ejemplo de Archivo:** `.github/workflows/main.yml`
```bash
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Install Mythril
      run: pip install mythril

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.12'

    - name: Cache dependencies
      uses: actions/cache@v2
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
          
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run analysis
      run: python ci_analysis.py

    - name: Upload reports
      uses: actions/upload-artifact@v3
      with:
        name: reports
        path: reports/
