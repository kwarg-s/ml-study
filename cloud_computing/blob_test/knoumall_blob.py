import os
from azure.storage.blob import BlobServiceClient

try:
  print("한국방송통신대학교 클라우드 컴퓨팅 Blob 파일 업로드")
  connect_str = "DefaultEndpointsProtocol=https;AccountName=knoublobstorage218;AccountKey=QGcPvELtvvwWnVkVZi4SwdfJ0Xhl3KZBR+X0PB84Fm/jh3V429tP/2uCPmJ4NGsrnU06Qj9mRcZE+AStwQJWJg==;EndpointSuffix=core.windows.net"
  blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  container_name = "knoublobcontainer"

  local_file_name = "main_carousel.png" 

  container_client = blob_service_client.get_container_client(container=container_name)

  print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
  with open(file=os.path.join('', local_file_name), mode="rb") as data:
    blob_client = container_client.upload_blob(name=local_file_name, data=data, overwrite=True)
  
except Exception as ex: 
  print('Exception:') 
  print(ex)