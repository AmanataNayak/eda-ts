# **Timeseries EDA**

This project allows users to upload CSV or Excel files via an API, preprocesses the data using **Polars**, stores it in **Elasticsearch**, and visualizes it using **Kibana**. It is built with **FastAPI** for the backend.

---

## **Features**
- **File Upload**: Users can upload CSV or Excel files via an API endpoint.
- **Data Preprocessing**: The data is preprocessed using Polars (e.g., filtering, datetime conversion).
- **Elasticsearch Integration**: Processed data is indexed in Elasticsearch for efficient querying.
- **Kibana Visualization**: Data can be visualized using Kibana dashboards.

---

## **Technologies Used**
- **FastAPI**: For building the API.
- **Polars**: For fast and efficient data preprocessing.
- **Elasticsearch**: For storing and indexing data.
- **Kibana**: For data visualization.
- **Python Libraries**:
  - `fastapi`
  - `polars`
  - `elasticsearch`
  - `python-multipart`

---

## **Setup and Installation**

### **1. Prerequisites**
- Python 3.11+
- Elasticsearch and Kibana installed and running locally or in a Docker container.

### **2. Install Dependencies**
Clone the repository and install the required Python packages:
```bash
git clone https://github.com/AmanataNayak/eda-ts.gitˇ
cd eda-ts
pip install -r requirements.txt
```

### **3. Run Elasticsearch and Kibana**
Start Elasticsearch and Kibana using Docker or locally:
```bash
# Using Docker
docker compose up -d
```

### **4. Run the FastAPI App**
Start the FastAPI application:
```bash
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

---

## **API Endpoints**

### **1. Upload File**
- **Endpoint**: `POST /upload/`
- **Description**: Upload a CSV or Excel file for processing.
- **Request**:
  - File: CSV or Excel file (form-data).
- **Response**:
  - Success: `{"message": "File uploaded and processed successfully!"}`
  - Error: `{"error": "Unsupported file format. Please upload a CSV or Excel file."}`

---

## **Data Preprocessing**
The uploaded data is preprocessed using Polars:
1. Ensure the file contains `cash` and `effective_date` columns.
2. Convert the `effective_date` column to a proper datetime format.

---

## **Elasticsearch Integration**
Processed data is sent to Elasticsearch and indexed under the `cash_data` index. You can query and visualize this data in Kibana.

---

## **Kibana Visualization**
1. Open Kibana at `http://localhost:5601`.
2. Go to saved object section and import `es/eda.ndjson` file.
3. Go to **Discover** and select the `cash_data` index.

---

## **Project Structure**
```
.
├── main.py                # FastAPI application entry point
├── requirements.txt       # Python dependencies
├── docker-compose.yml     # Docker setup for Elasticsearch and Kibana
├── .gitignore             # Files and directories to ignore in Git
├── env/                   # Virtual environment (if used)
├── preprocessors/         # Data preprocessing scripts
│   ├── __init__.py        # Initialization file for the preprocessors module
│   └── preprocess.py      # Preprocessing logic using Polars
├── es_utils.py            # Utility functions for Elasticsearch integration
├── eda.ndjson             # Example data file (optional)
├── init__.py               # Initialization file (if needed)
```

---

## **Example Workflow**
1. Upload a CSV or Excel file to the `/upload/` endpoint.
2. The data is preprocessed and sent to Elasticsearch.
3. Visualize the data in Kibana.

