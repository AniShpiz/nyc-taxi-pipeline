# NYC Taxi Data Engineering Project

An end-to-end data pipeline project that ingests, processes, and analyzes NYC Yellow Taxi trip data using Python, PySpark, PostgreSQL, and Power BI.

## 🚀 Current Features
- Python script to download taxi data (.parquet)
- Git structure with `.gitignore` to exclude large files
- Folder structure ready for staging, warehousing, and dashboarding

## 📁 Folder Structure
```
scripts/           # Python scripts (e.g., data download)
data/              # Raw data files (ignored by Git)
notebooks/         # Colab notebooks
dashboard/         # Power BI dashboards (published version)
diagrams/          # System architecture visuals
```

## 🛠 Tech Stack
- Python + Pandas
- Databricks (Community Edition)
- PostgreSQL or DuckDB
- Power BI
- Git + GitHub

## 📈 Upcoming Work
- Data cleaning & transformation with PySpark
- Data loading into PostgreSQL
- Power BI dashboard embedded on portfolio site
- Optional: Orchestration with Airflow or Prefect

## 📦 Dataset
Data is sourced from the official [NYC Taxi TLC Trip Records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## 📂 Notes
Raw data files are not included in the repository and must be downloaded via the provided script:
```bash
python scripts/download_data.py
```