from app.utils.core import slugify
from pydantic import BaseModel, ConfigDict, computed_field


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    reputation: int = 0
    universal_privilege_level: str = "normal"
    is_superuser: bool = False

    @computed_field  # type: ignore
    @property
    def encrypted_id(self) -> str:
        from app.utils.auth import encrypt_id

        return f"{encrypt_id(self.id)}"

    @computed_field  # type: ignore
    @property
    def slug(self) -> str:
        return slugify(self.username)

class UserPrivate(User):
    hashed_password: str

