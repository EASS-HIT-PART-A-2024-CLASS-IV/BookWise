from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
import models
from routers.users import router as user_router
from routers.library import router as library_router
from sqlalchemy import MetaData

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)

@app.get("/")
async def root():
    return {"message": "running"}

@app.get("/check-db")
def check_db_connection():
    try:
        db = SessionLocal()
        db.execute("SELECT 1") 
        return {"message": "Database connection successful"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database connection error: {str(e)}"
        )
    finally:
        db.close()

# @app.get("/check-db-structure")
# def check_db_structure(db: Session = Depends(get_db)):
#     try:
#         engine = db.bind
#         metadata = MetaData(bind=engine)
#         metadata.reflect()
#         table_name = "users"
#         if table_name in metadata.tables:
#             table = metadata.tables[table_name]
#             columns_info = [
#                 {
#                     "name": column.name,
#                     "type": str(column.type),
#                     "nullable": column.nullable,
#                 }
#                 for column in table.columns
#             ]

#             return {"table_name": table_name, "columns": columns_info}
#         else:
#             return {"message": f"Table '{table_name}' not found in the database"}

#     except Exception as e:
#         raise HTTPException(
#             status_code=500, detail=f"Database connection error: {str(e)}"
#         )
#     finally:
#         db.close()

app.include_router(user_router)
app.include_router(library_router)
