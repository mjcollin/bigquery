# Mostly taken from test_load_table_from_file() in 
# https://github.com/googleapis/google-cloud-python/blob/cf04f6d15615b09c1de9e584bb3462653f0770f1/bigquery/docs/snippets.py
#
# Apparently CSVs with text columns don't have their column names detected well,
# need to pass a whole schema:
# https://issuetracker.google.com/issues/112210765
from google.cloud import bigquery


dataset_id = "idb"
to_load = [
    {
        "table_id": "data_slice",
        "filename": "data/data_slice.csv",
        "schema": [
            bigquery.SchemaField("etag", "STRING"),
            bigquery.SchemaField("dwc_occurrenceid", "STRING")]
        },
    {
        "table_id": "uuids_data_slice",
        "filename": "data/uuids_data_slice.csv",
        "schema": [
            bigquery.SchemaField("uuid", "STRING"),
            bigquery.SchemaField("etag", "STRING"),
            bigquery.SchemaField("modified", "DATETIME"),
            bigquery.SchemaField("version", "INTEGER")]    
        }
    ]


client = bigquery.Client()
dataset_ref = client.dataset(dataset_id)

for d in to_load:
    table_ref = dataset_ref.table(d["table_id"])
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
#    job_config.autodetect = True
    job_config.schema = d["schema"]

    with open(d["filename"], 'rb') as source_file:
        job = client.load_table_from_file(
            source_file,
            table_ref,
            location='US',
            job_config=job_config)

    job.result()

    print('Loaded {} rows into {}:{}.'.format(
        job.output_rows, dataset_id, d["table_id"]))

