#!/bin/bash
#
# Copy out a slice of identifiers and versions into CSV files for
# loading in to BigQuery. To be run on idb-db-slave-prod as user
# postgres.

PGSQL='/usr/bin/psql -d idb_api_prod'

# etag is a hash so prefix will give us a random slice of
# ~750M/16^3 = 185k records
slice_prefix="'000'"

echo "COPY (SELECT etag, data->>'dwc:occurrenceID' as dwc_occurrenceID
      FROM data WHERE substring(etag, 1, 3) = $slice_prefix)
      TO '/var/lib/postgresql/dump/data_slice.csv'
      WITH CSV DELIMITER ',';" | $PGSQL

echo "COPY (SELECT uuids_id as uuid, data_etag as etag, modified, version
      FROM uuids_data WHERE substring(data_etag, 1, 3) = $slice_prefix)
      TO '/var/lib/postgresql/dump/uuids_data_slice.csv'
      WITH CSV DELIMITER ',';" | $PGSQL
