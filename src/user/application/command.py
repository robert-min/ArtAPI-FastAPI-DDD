from fastapi import UploadFile
from sqlalchemy.orm import Session
from src.user.domain.entity import (
    FileInfo,
    OriginImageInfo,
    MainContent, 
    ContentName
    )
from src.shared_kernel.domain.exception import DBError
from src.user.domain.service.insert_image import InsertImageService
from src.user.infra.database.repository import UserRepository
from src.user.domain.exception import UserServiceError, UserApplicationError
from src.user.domain.errorcode import InsertImageError, GetContentError


class UserCommandUseCase:
    def __init__(
            self,
            mongo_session: any = None,
            postgre_session: Session = None,
            azure_blob_session: Session = None
    ) -> None:
        self.mogno_session = mongo_session
        self.postgre_session = postgre_session
        self.azure_blob_session = azure_blob_session

    async def insert_image(
            self, id: str, file: UploadFile
    ) -> FileInfo:
        try:
            # convert request to entity
            origin_image = OriginImageInfo(
                id=id,
                image_file=file.file.read()
            )

            # find image_name
            file_info = await InsertImageService().insert_image(origin_image)

            return file_info
        except UserServiceError as e:
            raise e
        except Exception as e:
            raise UserApplicationError(
                **InsertImageError.UnknownError.value, err=e)

    async def get_main_content(
            self, generated_id: str
    ) -> MainContent:
        try:
            # load content
            content_name = ContentName(image_name=generated_id)
            image_content = UserRepository.get_origin_image(
                self.azure_blob_session, content_name
            )
            text_content = UserRepository.get_text_content(
                self.mogno_session, content_name
            )
            audio_content = UserRepository.get_audio_content(
                self.azure_blob_session, content_name
            )

            return MainContent(
                resize_image=image_content.data,
                text_content=text_content.data.decode(),
                audio_content=audio_content.data
            )
        except DBError as e:
            raise e
        except Exception as e:
            raise UserApplicationError(
                **GetContentError.UnknownError.value, err=e)
