from fastapi import FastAPI, UploadFile, File, HTTPException
from contextlib import asynccontextmanager
from prerpocessors.preprocess import preprocess_data
from es.es_utils import create_index, insert_data
import logging

logger = logging.getLogger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_index()
    yield

app = FastAPI(lifespan=lifespan)

@app.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    if file.filename.endswith('.csv'):
        file_type: str = 'csv'
    elif file.filename.endswith(('.xls', '.xlsx')):
        file_type: str = 'excel'
    else:
        raise HTTPException(status_code=400, detail='Invalid file format')
    

    content: bytes = await file.read()

    process_data = preprocess_data(content, file_type)

    insert_data(process_data)

    return {'message': 'Data Uploaded succesfully', 'record': len(process_data)}
