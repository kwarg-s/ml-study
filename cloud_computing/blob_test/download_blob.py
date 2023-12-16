import os
from azure.storage.blob import BlobServiceClient

try:
  print("한국방송통신대학교 클라우드 컴퓨팅 Blob 파일 다운로드")
  connect_str = "DefaultEndpointsProtocol=https;AccountName=knoublobstorage218;AccountKey=QGcPvELtvvwWnVkVZi4SwdfJ0Xhl3KZBR+X0PB84Fm/jh3V429tP/2uCPmJ4NGsrnU06Qj9mRcZE+AStwQJWJg==;EndpointSuffix=core.windows.net"
  blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  container_name = "knoublobcontainer"

  remote_file_name = "main_carousel.png" 
  local_file_name = "main_carousel_down.png"

  blob_client = blob_service_client.get_blob_client(container=container_name, blob=remote_file_name)

  print("\nDownloading blob from Azure Storage:\n\t" + remote_file_name)

  with open(file=os.path.join('', local_file_name), mode="wb") as download_blob:
        download_stream = blob_client.download_blob()
        download_blob.write(download_stream.readall())

except Exception as ex: 
  print('Exception:')
  print(ex)