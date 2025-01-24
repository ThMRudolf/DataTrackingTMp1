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

#################################### Data Processing #############################
events = []
for (i,row) in component_streams_df.iterrows():
    for event in row.events:
        event["id"] = i
    events.append(pd.DataFrame(component_streams_df.events[i]))
component_streams_events_df = pd.concat(events, axis = 0)

component_streams_final_df = component_streams_df.merge(component_streams_events_df,how="inner",left_index=True,right_on="id", suffixes=("","_event"))
component_streams_final_df.reset_index(inplace=True)
component_streams_final_df.drop(columns = ["events", "id", "id_event", "index"], inplace = True)

component_streams_final_df.to_csv("../Output/Trace_current.csv", index=False)
