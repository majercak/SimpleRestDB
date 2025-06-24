import pytest
from app import models

TEST_USER = {"name": "Test User", "email": "test@example.com", "phone_number": "123-456-7890"}


@pytest.mark.asyncio
async def test_create_and_read_user(db_session):
    new_user = models.User(**TEST_USER)
    db_session.add(new_user)
    await db_session.commit()

    result = await db_session.get(models.User, new_user.id)
    assert result is not None
    assert result.email == TEST_USER["email"]
