import csv
import json


class ProcessData:
    def __init__(self):
        pass

    def read_csv(self):
        with open('server_packet_data.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            data = []
            for row in csv_reader:
                data.append(row)
        return data[0], data[1:]

    def process_json(self, raw_json):
        if type(raw_json) == list:
            for i, l in enumerate(raw_json):
                raw_json[i] = self.process_json(l)
            return raw_json

        if type(raw_json) != dict:
            return raw_json

        for data_type in ['BOOL', 'L', 'M', 'N', 'S']:
            if data_type in raw_json:
                return self.process_json(raw_json[data_type])

        for key in raw_json:
            raw_json[key] = self.process_json(raw_json[key])

        return raw_json

    def process_data(self, keys, data):
        processed_data = {'data': []}
        for packet in data:
            packet_json = {}
            for i in range(len(packet)):
                try:
                    if '(M)' in keys[i]:
                        raw_json = json.loads(packet[i])
                        packet_json[keys[i]] = self.process_json(raw_json)
                    else:
                        packet_json[keys[i]] = packet[i].strip()
                except Exception:
                    packet_json[keys[i]] = {}
            keys_keep = ["timestamp (S)",
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
                if key not in keys_keep:
                    del packet_json[key]
            processed_data['data'].append(packet_json)
        return processed_data

    def save_data(self, data):
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return

    def run(self):
        keys, data = self.read_csv()
        processed_data = self.process_data(keys, data)
        self.save_data(processed_data)


ProcessData().run()
