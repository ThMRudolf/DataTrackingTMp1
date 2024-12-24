import xml.etree.ElementTree as ET

class MTConnectCurrentParser:
    def __init__(self, source):
        if source.startswith('http://') or source.startswith('https://'):
            # Fetch XML from URL
            response = requests.get(source)
            response.raise_for_status()  # Raise an error for bad responses (e.g., 404)
            xml_content = response.text
        else:
            # Load XML from local file
            with open(source, 'r') as file:
                xml_content = file.read()

        # Parse the XML
        self.tree = ET.ElementTree(ET.fromstring(xml_content))
        self.root = self.tree.getroot()
        self.namespace = {'m': 'urn:mtconnect.org:MTConnectStreams:1.2'}
        #if input is local file    
        #self.tree = ET.parse(xml_file)
        #self.root = self.tree.getroot()

    def get_device_streams(self):
        device_streams = []
        # if input is url
        # for device_stream in self.root.findall('.//m:DeviceStream', self.namespace):
        # if input is local file
        for device in self.root.findall('.//{urn:mtconnect.org:MTConnectStreams:1.2}DeviceStream'):
            name = device.get('name')
            uuid = device.get('uuid')
            device_streams.append({'name': name, 'uuid': uuid})
        return device_streams

    def get_component_streams_with_events(self, device_name):
        component_streams = []
        # if inout is url
        #for component_stream in self.root.findall(f".//m:DeviceStream[@name='{device_name}']/m:ComponentStream", self.namespace):
        # if input is a local file
        for device in self.root.findall(f".//{{urn:mtconnect.org:MTConnectStreams:1.2}}DeviceStream[@name='{device_name}']"):
            for component in device.findall('.//{urn:mtconnect.org:MTConnectStreams:1.2}ComponentStream'):
                component_name = component.get('name')
                component_id = component.get('componentId')
                component_type = component.get('component')

                # Gather events
                events = []
                for event in component.findall('.//{urn:mtconnect.org:MTConnectStreams:1.2}Events/*'):
                    event_data = {
                        'dataItemId': event.get('dataItemId'),
                        'timestamp': event.get('timestamp'),
                        'sequence': event.get('sequence'),
                        'name': event.get('name'),
                        'value': event.text.strip() if event.text else None
                    }
                    events.append(event_data)

                component_streams.append({
                    'name': component_name,
                    'id': component_id,
                    'type': component_type,
                    'events': events
                })
        return component_streams