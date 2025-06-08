# Currency ETL Pipeline with Apache Airflow, Docker, and PostgreSQL

This project is an end-to-end ETL pipeline that fetches live currency exchange rates from a public API, transforms the data, and loads it into PostgreSQL using **Airflow**, **Docker**, and **Python**.

---

## Tech Stack

- PostgreSQL
- Docker + Docker Compose
- Apache Airflow 2.8.1
- Python 3.9
- API: [https://open.er-api.com](https://open.er-api.com)

---

## How to Run

### 1. Prerequisites

- Docker Desktop
- Python 3.9+
- Open ports: 5432, 8080

### 2. Clone & Start

```bash
git clone https://github.com/yourusername/currency_etl_project.git
cd currency_etl_project
docker compose up --build