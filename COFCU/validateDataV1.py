def map_columns(input):
    results = []
    for data in input["data"]:
        result = {}
        for key, value in data.items():
            mapped_key = None
            for column_map in input["mapping"]:
                if column_map['column'] == key:
                    mapped_key = column_map['desired_column']
                    break

            if mapped_key is not None:
                mapped_value = value

                # Check if a character needs to be replaced
                replace_characters = column_map.get('replace_characters')
                if replace_characters:
                    for old, new in replace_characters.items():
                        mapped_value = mapped_value.replace(old, new)

                value_mapping = column_map.get('value_mapping')
                if value_mapping:
                    if value in value_mapping:
                        mapped_value = value_mapping[value]
                    else:
                        mapped_value = value_mapping["fallback"]

                concatenate_order = column_map.get('concatenate_order')

                if concatenate_order:
                    concatenate_value = ''
                    for order_item in concatenate_order:
                        if 'column' in order_item and order_item['column'] in data:
                            concatenate_value += str(data[order_item['column']])

                        if 'string' in order_item:
                            concatenate_value += order_item['string']

                    mapped_value = concatenate_value
            
                # Check if needs to be a required value
                required_values = column_map.get('required_values')
                if required_values and value not in required_values:
                    break

                result[mapped_key] = mapped_value

        # Check for required fields
        missing_fields = [column_map['desired_column'] for column_map in input["mapping"] if column_map.get('required', False) and column_map['desired_column'] not in result]
        
        # Check required values are not empty
        empty_fields = [column_map['desired_column'] for column_map in input["mapping"] if column_map.get('required', False) and column_map['desired_column'] in result and not result[column_map['desired_column']]]
        
        if not missing_fields and not empty_fields:
            results.append(result)
    return results

# Example dictionary and mapping
input = {
    
}
input["data"] = [
    {
        "MemberNumber": "3177663559",
        "Action": "LOGIN",
        "ReplaceMe":"P1000",
        "Account":"1000",
        "Suffix":"S"
    }
]

input["mapping"] = [
        {
            "column": "MemberNumber",
            "desired_column": "unique_id",
            "required": True
        },
        {
            "column": "Action",
            "value_mapping": {
                "LOGIN": True,
                "fallback": False
            },
            "desired_column": "online-banking",
            "required": True
        },
        {
            "column": "ReplaceMe",
            "replace_characters": {
                "P": ""
            },
            "desired_column": "account_number",
            "required": True
        },
        {
            "column": "Account",
            "concatenate_order": [
                {
                    "column":"Account"
                },
                {
                    "column":"Suffix"
                },
                {
                    "string":"L"
                }
            ],
            "desired_column": "account_number",
            "required": True
        }
    ]

# Map columns
mapped_data = map_columns(input)

# Print the mapped input["data"]
print(mapped_data)
