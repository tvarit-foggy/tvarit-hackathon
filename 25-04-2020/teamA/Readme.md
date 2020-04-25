## Scope of the activity
* Create a consumer with the said topic from the KAFKA (EC2 instance)
* The consumer should poll every 5 seconds and fetch data in batch for the batch processing
* Process the data and move it to the Elastic Search
* Setup Kibana to show following graphs
  * Total packets transferred at any given time
  * Total HTTP packets at any given time
  * HTTP packets with different status code against time

## Architecture
We are using the below reference architecture