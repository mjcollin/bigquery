# bigquery
Bigquery explorations

## First problem - changed identifiers in iDigBio

Already have done work to develop relevent SQL query and data, however running
the query on PostgreSQL single threaded is slow and moving the data into 
parquet exposed issues with character encodings in non-relvent fields.

Let's try moving this data in to BigQuery and see how things work there.

**Ref:** 
* [How many occurrences in iDigBio have had their occurrenceID change over our 7 years? #17](https://github.com/iDigBio/research-project-ideas/issues/17)
* [Prive Jupyter notebook working with Parquet](https://jupyter.idigbio.org/user/mjcollin/notebooks/ChangedOccurrenceIDs.ipynb)

### Input data

Data comes from two tables: `data` and `uuids_data` however limited columns 
are needed for this task. Additionally, given BigQuery's cost model, we'll
only do a small slice selected by etag prefix which will give us a random 
cross-section of data.

Exporting data from iDigBio PostgreSQL servers:

1. Log in to idb-db-slave-prod as postgres
1. Run pgsql_tables_to_csv.sh
1. Copy resulting .csv files from the dump directory into the data directory 
for this project


### Set up Python client

Follow the client library quick start. Place the resulting .json file in 
`~/.<account name>.json`. When running Python programs, set the 
`GOOGLE_APPLICATION_CREDENTIALS` environment variable to this file name.

In Python environment:

`pip install --upgrade google-cloud-bigquery`

**Ref:**
[Quickstart: Using Client Libraries](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries)

### Loading data into BigQuery

Among the various ways, let's try using the Python library to do so since 
that's the most realistic. 

Do the create dataset layer in the WebUI:

1. Go to BigQuery
1. Click on project name under Resources
1. Click Create Dataset in right mid nav

And run the import script with:

1. `GOOGLE_APPLICATION_CREDENTIALS=<cred file> python3 load_csv_to_bigquery.py`




### Processing

Try using a Jupyter notebook with inline SQL query.