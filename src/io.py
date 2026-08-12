from pathlib import Path
from typing import Literal

import polars as pl

from config import raw_dir, schema

Extension = Literal["csv", "parquet"]

# lectura lazy, usualmente para bases grandes

def lazy(dir: Path = raw_dir, ext: Extension = "csv") -> pl.LazyFrame:
    """
    cargar datos de forma lazy siguiendo la ruta en src/config.py
    ext: extension de los archivos a cargar ("csv" o "parquet")
    """
    lfs = []
    for f in sorted(dir.glob(f"*.{ext}")):
        if ext == "csv":
            lf = pl.scan_csv(
                f,
                separator=";",   # cuando conoces tus bases, estableces tu estandar de trabajo
                encoding="utf8", # y defines tanto el separador, el encoding
                schema=schema)   # como el schema
        elif ext == "parquet":
            lf = pl.scan_parquet(f)  # parquet ya trae su propio schema, no hace falta declararlo
        else:
            raise ValueError(f"extension no soportada: {ext}")
        lfs.append(lf)
    return pl.concat(lfs, how="diagonal", rechunk=False)


# lectura directa, cuando el dataset no es tan masivo

def eager(dir: Path = raw_dir, ext: Extension = "csv") -> pl.DataFrame:
    """
    cargar datos de forma directa (eager) siguiendo la ruta en src/config.py
    ext: extension de los archivos a cargar ("csv" o "parquet")
    """
    dfs = []
    for f in sorted(dir.glob(f"*.{ext}")):
        if ext == "csv":
            df = pl.read_csv(f, separator=";", encoding="utf8", schema=schema)
        elif ext == "parquet":
            df = pl.read_parquet(f)
        else:
            raise ValueError(f"extension no soportada: {ext}")
        dfs.append(df)
    return pl.concat(dfs, how="diagonal", rechunk=False)



# el caso que viene es un ejemplo de reutilizacion de codigo para la version "eager"
# y es ciertamente más eficiente en memoria, queda al lector investigar por si le interesa

#def eager(dir: Path = raw_dir, ext: Extension = "csv") -> pl.DataFrame:
#    """
#    cargar datos de forma directa siguiendo la ruta en src/config.py
#    ext: extension de los archivos a cargar ("csv", "parquet", etc.)
#    """
#    return lazy(dir, ext).collect()
