import os
import shutil

def image_upload(source, destination):
    shutil.copy(source, destination)

source = os.getenv('IMAGE_SOURCE')
destination = os.getenv('IMAGE_DESTINATION')

image_upload(source, destination)