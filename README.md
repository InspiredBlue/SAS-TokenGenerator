<h1>SAS Token Generator</h1>

Sas Tokens Generator is a script that generates new Sas Tokens using Python. 

In order to generate a new Sas Token you need to fill out the following variables:

* iothubaddress -> ID of the Iot Hub
* device_id -> ID of the Device
* shared_access_key -> Located inside the Connection String
* expiry -> In seconds. Defines the Sas Token time limit.
* policy -> The policy of the Sas Token. Example: "iothubowner, registryRead, registryReadWrite, etc... " 
