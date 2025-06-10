# s3-supplier-pipeline

Pipeline focused on cleaning monthly purchase reports, for a real Retail Company based in Spain, in order to load the data to postgre SQL for analysis.

---

## What is this? 

A pipeline that processes real monthly reports issued by a **Cooperative** who gathers multiple suppliers. 
The purchaser is a real **Wholesale and Retail Company** based in Spain. 
Each monthly report is provided in CSV format. After manual download, the pipeline parses and transforms these files into a clean, unified dataset. This dataset becomes the foundation for business intelligence tasks such as supplier analysis, purchasing trends, and budget planning.


# Logic behind the reports (necessary to define the purpose of the pipeline)

The monthly report is the comparison between the amount purchased in the same month of the current year vs the previous year trough two different channels: warehouse (items purchased by the Coopeative and stored in its warehouse) or direct (items purchased directly to the supplier.
Pros and cons of each purchasing method:
               
warehouse     pros:  periodic delivery, possibilty of combinig in asame order items of various suppliers.
              cons:  prices are a bit more expensive.
              
direct        pros:  Bonuses at the end of the year proportional to purchasing volume. In most cases lower prices.
              cons:  Delivery can be slow, specially if ordering to factories. Need to puechase medium to big volumes.

---

## Report Structure (Raw CSV Columns)

Each row represents a single supplier. The columns include purchase accumulations across two years and multiple channels:

| Column Name              | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `PROVEEDOR`              | Supplier name.                                                              |
| `Acum. Almacén 2024`     | Purchases from the warehouse in X month of current year in €                |
| `Acum. Directo 2024`     | Direct purchases in X month of current year in €                            |
| `Acum. Almacén 2023`     | Purchases from the warehouse in X month of previous year in €               |
| `Acum. Directo 2023`     | Direct purchases in X month of previous year in €                           |

#### [Example Image of a raw .csv report](URL-or-path-to-image)
---

More details about the ETL phases, data cleaning logic, and SQL schema will be provided in their respective subfolders.
