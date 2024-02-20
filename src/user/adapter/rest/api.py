from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from fastapi import APIRouter, UploadFile, File, Header, Depends
from src.user.application.command import UserCommandUseCase
from src.user.application.demo import UserCommandDemo
from src.user.adapter.rest.response import SignUpUserResponse
from src.user.adapter.rest.request import GeneratedContentRequest
from src.shared_kernel.infra.database.connection import (
    MongoManager,
    PostgreManager
)

user = APIRouter(prefix="/user")


@user.post('/image')
async def insert_image(
    id: str = Header(),
    token: str = Header(),
    file: UploadFile = File(...),
):
    command = UserCommandUseCase()
    result = command.insert_image(id, file)
    return SignUpUserResponse(file_info=result).build()


@user.post('/content')
async def generate_content(
    request: GeneratedContentRequest,
    id: str = Header(),
    token: str = Header(),
    mogno_session: any = Depends(MongoManager.get_session),
    postgre_session: Session = Depends(PostgreManager.get_session)
):
    command = UserCommandUseCase(mogno_session, postgre_session)
    return StreamingResponse(command.generate_content(id, request),
                             media_type="text/event-stream")


@user.post('/image/demo')
async def demo_insert_image(
    id: str = Header(),
    token: str = Header(),
    file: UploadFile = File(...),
):
    command = UserCommandDemo()
    result = command.demo_insert_image(id, file)
    return SignUpUserResponse(file_info=result).build()


@user.post('/content/demo')
async def demo_generate_content(
    id: str = Header(),
    token: str = Header(),
    generated_id: str = "demo"
):
    command = UserCommandDemo()
    return StreamingResponse(command.demo_generate_content(generated_id),
                             media_type="text/event-stream")
