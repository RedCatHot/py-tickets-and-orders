from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


def create_user(
        username: str,
        password: str,
        **kwargs
) -> None:
    new_user = get_user_model().objects.create_user(
        username=username,
        password=password
    )

    for attr, value in kwargs.items():
        if attr in ["email", "first_name", "last_name"]:
            setattr(new_user, attr, value)
    new_user.save()


def get_user(user_id: int) -> User:
    return get_user_model().objects.get(id=user_id)


def update_user(
        user_id: int,
        password: str = None,
        **kwargs
) -> None:
    user = get_user_model().objects.get(id=user_id)
    if password:
        user.set_password(password)

    for attr, value in kwargs.items():
        if attr in [
            "email", "first_name", "last_name", "username", "password"
        ]:
            setattr(user, attr, value)
    user.save()
