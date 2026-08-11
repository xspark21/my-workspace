import polars as pl
from config import schema, rutas_archivos


# lectura lazy, usualmente para bases grandes

def load_lazy(dir: "Direccion de los datos") -> pl.LazyFrame:
    """
    cargar datos de forma lazy siguiendo la ruta en src/config.py
    """
    lfs = []
    for f in sorted(fixed_dir.glob("*.csv")): # cambialo a lo que estés usando como csv, parquet, rda, xlsx, etc
        lf = pl.scan_csv(
            f,
            separator=";", # cuando conoces tus bases, estableces tu estandar de trabajo
            encoding="utf8", # y defines tanto el separador, el encoding
            schema= schema) # como el schema
        lfs.append(lf)
    return pl.concat(lfs, how="diagonal", rechunk=False) 


# lectura directa, cuando el dataset no es tan masivo

def read_df(dir: Path = rutas_archivos):
    lfs = []
    for f in sorted(fixed_dir.glob("*.csv")): # cambialo a lo que estés usando como csv, parquet, rda, xlsx, etc
        lf = pl.raed_csv(
            f,
            separator=";", # cuando conoces tus bases, estableces tu estandar de trabajo
            encoding="utf8", # y defines tanto el separador, el encoding
            schema= schema) # como el schema
        lfs.append(lf)
    return pl.concat(lfs, how="diagonal", rechunk=False) 




