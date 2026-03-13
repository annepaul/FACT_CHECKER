import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# 1. Setup the Engine
# Format: postgresql://username:password@localhost:5432/db_name
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Define the Model
class FactCheck(Base):
    __tablename__ = "fact_checks"

    id = Column(Integer, primary_key=True, index=True)
    claim = Column(String(500), nullable=False)
    verdict = Column(String(50), nullable=False)
    reasoning = Column(Text, nullable=False)
    # We store the raw evidence as a Text block for the POC
    evidence_data = Column(Text, nullable=True) 
    created_at = Column(DateTime, default=datetime.utcnow)

# 3. Helper functions
def init_db():
    Base.metadata.create_all(bind=engine)

def save_fact_check(claim, verdict, reasoning, evidence):
    db = SessionLocal()
    try:
        new_entry = FactCheck(
            claim=claim,
            verdict=verdict,
            reasoning=reasoning,
            evidence_data=evidence
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return new_entry
    except Exception as e:
        print(f"Error saving to DB: {e}")
        db.rollback()
    finally:
        db.close()