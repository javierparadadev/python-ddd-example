import base64

from fastapi import UploadFile


async def bytify_upload_file(file: UploadFile) -> bytes:
    data = await file.read()
    base64_data = base64.b64encode(data)
    bytes_data = base64.decodebytes(base64_data)
    return bytes_data
