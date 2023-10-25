def executeScript(input):
    input["record"] = {}
    for row in input["rows"]:
        for map in input["mappings"]:
            if map["customer_field"] == row:
                if map["required"] and input["rows"][row] != '':
                    if map["convert.value"] != '':
                        if map['type'] == 'boolean':
                            input["record"][map["digital_onboarding_field"]] = input["rows"][row] == map["convert.value"]
                    else:
                        input["record"][map["digital_onboarding_field"]] = input["rows"][row]
                else:
                    input["record"] = {}
                    return
    return input["record"]
    
input = {
    "rows":{
        "EventSource": "MTE",
        "InternalUserID": "14",
        "UserLogin": "ch.cash",
        "MemberNumber": "300158",
        "SessionID": "7516c940-63cc-40d7-8308-7d3f41d86b3b",
        "EventDate": "2021-06-17",
        "EventTime": "13:13:16.905",
        "IPAddress": "75.148.0.46",
        "Service": "APP",
        "Action": "LOGIN",
        "Result": "",
        "Attribute": "",
        "Latitude": "",
        "Longitude": "",
        "Client": "Iphone",
        "OSVersion": "14.6",
        "Device": "iPhone12,1",
        "AppVersion": "4.40.92",
        "UserAgent": "MFM-4.40.92/iPhone-14.6",
        "CodeCustomEvent": "",
        "NameCustomEvent": ""
    },
    "mappings":[
        {
            "digital_onboarding_field": "unique_id",
            "customer_field": "MemberNumber",
            "required": "TRUE",
            "type": "string",
            "convert.condition": "",
            "convert.value": "",
            "convert.set": ""
        },
        {
            "digital_onboarding_field": "mobile-banking",
            "customer_field": "Action",
            "required": "TRUE",
            "type": "boolean",
            "convert.condition": "equals",
            "convert.value": "LOGIN",
            "convert.set": "TRUE"
        }
    ]
}
print(executeScript(input))