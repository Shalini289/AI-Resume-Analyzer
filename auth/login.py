from database.crud import (
    get_user_by_email
)

from auth.password_hash import (
    verify_password
)

from auth.jwt_handler import (
    create_access_token
)


def login_user(
    db,
    email,
    password
):

    user = get_user_by_email(
        db,
        email
    )

    if not user:

        return {
            "success": False,
            "message":
            "User not found"
        }

    if not verify_password(
        password,
        user.password_hash
    ):

        return {
            "success": False,
            "message":
            "Invalid password"
        }

    token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email
        }
    )

    return {
        "success": True,
        "token": token
    }
