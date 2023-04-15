from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
import base64
from io import BytesIO
from graphene_file_upload.scalars import Upload
import graphene

class UploadImage(graphene.Mutation):
    class Arguments:
        image = Upload()

    url = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, image):
        # Convert base64-encoded string to image file
        format, imgstr = image.split(';base64,')
        ext = format.split('/')[-1]
        image_data = BytesIO(base64.b64decode(imgstr))
        image_file = InMemoryUploadedFile(image_data, None, 'image.jpg', 'image/jpeg', image_data.getbuffer().nbytes, None)
        saved_file_name = default_storage.save(image_file.name, image_file)
        url = default_storage.url(saved_file_name)

        return UploadImage(url=url, success=True)
