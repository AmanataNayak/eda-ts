import polars as pl
import pandas as pd
from io import BytesIO

def preprocess_data(file_content: bytes, file_type: str):
    if file_type == 'csv':
        df: pl.DataFrame = pl.read_csv(BytesIO(file_content))
    else:
        df: pl.DataFrame = pl.read_excel(BytesIO(file_content))

    # Ensure date time column is in ISO format
    df = df.with_columns(pl.col('effective_date').str.strptime(pl.Datetime, format='%Y-%m-%d %H:%M:%S'))

    # Convert cash column to float
    df = df.with_columns(pl.col('cash').cast(pl.Float64))

    # preprocess
    df = df.with_columns(pl.col('effective_date').dt.year().alias('year'))
    df = df.with_columns(pl.col('effective_date').dt.month().alias('month'))
    df = df.with_columns(pl.col('effective_date').dt.ordinal_day().alias('year_day'))
    df = df.with_columns(pl.col('effective_date').dt.day().alias('day'))
    df = df.with_columns(pl.col('effective_date').dt.quarter().alias('quarter'))
    df = df.with_columns(pl.col('effective_date').dt.week().alias('week'))  
    df = df.with_columns(pl.col('effective_date').dt.weekday().alias('weekday'))
    df = df.with_columns((pl.col('year').cast(pl.Utf8) + '-' + pl.col('quarter').cast(pl.Utf8)).alias('year_quarter'))

    df = df.with_columns(pl.col('effective_date').cast(pl.Utf8).str.to_datetime().dt.strftime('%Y-%m-%d %H:%M:%S'))

    return df.to_pandas().to_dict(orient='records')