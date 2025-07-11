from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings #loads DATABASE_URL from .env

#Read DATABASE_URL from env
DATABASE_URL=settings.DATABASE_URL

# create async engine
engine= create_async_engine(DATABASE_URL,echo=True)

#create async session factory

AsyncSessionLocal= sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

#dependency function to inject DB session

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


