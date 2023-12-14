# Covid-19-Data-Analysis
This project focuses on analysing a sample dataset of COVID-19 cases recorded from January 2019 to December 2020 across different countries.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Summary](#data-summary)
- [Prerequisites](#prerequisites)
- [Instructions](#instructions)
- [Output](#output)
- [Contribution](#contribution)

## Project Overview
This project conducts an analysis of COVID-19 data for the years 2019 and 2020, employing PostgreSQL PGAdmin 4 for the creation and execution of SQL queries. It includes an SQL file containing all the queries necessary to answer specific questions about the data, alongside an output file featuring screenshots of the results as displayed in PGAdmin 4.

## Data Summary
| Column Name     | Description                                                      | Data Type      |
|-----------------|------------------------------------------------------------------|----------------|
| sno             | A unique serial number for each record.                          | int            |
| observationdate | The date of observation in the format varchar(15).               | varchar        |
| province        | The province where the observation was made.                     | varchar        |
| country         | The country where the observation was made.                      | varchar        |
| lastupdate      | The date and time of the last update for the record.             | varchar        |
| confirmed       | The number of confirmed COVID-19 cases.                          | int            |
| deaths          | The number of deaths due to COVID-19.                            | int            |
| recovered       | The number of recovered COVID-19 cases.                          | int            |

## Prerequisites
Before initiating the project, make sure you have installed the following on your local machine:
- PostgreSQL database
- Python 3.x
- pgAdmin 4 

## Instructions
Follow the following steps to successfully complete this project.

1. Database and Table Creation: To begin, set up a database called 'covid_19_data'. In this database, create a table also named 'covid_19_data', which is structured to hold the dataset appropriately.

2. Data Type Modification: Alter the data type of the 'ObservationDate' column in the 'covid_19_data' table. Convert it from its original 'String' format to the more suitable 'DATE' data type.

3. Data Extraction and Loading: Employ a Python script to fetch the 'Covid_19_data.csv' file. After acquisition, import the data from this file into the 'covid_19_data' table in the PostgreSQL database.

4. SQL Queries Using PostgreSQL PGAdmin: Use PostgreSQL PGAdmin, an effective database management tool, to create and execute SQL queries. Utilize this platform to analyze the dataset and answer pertinent questions.

5. Consolidated SQL Script: Compile all your SQL queries in one unified SQL file. This comprehensive document should encompass all the SQL queries developed throughout the project, structured for ease of understanding and readability.

Adhering to these guidelines will guide you in methodically using PostgreSQL for setting up the database, importing the data, and executing SQL queries. These outlined steps are designed to assist you in efficiently analyzing the COVID-19 dataset and deriving insightful conclusions.

## Output
The `output` folder includes screenshots showcasing the results of the queries when they are executed in pgAdmin 4.

## Contribution
Your contributions to improve and expand this project are greatly valued. You are encouraged to contribute by submitting pull requests, reporting issues, or offering feedback.
