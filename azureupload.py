from azure.storage.blob import BlobService
import os

blob_service = BlobService(account_name='songanalysis', account_key=os.environ['AZUREKEY'])
blob_service.put_block_blob_from_path(
    'songs',
    'happy',
    'happy.mp3',
    x_ms_blob_content_type='mp3'
)