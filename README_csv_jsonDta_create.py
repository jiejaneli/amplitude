# td-qa

Script description

This Python script is used to create csv input files to facilitate testing Amplitude Output Plugins to upload the  data to Amplitude via Amplitude HTTP API
The input file currently specifies 46 columns, as below:
    - {name: app, type: long}
    - {name: amplitude_id, type: long}
    - {name: user_id, type: string}
    - {name: device_id, type: string}
    - {name: event_time, type: timestamp, format: '%Y-%m-%d %H:%M:%S.%L'}
    - {name: server_upload_time, type: timestamp, format: '%Y-%m-%d %H:%M:%S.%L'}
    - {name: client_event_time, type: timestamp, format: '%Y-%m-%d %H:%M:%S.%L'}
    - {name: client_upload_time, type: timestamp, format: '%Y-%m-%d %H:%M:%S.%L'}
    - {name: event_id, type: long}
    - {name: session_id, type: long}
    - {name: event_type, type: string}
    - {name: amplitude_event_type, type: string}
    - {name: version_name, type: string}
    - {name: _schema, type: long}
    - {name: adid, type: string}
    - {name: groups, type: json}
    - {name: idfa, type: string}
    - {name: library, type: string}
    - {name: processed_time, type: timestamp, format: '%Y-%m-%d %H:%M:%S.%L'}
    - {name: user_creation_time, type: timestamp, format: '%Y-%m-%d %H:%M:%S.%L'}
    - {name: platform, type: string}
    - {name: os_name, type: string}
    - {name: os_version, type: string}
    - {name: device_brand, type: string}
    - {name: device_manufacturer, type: string}
    - {name: device_model, type: string}
    - {name: device_carrier, type: string}
    - {name: device_type, type: string}
    - {name: device_family, type: string}
    - {name: location_lat, type: string}
    - {name: location_lng, type: string}
    - {name: country, type: string}
    - {name: language, type: string}
    - {name: city, type: string}
    - {name: region, type: string}
    - {name: dma, type: string}
    - {name: revenue, type: string}
    - {name: ip_address, type: string}
    - {name: paying, type: string}
    - {name: start_version, type: string}
    - {name: event_properties, type: json}
    - {name: user_properties, type: json}
    - {name: data, type: string}
    - {name: uuid, type: string}
    - {name: _insert_id, type: string}
    - {name: time, type: long}

The script basically generate multiple events of these 46 columns (one event per line).
Each column can be generated with of the following choices:
   1)  empty string -  meaning no input for this column if this column is optional (not required input)
   2)  non-empty and valid type of input, as specified above
   3)  randomly created input at run time, either of 1) or 2) above

The script requires two command-line arguments:   output_csv_file_name and number_of_events_to_generate.
The first argument let user specify the name of csv output file,
The second argument tells the script how many events (lines of inputs) to create for the csv file.

Currently the script supprots only Python 2.x, as the version installed on office laptop is 2.7.
Version 3.x will be investigated if needed after the script is in a good shape.

the script requires the delimiter defined in the config.yml as ';'


