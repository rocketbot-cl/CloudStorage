# CloudStorage
  
Upload files to Cloud Storage  

*Read this in other languages: [English](Manual_CloudStorage.md), [Español](Manual_CloudStorage.es.md).*
  
![banner](imgs/Banner_cloudstorage.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Setup Google Cloud Storage credentials
  
Configure Cloud Storage credentials
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path|Google Cloud Storage credentials file path|C:\Usuario\Desktop\credentials.json|

### Upload file
  
Upload a file
|Parameters|Description|example|
| --- | --- | --- |
|File path|File path to upload|C:\Usuario\Desktop\file.png|
|Bucket name|The name of the bucket where the file will be uploaded|your-bucket-name|
|Blob name|The name of the blob where the file will be uploaded|your destination blob name|
|Timeout|Timeout of the request. If left empty, by default is 1000|1000|
