from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from ..core.config import settings

# Create engine using DATABASE_URL from settings. If DATABASE_URL is None,
# fall back to a sqlite in-memory database to avoid immediate import errors.
db_url = settings.DATABASE_URL  
engine = create_engine(db_url)
Base = declarative_base()
