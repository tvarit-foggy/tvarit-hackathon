import csv
import json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch


es = Elasticsearch(hosts="http://elastic:1234567Ee@ec2-54-189-130-235.us-west-2.compute.amazonaws.com:9200/")

def read_csv():
    with open('server_packet_data.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        data = []
        for row in csv_reader:
            data.append(row)
    return data[0], data[1:]

def process_json(raw_json):
    if type(raw_json) == list:
        for i, l in enumerate(raw_json):
            raw_json[i] = process_json(l)
        return raw_json

    if type(raw_json) != dict:
        return raw_json

    for data_type in ['BOOL', 'L', 'M', 'N', 'S']:
        if data_type in raw_json:
            return process_json(raw_json[data_type])

    for key in raw_json:
        raw_json[key] = process_json(raw_json[key])

    return raw_json

def process_data(data):
    keys = ["timestamp (S)",
            "destination (M)",
            "event (M)",
            "network (M)",
            "source (M)",
            "type (S)",
            "flow (M)",
            "client (M)",
            "server (M)",
            "status (S)",
            "dhcpv4 (M)",
            "dns (M)",
            "icmp (M)",
            "method (S)",
            "path (S)",
            "query (S)",
            "resource (S)"]
    for key in keys:
        if key not in keys:
            del data[key]
    return data

def write_es(data):
    es.index(index='packets', body=data)
    return

def run():
    consumer = KafkaConsumer(
    'packetbeats-topic',
    bootstrap_servers=[
        'ec2-99-79-7-20.ca-central-1.compute.amazonaws.com:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        message = message.value
        print('{} added'.format(message))
        processed_data = process_data(message)
        write_es(processed_data)
        # print(processed_data)
        # save_data(processed_data)

run()
