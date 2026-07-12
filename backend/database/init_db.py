from backend.database.connection import Base, engine

import backend.models.upload_model

Base.metadata.create_all(bind=engine)

print("Database Created Successfully")