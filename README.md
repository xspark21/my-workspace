# Purpose

Ofrecer una guia y plantilla para trabajar tanto en proyectos como investigaciones propias.

# how to use it
> en some-notes hay un apunte de ayuda sobre como usar git

Clonar y sincronizar:

```bash
git clone https://github.com/xspark21/my-workspace.git
cd my-workspace # ubicarse en el proyecto
uv sync # sincronizar entorno
uv run main.py # corre archivo main de bienvenida
```

de necesitarse añadir más librerias:

```bash
uv add libreria1 libreria2 libreria3
```
>nota: las librerias deben coincidir con la version de python del proyecto, recuerda revisar el `pyproject.toml` para configurarlo

si quieres hacer un proyecto y subirlo a github pero clonaste este repo:

```bash
rm -rf .git
git init
```

# about `src/`

Estos tres archivos tienen el objetivo de ayudar con ciertos procesos repetitivos y de configuracion ademas de 

- `io.py`: carga de archivos en caso de que sean varios y de distintos tipos
- `config.py`: centraliza rutas de archivos, configuracion de `schemas`, entre otros
- `modules.py`: funciones de ayuda para análisis exploratorio de datos

>nota: añadir o quitar funciones personalizadas segun vayan necesitando

# tree

Visualizacion del espacio de trabajo

```bash
.
├── datasets # carga y proceso de los datos
│   ├── processed/
│   ├── raw/
│   └── README.md
├── main.py # archivo central que orquesta el pipeline
├── notebooks
│   └── example.ipynb # archivo exploratorio
├── pyproject.toml # archivo de configuracion del proyecto
├── README.md 
├── src # carpeta con la fuente de archivos necesarios para el trabajo
│   ├── config.py
│   ├── rw.py # read/write
│   └── modules.py
└── uv.lock
```

en la practica y mientras se estudia solemos usar `colab`, por lo que `notebooks/` vendria a ser el lugar principal de exploracion, si su trabajo escala van a necesitar de todo el árbol completo, adaptado a sus necesidades, por lo que no es prioridad entender el flujo completo

> la mejor forma de mejorar aqui es simplemente intentándolo, no haciéndolo perfecto