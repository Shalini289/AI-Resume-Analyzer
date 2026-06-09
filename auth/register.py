from database.crud import (
    create_user,
    get_user_by_email
)

from auth.password_hash import (
    hash_password
)


def register_user(
    db,
    name,
    email,
    password
):

    existing_user = get_user_by_email(
        db,
        email
    )

    if existing_user:

        return {
            "success": False,
            "message":
            "User already exists"
        }

    password_hash = hash_password(
        password
    )

    user = create_user(
        db,
        name,
        email,
        password_hash
    )

    return {
        "success": True,
        "user_id": user.id
    }