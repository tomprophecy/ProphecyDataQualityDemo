## Gems

### Deequ

This component leverages AWS Deequ, a library built on top of Apache Spark for defining and executing data quality checks on large datasets. It enables users to specify a variety of data quality constraints, such as completeness, uniqueness, and compliance, to ensure the integrity of their data. The results of these checks can be used to monitor the health of the data over time and trigger alerts or workflows if anomalies are detected.

## Subgraphs

## Audit

The auditing subgraph function is designed to perform a thorough examination of a specified table, assessing various metrics such as row count, column statistics, and data anomalies. Upon completion, the results of the audit are automatically appended to another designated table, which serves as a historical record of audits. This function is crucial for maintaining transparency, tracking changes, and ensuring data governance within an organization.

## Pipelines

### deequ_test

The **deequ_test** pipeline is a Spark-based solution that utilizes the Deequ library to perform data quality checks on a dataset. This pipeline checks for completeness of text columns, adds null values to the dataset, and performs a data quality audit. By running this pipeline in a Spark environment using Python, data quality issues can be identified and addressed, leading to more accurate and reliable insights.

## Datasets

1. **dq_audits**
This dataset contains information about data quality audits, including the timestamp of the audit, the name of the column being audited, the number of null values found, and the number of non-null values found. This data is useful for monitoring data quality and identifying areas for improvement in data collection and processing. It can also aid in identifying potential issues with data analysis and decision-making based on incomplete or inaccurate data.

2. **deequ_test**
This dataset is a test dataset for Deequ, a data quality library for Apache Spark. It consists of a single column named 'input' with string values. This dataset is used for testing and validating the functionality of Deequ's data quality checks and constraints. It is an essential resource for ensuring the accuracy and reliability of data processing and analysis.

