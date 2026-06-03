# database.py

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# --- DATABASE_URL = os.getenv("DATABASE_URL") --- > internal render
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://hamego_creation_user:g4AZ5Y4fbKpU5AGLc8PpbfLqSmrFSbWq@dpg-d7mdtopf9bms73fv3nn0-a.singapore-postgres.render.com/hamego_creation"
)


if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql://",
        1
    )

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    future=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()