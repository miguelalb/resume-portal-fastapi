import logging

import pytest
from app.config import get_settings
from app.crud import (
    create_user,
    get_user_by_username,
    promote_user,
    upgrade_user_to_premium,
)
from app.dependencies import get_db
from app.main import create_application
from app.models import Base
from app.schemas import UserCreate
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = get_settings()

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_TEST_URI

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down


@pytest.fixture(scope="module")
def superuser():
    db = TestingSessionLocal()
    user_creds = UserCreate(username="admin", password="admin")
    superuser = get_user_by_username(db, user_creds.username)
    if superuser is None:
        user = create_user(db, user_creds)
        promote_user(db, user.id)
        upgrade_user_to_premium(db, user.id)
    return user_creds


@pytest.fixture(scope="module")
def access_token(superuser, test_app):
    response = test_app.post(
        f"/auth/login?username={superuser.username}&password={superuser.password}",
        headers={"accept": "application/json"},
        data="",
    )
    tokens = response.json()
    logging.info("Getting access token")
    logging.info("Access token:", tokens["access_token"])

    return tokens["access_token"]


@pytest.fixture(scope="module")
def auth_headers(access_token):
    return {"token": f"{access_token}"}
