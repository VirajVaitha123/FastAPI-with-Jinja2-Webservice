"""
Functions to help work with Azure Blob Storage
"""
# Author: Viraj Vaitha

# Import Libaries
from typing import BinaryIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from ..responses.reponses_json import response_json
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv()
connect_str = os.getenv('AZURE_CONNECTION_STRING')

# Parameters
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Upload contents to blob storage
def upload_blob(filename:str, container:str, data: BinaryIO) -> response_json:
    """
    Parameters
    ----------
    filename : string defining the name of the file to be shown in azure blob storage
    container: string defining the name of the container in Azure to store the file
    data: information in the form of BinaryIO can be uploaded to Azure Blob Storage
    Returns
    -------
    response_json: json message with a relevant status message
    """

    try:
        blob_client = blob_service_client.get_blob_client(
            container=container, blob=filename)

        blob_client.upload_blob(data)
        return response_json(message = "success", status = 200 )

    except Exception as e:
        return response_json(message = e.message, status = 500)
        
