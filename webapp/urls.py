from fastapi import APIRouter
from fastapi import status

from .views import downloader_app
from .views import error
from .views import index

web_route = APIRouter(include_in_schema=False)

web_route.add_api_route(
    "/",
    endpoint=index,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    summary="Index page",
    tags=["web"],
    name="index",
)

web_route.add_api_route(
    "/",
    endpoint=downloader_app,
    methods=["POST"],
    status_code=status.HTTP_200_OK,
    summary="Index page",
    tags=["web"],
    name="index",
)

web_route.add_api_route(
    "/error",
    endpoint=error,
    status_code=status.HTTP_200_OK,
    summary="Error page",
    tags=["web"],
    name="error",
)
