from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

load_dotenv()

ES_HOST = os.getenv('ELASTIC_HOST')
ES_INDEX = os.getenv('ELASTIC_INDEX')

es = Elasticsearch(
    ES_HOST,
    headers={"accept": "application/json", "content-type": "application/json"}
)

def create_index() -> None:
    if not es.indices.exists(index=ES_INDEX):
        es.indices.create(index=ES_INDEX, ignore=400)


def insert_data(data):
    for record in data:
        es.index(index=ES_INDEX, body=record)

