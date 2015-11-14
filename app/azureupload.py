from azure.storage.blob import BlobService
import os

blob_service = BlobService(account_name='songanalysis', account_key=os.environ['AZUREKEY'])
blob_service.put_block_blob_from_path(
    'songs',
    '10_happy',       # number before the song emotion corresponds to 'sentValue' from songdictionary.py. 10 = 1.0, 08 = 0.8, etc.
    '10_happy.mp3',
    x_ms_blob_content_type='mp3'
)