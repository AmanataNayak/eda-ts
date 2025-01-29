import pytest
from io import BytesIO
import polars as pl

from prerpocessors.preprocess import preprocess_data

@pytest.fixture
def csv_file_content():
    data = """effective_date,cash
2023-01-01 12:00:00,100.0
2023-02-01 13:00:00,200.0
"""
    return data.encode('utf-8')

@pytest.fixture
def excel_file_content():
    df = pl.DataFrame({
        'effective_date': ['2023-01-01 12:00:00', '2023-02-01 13:00:00'],
        'cash': [100.0, 200.0]
    })
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    return buffer.getvalue()

def test_preprocess_data_csv(csv_file_content):
    result = preprocess_data(csv_file_content, 'csv')
    expected = [
        {'effective_date': '2023-01-01 12:00:00', 'cash': 100.0, 'year': 2023, 'month': 1, 'year_day': 1, 'day': 1, 'quarter': 1, 'week': 52, 'weekday': 6, 'year_quarter': '2023-1'},
        {'effective_date': '2023-02-01 13:00:00', 'cash': 200.0, 'year': 2023, 'month': 2, 'year_day': 32, 'day': 1, 'quarter': 1, 'week': 5, 'weekday': 2, 'year_quarter': '2023-1'}
    ]
    assert result == expected

def test_preprocess_data_excel(excel_file_content):
    result = preprocess_data(excel_file_content, 'excel')
    expected = [
        {'effective_date': '2023-01-01 12:00:00', 'cash': 100.0, 'year': 2023, 'month': 1, 'year_day': 1, 'day': 1, 'quarter': 1, 'week': 52, 'weekday': 6, 'year_quarter': '2023-1'},
        {'effective_date': '2023-02-01 13:00:00', 'cash': 200.0, 'year': 2023, 'month': 2, 'year_day': 32, 'day': 1, 'quarter': 1, 'week': 5, 'weekday': 2, 'year_quarter': '2023-1'}
    ]
    assert result == expected