from io import BytesIO
from typing import BinaryIO, cast


class ObjectResponse(BytesIO):
    def stream(self, chunk_size: int):
        while chunk := self.read(chunk_size):
            yield chunk

    def release_conn(self) -> None:
        pass


class InMemoryStorage:
    def __init__(self) -> None:
        self.objects: dict[str, bytes] = {}
        self.uploads: list[dict[str, object]] = []
        self.removed: list[str] = []

    def put_object(self, **kwargs: object) -> None:
        data = cast(BinaryIO, kwargs["data"])
        body = data.read()
        object_name = cast(str, kwargs["object_name"])
        self.objects[object_name] = body
        self.uploads.append({**kwargs, "body": body})

    def get_object(self, bucket_name: str, object_name: str) -> ObjectResponse:
        return ObjectResponse(self.objects[object_name])

    def remove_object(self, bucket_name: str, object_name: str) -> None:
        self.removed.append(object_name)
        self.objects.pop(object_name, None)
