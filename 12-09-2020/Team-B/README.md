### Steps
1. Create Kinesis Stream
    1. Create Kinesis Stream Hackathon-12-09-2020-Team-B-Source
    1. Publish Data using publish.py
    1. Check if data is successfully published using monitor tab
1. Write Raw Data to S3 Bucket
    1. Create delivery stream in AWS Kinesis
        1. Write to S3 from Hackathon-12-09-2020-Team-B-Source
1. Run Flink Application on Data
    1. Create Kinesis Stream Hackathon-12-09-2020-Team-B-Target
    1. Download this repository
    1. `sudo apt install maven openjdk-8-jre openjdk-8-jdk`
    1. `mkdir -p ~/.m2/repository/org/apache/flink/flink-connector-kinesis_2.11/1.8.2/`
    1. `cp target/flink-connector-kinesis_2.11-1.8.2.jar ~/.m2/repository/org/apache/flink/flink-connector-kinesis_2.11/1.8.2/`
    1. `cd GettingStarted`
    1. `maven package`
    1. Create S3 bucket named com.tvarit.hackathon-12-09-2020.teamb
    1. Upload target/aws-kinesis-analytics-java-apps-1.0.jar to the S3 bucket
    1. Create Data Analytics application on AWS Kinesis
    1. Select type as Flink
    1. Save
    1. Click on configure
    1. Select the jar file uploaded in com.tvarit.hackathon-12-09-2020.teamb
    1. Save
    1. Update the IAM Policy with the policy.json. Change region, aws account id etc with the correct ones
    1. Run application

1. Write Processed Data to S3 Bucket
    1. Create delivery stream in AWS Kinesis
        1. Write to S3 from Hackathon-12-09-2020-Team-B-Target
