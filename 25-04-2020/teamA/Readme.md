## Scope of the activity
* Create a consumer with the said topic from the KAFKA (EC2 instance)
* The consumer should poll every 5 seconds and fetch data in batch for the batch processing
* Process the data and move it to the Elastic Search
* Setup Kibana to show following graphs
  * Total packets transferred at any given time
  * Total HTTP packets at any given time
  * HTTP packets with different status code against time
  * Ratio of each HTTP packet types

## Tech Stack
 * Kafka python library to read and export messages 
 * Docker-compose for infrastructure commissioning
 * Elastic search as a search optimized persistence 
 * KIBANA as a user friendly interface to create dashboards 
 * AWS Lambda(server-less) to extract data from KAFKA and process it

## Architecture
We are using the below reference architecture

![Image description](resources/media/Untitled%20Diagram%20(1).png)