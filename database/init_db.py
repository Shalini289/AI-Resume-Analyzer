from database.postgres import (
    Base,
    engine
)

from database.models import *

Base.metadata.create_all(
    bind=engine
)

print(
    "Database tables created successfully."
)