# Create an instance of the parser
parser = MTConnectProbeParser('Trace_probe.xml')

# Get device information
devices = parser.get_device_info()
print("Devices:")
for device in devices:
    print(device)

# Get components for a specific device
device_id = 'dev1'  # Replace with the desired device ID
components = parser.get_components(device_id)
print("\nComponents:")
for component in components:
    print(component)

# Get data items for a specific component
component_id = 'cont1'  # Replace with the desired component ID
data_items = parser.get_data_items(component_id)
print("\nData Items:")
for data_item in data_items:
    print(data_item)
