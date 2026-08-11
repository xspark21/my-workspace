import polars as pl

# si tienen archivos separados por años o periodos pueden ponerlos en una lista
# llamarlos uno a uno y evitar escribir direccion por direccion
rutas_archivos = [
        "datasets/raw/archivo_tipo.csv ", # formato comun (lento y pesado)
        "datasets/raw/archivo_tipo.xslx", # formato excel
        "datasets/raw/archivo_tipo.parquet", # formato estandar de industria (recomendable)
        "datasets/raw/archivo_tipo.rda", # formato de bases de datos de R
    # ... 
    ]



# los schemas sirven para optimizar recursos a la hora de cargar datos (tambien cuando se tratan de pipelines)
# usualmente cuando tenemos informacion previa y sirve para facilitar la lectura de datos
# se declara por columna y tipo de dato en esa columna

schema = {
    "nombre de la columna con datos en formato texto": pl.String,
    "nombre de la columna con datos enteros o naturales": pl.Int64,
    "nombre de la columna con datos 0, 1": pl.Boolean,
    "nombre de la columna con datos decimales como 1.2 o 3.1415...": pl.Float64,
}

# NOTA: schema tambien sirve para corregir datos mal detectados y da total claridad.



# truco avanzado

# si tengo varios archivos distintos, guardo sus direcciones en un diccionario y los uso despues
rutas_archivos_2 = {
        "CSV":["datasets/raw/archivo_tipo.csv "], # lista de archivos csv
        "XLSX":["datasets/raw/archivo_tipo.xslx"], # lista de archivos excel (xlsx)
        "PARQUET":["datasets/raw/archivo_tipo.parquet"], # lista de archivos parquet
        "RDA":["datasets/raw/archivo_tipo.rda"], # lista de archivos rda para R
    # ... 
}    
