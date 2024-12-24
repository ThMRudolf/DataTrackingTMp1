import os
import xml.etree.ElementTree as ET
from classMTConnectCurrentParser import MTConnectCurrentParser
import pandas as pd

# Execute the Python file
#os.system('python MTConnectParser.py')

# Create an instance of the parser
current_directory = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(current_directory, '../data/Trace_current.xml')

parser = MTConnectCurrentParser('../data/Trace_current.xml')
# Store device streams in a DataFrame
device_streams = parser.get_device_streams()
device_streams_df = pd.DataFrame(device_streams)
print("Device Streams DataFrame:")
print(device_streams_df)


# Get component streams with events for a specific device
device_name = "TM-1P"
component_streams = parser.get_component_streams_with_events(device_name)
#print(f"\nComponent Streams with Events for {device_name}:")

# Store component streams with events in a DataFrame
component_streams_df = pd.DataFrame(component_streams)

#print(f"\nComponent Streams with Events DataFrame for {device_name}:")
#print("Component Streams DataFrame:")
#print(component_streams_df)
#print(component_streams_df['events'][1])
