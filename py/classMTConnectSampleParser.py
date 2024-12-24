import xml.etree.ElementTree as ET

class MTConnectSampleParser:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.namespace = {'m': 'urn:mtconnect.org:MTConnectStreams:1.2'}

    def get_device_streams(self):
        device_streams = []
        for device_stream in self.root.findall('.//m:DeviceStream', self.namespace):
            device_info = {
                'name': device_stream.get('name'),
                'uuid': device_stream.get('uuid'),
            }
            device_streams.append(device_info)
        return device_streams

    def get_component_streams(self, device_name):
        component_streams = []
        for component_stream in self.root.findall(f".//m:DeviceStream[@name='{device_name}']/m:ComponentStream", self.namespace):
            component_info = {
                'component': component_stream.get('component'),
                'componentId': component_stream.get('componentId'),
                'name': component_stream.get('name'),
            }
            component_streams.append(component_info)
        return component_streams

    def get_samples(self, component_id):
        samples = []
        for sample in self.root.findall(f".//m:ComponentStream[@componentId='{component_id}']/m:Samples/*", self.namespace):
            sample_info = {
                'type': sample.tag.split('}')[-1],  # Extract the sample type (e.g., PathPosition)
                'dataItemId': sample.get('dataItemId'),
                'timestamp': sample.get('timestamp'),
                'sequence': sample.get('sequence'),
                'name': sample.get('name'),
                'subType': sample.get('subType'),
                'value': float(sample.text) if sample.text else None,
            }
            samples.append(sample_info)
        return samples

    def get_events(self, component_id):
        events = []
        for event in self.root.findall(f".//m:ComponentStream[@componentId='{component_id}']/m:Events/*", self.namespace):
            event_info = {
                'type': event.tag.split('}')[-1],  # Extract the event type (e.g., Message)
                'dataItemId': event.get('dataItemId'),
                'timestamp': event.get('timestamp'),
                'sequence': event.get('sequence'),
                'name': event.get('name'),
                'value': event.text.strip() if event.text else None,
            }
            events.append(event_info)
        return events
