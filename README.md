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
only do a small slice selected by uuid prefix which will give us a random 
cross-section of data.

### Processing

Try using a Jupyter notebook with inline SQL query.