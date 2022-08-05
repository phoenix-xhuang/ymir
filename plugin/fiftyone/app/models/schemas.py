from pathlib import Path
from typing import List

from loguru import logger
from pydantic import BaseModel, Field, validator

from conf.configs import conf
from utils.constants import FiftyoneTaskStatus
from utils.errors import FiftyOneResponseCode


class DataSet(BaseModel):
    name: str = Field(...)
    data_dir: str = Field(...)

    @validator("data_dir")
    def check_dir(cls, v):
        base_path = Path(conf.base_path)
        if Path.exists(base_path / v):
            return v
        logger.error(f"{v} does not exist")
        raise ValueError(f"{v} is not a valid directory")

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "ymir_data233",
                "data_dir": "ymir-workplace/voc",
            }
        }


class Task(BaseModel):
    tid: str
    datas: List[DataSet]


class BaseResponse(BaseModel):
    code: int = FiftyOneResponseCode.FO_OK
    error: str = ""

    class Config:
        schema_extra = {
            "example": {
                "code": FiftyOneResponseCode.FO_OK,
                "error": "",
            }
        }


class TaskCreateBody(BaseModel):
    tid: str = ""


class TaskCreateResponse(BaseResponse):
    data: TaskCreateBody = TaskCreateBody()


class TaskQueryBody(BaseModel):
    status: int = FiftyoneTaskStatus.PENDING.value
    url: str = ""


class TaskQueryResponse(BaseResponse):
    data: TaskQueryBody = TaskQueryBody()


class TaskDeleteResponse(BaseResponse):
    data: dict = {}


class ErrorResponse(BaseResponse):
    data: dict = {}