# about datasets

En algunas ocasiones los datasets no vendrán limpios o entendibles y mucho menos se podrá entender cómo cargarlos o dónde tenerlos, lo que nos puede resultar en un desorden que al volver despues de una pausa no podamos entender que estabamos haciendo, por esa razon es bueno tener estructurado donde están y estarán nuestros datos.

```bash
├── datasets
│   ├── processed/ #<- procesado, terminado, exportable. paso final de ETL
│   ├── raw/ #<- sin procesar, original, backup. origen del ETL
│   └── README.md
```

> ETL: Extract, Transform, Load

- `raw`: son los datos originales, solo cargar y no modificar estos archivos
- `processed`: es la carpeta donde termina el ETL

>nota: `.gitkeep` solo es auxiliar ya que git no sube carpetas vacias 

# about ETL

Se trata del proceso completo desde buscar y extraer los datos (e.g.`csv`, `xlsx`, `db`), procesarlos y guardarlos en un formato para poder trabajarlos después (e.g. `rda`, `parquet`, `avro`, `orc` ,`db`, etc), la razon del porque cambiar de un formato a otro viene justificado más de la capacidad de nuestro equipo de trabajo y del contexto. 

Por ejemplo, para procesar millones de filas no suele ser común (ni óptimo) usar `csv` o `xlsx` debido a las limitaciones que tienen pero si por el contrario nuestro trabajo es usar una base pequeña en `csv` y devolver un `csv` no vamos a matar una hormiga con una bazuka por lo que depende del contexto y a la pregunta que respondemos

>nota: en algunas ocasiones se trabajará en la nube y nuestro equipo tendra casi cero relevancia en la decisión de usar el formato 
