from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    slug: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False

class UserPrivate(User):
    hashed_password: str

