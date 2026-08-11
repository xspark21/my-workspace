from typing import overload
import polars as pl


@overload
def info_col(data: pl.DataFrame, col: str) -> pl.Series: ...
@overload
def info_col(data: pl.LazyFrame, col: str) -> pl.Series: ...
def info_col(data: pl.DataFrame | pl.LazyFrame, col: str) -> pl.Series:
    """
    Valores únicos de una columna (ordenados), acepta DataFrame o LazyFrame.
    
    Sirve para explorar y reconocer.
    """
    lf = data.lazy() if isinstance(data, pl.DataFrame) else data
    return lf.select(pl.col(col).unique().sort()).collect().to_series()


def info_schema(data: pl.DataFrame | pl.LazyFrame) -> pl.DataFrame:
    """Esquema como tabla"""
    schema = data.collect_schema()
    return pl.DataFrame({
        "Columna": schema.names(),
        "Tipo": [str(t) for t in schema.dtypes()],
    })


@overload
def info(data: pl.DataFrame) -> pl.DataFrame: ...
@overload
def info(data: pl.LazyFrame) -> pl.DataFrame: ...
def info(data: pl.DataFrame | pl.LazyFrame) -> pl.DataFrame:
    """
    Resumen de columnas: tipo, nulos y valores únicos.
    Acepta DataFrame o LazyFrame
    """
    lf = data.lazy() if isinstance(data, pl.DataFrame) else data
    schema = lf.collect_schema()
    cols = schema.names()
    exprs = []
    for col in cols:
        exprs.append(pl.col(col).null_count().alias(f"{col}__nulos"))
        exprs.append(pl.col(col).n_unique().alias(f"{col}__unicos"))
    metrics = lf.select(exprs).collect()
    return pl.DataFrame({
        "Columna": cols,
        "Tipo": [str(t) for t in schema.dtypes()],
        "Nulos": [metrics[f"{c}__nulos"][0] for c in cols],
        "Unicos": [metrics[f"{c}__unicos"][0] for c in cols],
    })


def show(
    data: pl.DataFrame | pl.LazyFrame | pl.Series,
    nf: int = 15,
    nc: int = 10,
) -> None:
    """
    Args:
        data: DataFrame o Series
        nf: numero de filas a mostrar
        nc: numero de columnas a mostrar
    Imprime un DataFrame o Series, truncado a nf filas y nc columnas.
    """
    if isinstance(data, pl.LazyFrame):
        data = data.head(nf).collect()
    
    with pl.Config(tbl_rows=nf, tbl_cols=nc):
        print(data)
