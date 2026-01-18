

import subprocess
from sqlmodel import Session, create_engine
from app.settings import config


DATABASE_URL = f"postgresql://{config.db_user}:{config.db_password}@{config.db_host}/{config.db_name}"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
        
def setup_db():
    
    subprocess.run(['poetry', 'run', 'alembic', 'upgrade', 'head'])