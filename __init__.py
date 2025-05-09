# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

   sudo pip install <package> -t .

"""
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "CloudStorage" + os.sep + "libs" + os.sep
sys.path.append(cur_path)

from google.oauth2 import service_account
from google.cloud import storage

global credentials
module = GetParams("module")

if module == "setCredentials":
    credentials_path = GetParams("credentials_path")
    try:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
    
if module == "uploadFile":
    source_file_name = GetParams("file_path")  # Puede ser archivo, lista de archivos, o carpeta
    bucket_name = GetParams("bucket_name")
    destination_blob_name = GetParams("destination_blob_name")  # Puede ser nombre único o carpeta destino
    timeout = GetParams("timeout")
    if not timeout:
        timeout = 1000

    try:
        storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        if os.path.isdir(source_file_name):
            # Subir todos los archivos de la carpeta
            for root, _, files in os.walk(source_file_name):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, start=source_file_name)
                    blob_path = os.path.join(destination_blob_name, rel_path).replace("\\", "/")
                    blob = bucket.blob(blob_path)
                    blob.chunk_size = 5 * 1024 * 1024
                    blob.upload_from_filename(full_path, timeout=int(timeout))
                    print("File {} uploaded to {}.".format(full_path, blob_path))
        else:
            # Carga múltiple por coma
            source_list = [x.strip() for x in source_file_name.split(',')]
            destination_list = [x.strip() for x in destination_blob_name.split(',')] if destination_blob_name else []

            if len(destination_list) == 1 and len(source_list) > 1:
                destination_list = [destination_list[0]] * len(source_list)

            if destination_list and len(source_list) != len(destination_list):
                raise ValueError("La cantidad de archivos y nombres de destino no coincide.")

            for i, src in enumerate(source_list):
                dst = destination_list[i] if destination_list else os.path.basename(src)
                blob = bucket.blob(dst)
                blob.chunk_size = 5 * 1024 * 1024
                blob.upload_from_filename(src, timeout=int(timeout))
                print("File {} uploaded to {}.".format(src, dst))

    except Exception as e:
        print("\x1B[31;40mAn error occurred\x1B[0m")
        PrintException()
        raise e