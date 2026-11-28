from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.organizations.models import Organization


def test_create_and_retrieve_organization(db_session: Session):
    slug = f"test-org-{uuid4().hex}"

    organization = Organization(
        name="HONEST DIMENSIONS Test Organization",
        slug=slug,
    )

    db_session.add(organization)
    db_session.flush()

    organization_id = organization.id

    retrieved_organization = db_session.scalar(
        select(Organization).where(
            Organization.id == organization_id
        )
    )

    assert retrieved_organization is not None
    assert retrieved_organization.name == (
        "HONEST DIMENSIONS Test Organization"
    )
    assert retrieved_organization.slug == slug
    assert retrieved_organization.is_active is True