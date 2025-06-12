# s3-supplier-pipeline

A modular ETL pipeline for cleaning monthly supplier purchase reports for a real Wholesale & Retail Company based in Spain. Outputs clean data for loading into PostgreSQL and performing supplier analysis, purchasing trend reports, and business planning.

---

## Table of Contents
- [Overview](#overview)
- [Business Context](#business-context)
- [Raw Report Structure](#raw-report-structure)
- [ETL Architecture](#etl-architecture)
- [Setup & Usage](#setup--usage)
- [Project Structure](#project-structure)

---

## Overview

This pipeline processes real monthly CSV reports issued by a Cooperative. Each report compares purchase totals from the same month across two years and two channels: warehouse and direct supplier.

The result is a unified, clean CSV ready for analysis or loading into a PostgreSQL database.

---

## Business Context

The purchaser is a mid-sized Retail & Wholesale company (Spain, ~€2M/year). Each month, they receive a report comparing purchases made via:

- **Warehouse**: more expensive, but faster and combines suppliers.
- **Direct**: cheaper, slower, and comes with annual bonuses.

Clean data helps answer questions like:
- Are we ordering more via direct or warehouse this year?
- Which suppliers dropped in volume compared to last year?
- Is our bonus-earning potential increasing?

---

## Raw Report Structure

Each row represents a single supplier. The columns include purchase accumulations across two years and multiple channels:

| Column Name              | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `PROVEEDOR`              | Supplier name.                                                              |
| `Acum. Almacén 2024`     | Purchases from the warehouse in X month of current year in €                |
| `Acum. Directo 2024`     | Direct purchases in X month of current year in €                            |
| `Acum. Almacén 2023`     | Purchases from the warehouse in X month of previous year in €               |
| `Acum. Directo 2023`     | Direct purchases in X month of previous year in €                           |

*Example:*  
![Raw CSV Example](docs/images/raw_csv_sample.png)

---

## ETL Architecture

```
[Raw CSV]
   ↓
[extract/download_csv.py]
   ↓
[transform/clean_df.py]
   ↓
[Cleaned CSV Output]
   ↓
[Upload to S3 and PostgreSQL]
```

More details about the ETL phases, data cleaning logic, and SQL schema will be provided in their respective subfolders.

---

## Setup & Usage

---

## Project Structure

---
