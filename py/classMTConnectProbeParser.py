import xml.etree.ElementTree as ET


class MTConnectProbeParser:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.namespace = {'m': 'urn:mtconnect.org:MTConnectDevices:1.2'}

    def get_device_info(self):
        devices = []
        for device in self.root.findall('.//m:Device', self.namespace):
            device_info = {
                'id': device.get('id'),
                'name': device.get('name'),
                'uuid': device.get('uuid'),
                'sampleInterval': device.get('sampleInterval'),
                'manufacturer': device.find('m:Description', self.namespace).get('manufacturer'),
                'model': device.find('m:Description', self.namespace).get('model'),
            }
            devices.append(device_info)
        return devices

    def get_components(self, device_id):
        components = []
        for component in self.root.findall(f".//m:Device[@id='{device_id}']/m:Components//*", self.namespace):
            component_info = {
                'id': component.get('id'),
                'name': component.get('name'),
                'type': component.tag.split('}')[-1],  # Extract the type (e.g., 'Controller', 'Axes')
            }
            components.append(component_info)
        return components

    def get_data_items(self, component_id):
        data_items = []
        for data_item in self.root.findall(f".//*[@id='{component_id}']/m:DataItems/m:DataItem", self.namespace):
            data_item_info = {
                'id': data_item.get('id'),
                'name': data_item.get('name'),
                'type': data_item.get('type'),
                'category': data_item.get('category'),
                'units': data_item.get('units'),
                'nativeUnits': data_item.get('nativeUnits'),
                'subType': data_item.get('subType'),
                'source': data_item.find('m:Source', self.namespace).text if data_item.find('m:Source', self.namespace) else None
            }
            data_items.append(data_item_info)
        return data_items
