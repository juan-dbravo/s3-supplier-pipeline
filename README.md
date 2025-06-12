# s3-supplier-pipeline: A Cloud-Native ETL Pipeline for Supplier Spend Analysis in a Spanish SME Context

A modular ETL pipeline for transforming monthly supplier purchase reports for a real Wholesale & Retail Company based in Spain. Outputs clean data for loading into PostgreSQL and performing supplier analysis, purchasing trend reports, and business planning.

---

## Table of Contents
- [Executive Summary](#executive-summary)
- [Business Problem & Motivation](#business-problem--motivation)
- [Data Structure & Raw Input](#data-structure--raw-input)
- [Methodology & ETL Architecture](#methodology--etl-architecture)
- [Setup & Execution](#setup--execution)
- [Repository Structure](#repository-structure)

---

## Executive Summary

This pipeline processes real monthly CSV reports issued by a Cooperative. Each report compares purchase totals from the same month across two years and two channels: warehouse and direct supplier.

The result is a unified, clean CSV ready for analysis or loading into a PostgreSQL database.

#### Disclaimer:

This project is for educational and pportfolio purposes only . All data has been anonymized or synthesized based on real-world report structures. No confidential or proprietary business information is included.

---

## Business Problem & Motivation

The purchaser is a mid-sized Retail & Wholesale company (Spain, ~€2M/year). Each month, they receive a report comparing purchases made via:

- **Warehouse**: more expensive, but faster and combines suppliers.
- **Direct**: cheaper, slower, and comes with annual bonuses.

Clean data helps answer questions like:
- Are we ordering more via direct or warehouse this year?
- Which suppliers dropped in volume compared to last year?
- Is our bonus-earning potential increasing?

---

## Data Structure & Raw Input

Each row represents a single supplier. The columns include purchase accumulations across two years and multiple channels:

| Column Name              | Description                                                                     |
|--------------------------|---------------------------------------------------------------------------------|
| `PROVEEDOR`              | Supplier name (up to 280 different suppliers)                                   |
| `Acum. Almacén 2025`     | Purchases from the warehouse in a given month (e.g., May) of current year in €  |
| `Acum. Directo 2025`     | Direct purchases in the same month of current year in €                         |
| `Acum. Encargos 2025`    | Additional purchase chanel (Column to be deleted in cleaning stage)             |
| `Acum. Almacén 2024`     | Purchases from the warehouse in a given month (e.g., May) of previous year in € |
| `Acum. Directo 2024`     | Direct purchases in the same month of previous year in €                        |
| `Acum. Encargos 2024`    | Additional purchase chanel (Column to be deleted)                               |

*Example:*

[Raw CSV May Report](images/raw_report.png)

Note: Supplier names have been left visible for illustrative purposes only. No sensitive information is shown. This excerpt contains fewer than 5% of the original data and is used for educational context.

---

## Methodology & ETL Architecture

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

## Setup & Execution

Instructions coming soon: environment setup, how to run the pipeline, and sample commands.

---

## Repository Structure

A breakdown of folders and key scripts.

---
