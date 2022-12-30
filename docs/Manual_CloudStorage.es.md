# CloudStorage
  
Cargar archivos en Cloud Storage 


  
![banner](imgs/Banner_cloudstorage.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Configurar credenciales Google Cloud Storage
  
Configura credenciales de Cloud Storage
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales|Ruta del archivo de credenciales de Google Cloud Storage|C:\Usuario\Desktop\credentials.json|

### Subir archivo
  
Sube un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo|Ruta del archivo a subir|C:\Usuario\Desktop\file.png|
|Bucket name|El nombre del bucket donde se subira el archivo|your-bucket-name|
|Blob name|El nombre del blob donde se subira el archivo|your destination blob name|
|Timeout|Timeout de la peticion. Si se deja vacio, por defecto es 1000|1000|
