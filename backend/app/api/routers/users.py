from app.api.dependencies.auth import validate_is_authenticated
from app.api.dependencies.core import DBSessionDep
from app.crud.user import get_user
from app.schemas.user import User
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/{user_id}",
    response_model=User,
    dependencies=[Depends(validate_is_authenticated)],
)
async def user_details(
    user_id: int,
    db_session: DBSessionDep,
):
    """
    Get any user details
    """
    user = await get_user(db_session, user_id)
    return user