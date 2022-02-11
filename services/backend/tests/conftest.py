import pytest
from app.config import get_settings
from app.dependencies import get_db
from app.main import create_application
from app.models import Base
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
