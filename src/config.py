from pathlib import Path

import polars as pl

# directorios
data_dir = Path("datasets")
raw_dir = data_dir / "raw"            # datos originales, solo lectura
processed_dir = data_dir / "processed"  # datos ya transformados, listos para analisis

# los schemas sirven para optimizar recursos a la hora de cargar datos (tambien cuando se tratan de pipelines)
# usualmente cuando tenemos informacion previa y sirve para facilitar la lectura de datos
# se declara por columna y tipo de dato en esa columna

schema = {
    "nombre de la columna con datos en formato texto": pl.String,
    "nombre de la columna con datos enteros o naturales": pl.Int64,
    "nombre de la columna con datos true/false o True/False": pl.Boolean,
    "nombre de la columna con datos decimales como 1.2 o 3.1415...": pl.Float64,
}

# NOTA: schema tambien sirve para corregir datos mal detectados y da total claridad.


# si quieres usar tus propias versiones de IO, aqui hay otra forma de acceder a los archivos
# por ejemplo si solo quisieras acceder a un cierto conjunto lo puedes definir como:

conjunto = [
        "datasets/raw/archivo_tipo.csv", # formato comun (lento y pesado)
        "datasets/raw/archivo_tipo.xlsx", # formato excel
        "datasets/raw/archivo_tipo.parquet", # formato estandar de industria (recomendable)
        "datasets/raw/archivo_tipo.rda", # formato de bases de datos de R
    # otros formatos ...
    ]


# truco avanzado

# si tengo varios archivos distintos, guardo sus direcciones en un diccionario y los uso despues
# IO lo resuelve con el parametro "ext"
archivos= {
        "CSV":["datasets/raw/archivo_tipo.csv"], # lista de archivos csv
        "XLSX":["datasets/raw/archivo_tipo.xlsx"], # lista de archivos excel (xlsx)
        "PARQUET":["datasets/raw/archivo_tipo.parquet"], # lista de archivos parquet
        "RDA":["datasets/raw/archivo_tipo.rda"], # lista de archivos rda para R
    # ...
}
