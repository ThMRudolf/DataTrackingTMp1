# Create an instance of the parser
parser = MTConnectSampleParser('Trace_samples.xml')

# Get all device streams
device_streams = parser.get_device_streams()
print("Device Streams:")
for stream in device_streams:
    print(stream)

# Get all component streams for a specific device
device_name = 'TM-1P'  # Replace with the device name
component_streams = parser.get_component_streams(device_name)
print(f"\nComponent Streams for Device '{device_name}':")
for component in component_streams:
    print(component)

# Get samples for a specific component
component_id = 'x_axis'  # Replace with the desired component ID
samples = parser.get_samples(component_id)
print(f"\nSamples for Component '{component_id}':")
for sample in samples:
    print(sample)

# Get events for a specific component
events = parser.get_events(component_id)
print(f"\nEvents for Component '{component_id}':")
for event in events:
    print(event)
