# Azure Data Engineering Tasks with Azure Data Factory and Blob Storage

## Overview
This project demonstrates four essential data engineering tasks using Azure Data Factory (ADF), Azure Blob Storage, and Azure SQL Database. The tasks include:

1. **Copying Data from Database to CSV, Parquet, and Avro File Formats**
2. **Configuring Schedule and Event Triggers to Automate Pipelines**
3. **Copying All Tables from One Database to Another**
4. **Copying Selective Tables with Selective Columns Between Databases**

These workflows support reporting, analytics, data warehousing, migration, and compliance scenarios.

---

## Prerequisites
- An active [Azure subscription](https://azure.microsoft.com/free/)
- Azure SQL Database(s) with sample data (e.g., `Employees`, `Departments` tables)
- [Azure Data Factory](https://docs.microsoft.com/azure/data-factory/introduction) instance
- Azure Blob Storage account
- Sufficient permissions to create resources and run pipelines

---

## 1. Copy Data from Database to CSV, Parquet, and Avro File Formats

**Purpose:**
- Export data from Azure SQL Database to multiple file formats for compatibility, analytics, and downstream processing.

**Steps:**
1. **Create Linked Services** in ADF for your Azure SQL Database and Blob Storage.
2. **Create Datasets** for:
   - Source: Azure SQL Table (e.g., `Employees`)
   - Sinks: CSV, Parquet, and Avro files in Blob Storage
3. **Build a Pipeline** with three Copy Data activities (one for each format):
   - **Source:** Table or custom query (e.g., `SELECT * FROM Employees`)
   - **Sink:** Choose DelimitedText (CSV), Parquet, or Avro format
4. **Run the Pipeline** to export data to Blob Storage.

**Example:**
- Output files: `employees.csv`, `employees.parquet`, `employees.avro` in your Blob container

**Use Cases:**
- CSV for interoperability, Parquet for analytics, Avro for schema evolution and compact storage

---

## 2. Configure Schedule Trigger and Event Triggers to Automate the Pipeline Process

**Purpose:**
- Automate data movement for real-time and batch scenarios.

**Steps:**
1. **Schedule Trigger:**
   - In ADF, create a new trigger of type `Schedule` (e.g., daily at midnight)
   - Attach the trigger to your pipeline
2. **Event Trigger:**
   - Create a trigger of type `Event` (e.g., Blob Created event)
   - Configure the trigger to listen for new files in a specific Blob Storage path
   - Attach the trigger to your pipeline

**Example JSON (Schedule Trigger):**
```json
{
  "type": "ScheduleTrigger",
  "typeProperties": {
    "recurrence": { "frequency": "Day", "interval": 1 }
  }
}
```

**Use Cases:**
- Schedule: Regular ETL jobs
- Event: React to new data arrivals or database changes

---

## 3. Copy All Tables from One Database to Another

**Purpose:**
- Full database replication for migration, backup, or environment sync.

**Steps:**
1. **Get Metadata Activity:**
   - Use to list all tables in the source database
2. **ForEach Activity:**
   - Iterate over the list of tables
   - For each table, use a Copy Data activity to transfer data to the target database
3. **Parameterize Datasets:**
   - Use table name as a parameter for dynamic copying

**Example SQL to List Tables:**
```sql
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';
```

**Best Practice:**
- Ensure target tables exist with matching schema before copying

---

## 4. Copy Selective Tables with Selective Columns from One Database to Another

**Purpose:**
- Targeted data migration for compliance, reduced data volume, or business-specific needs.

**Steps:**
1. **Parameterize Pipeline:**
   - Accept table and column names as parameters
2. **Custom SQL Query:**
   - Use a query like `SELECT column1, column2 FROM TableName` in the Copy Data activity
3. **Copy Data Activity:**
   - Map source columns to target columns as needed

**Example:**
```json
{
  "source": {
    "type": "SqlSource",
    "sqlReaderQuery": "SELECT FirstName, LastName FROM Employees"
  }
}
```

**Use Cases:**
- Migrate only necessary data for privacy, compliance, or efficiency

---

## Tips & Best Practices
- Use parameterization in ADF for reusable pipelines
- Monitor pipeline runs and set up alerts for failures
- Use staging in Blob Storage for intermediate data
- Secure your data with managed identities and firewall rules
- Test pipelines with sample data before production runs

---

## References
- [Azure Data Factory Documentation](https://docs.microsoft.com/azure/data-factory/)
- [Azure SQL Database Documentation](https://docs.microsoft.com/azure/azure-sql/)
- [Azure Blob Storage Documentation](https://docs.microsoft.com/azure/storage/blobs/)
