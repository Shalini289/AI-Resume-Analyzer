from auth.jwt_handler import (
    create_access_token,
    verify_token
)


def test_token():

    token = create_access_token(
        {
            "user_id": 1
        }
    )

    payload = verify_token(
        token
    )

    assert payload[
        "user_id"
    ] == 1