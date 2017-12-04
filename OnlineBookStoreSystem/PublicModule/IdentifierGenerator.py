import uuid
import base64


def uuid_generator():
    return uuid.uuid1()


def base64_uuid_generator():
    return bytes.decode(base64.b64encode(uuid.uuid1().bytes))
