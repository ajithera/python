import yaml

def search_yaml_key(yaml_file, key):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # Convert the key to lowercase for case-insensitive search
    key_lower = key.lower()

    # Traverse the YAML data recursively
    def traverse(data, key_lower):
        if isinstance(data, dict):
            for k, v in data.items():
                if k.lower() == key_lower:
                    return v
                result = traverse(v, key_lower)
                if result is not None:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = traverse(item, key_lower)
                if result is not None:
                    return result

    return traverse(data, key_lower)

# Usage example
yaml_file_path = 'D:\Learning\Coder_mode\Python_\office_tasks\example.yaml'
search_key = 'PERSON'

result = search_yaml_key(yaml_file_path, search_key)
if result is not None:
    print(f"Value for key '{search_key}' found: {result}")
else:
    print(f"Key '{search_key}' not found in the YAML file.")

import yaml

def search_yaml_key(yaml_file, key):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

        # Convert the keys to lowercase
        if isinstance(data, dict):
            data = {k.lower(): v for k, v in data.items()}
        else:
            data = {}

    # Convert the search key to lowercase for case-insensitive search
    key_lower = key.lower()

    # Perform the search
    def traverse(data, key_lower):
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key_lower:
                    return v
                result = traverse(v, key_lower)
                if result is not None:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = traverse(item, key_lower)
                if result is not None:
                    return result

    return traverse(data, key_lower)

# Usage example
yaml_file_path = 'D:\Learning\Coder_mode\Python_\office_tasks\example.yaml'
search_key = 'PERSON'



import yaml

# Load the YAML file
with open(yaml_file_path, 'r') as file:
    yaml_data = yaml.safe_load(file)

# Search for a specific key value
target_key = ['pErSon','BoOk']
result = None

# Perform case-insensitive search
for key, value in yaml_data.items():
    if key.lower() == target_key.lower():
        result = value
        break
    elif isinstance(value, dict):
        for inner_key, inner_value in value.items():
            if inner_key.lower() == target_key.lower():
                result = inner_value
                break

if result is not None:
    print(f"Value for key '{target_key}': {result}")
else:
    print(f"Key '{target_key}' not found.")


import yaml

yaml_file_path = 'D:\Learning\Coder_mode\Python_\office_tasks\example.yaml'

# Load the YAML file
with open(yaml_file_path, 'r') as file:
    yaml_data = yaml.safe_load(file)

# Convert all keys to lowercase
def convert_keys_to_lowercase(data):
    if isinstance(data, dict):
        return {key.lower(): convert_keys_to_lowercase(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_keys_to_lowercase(item) for item in data]
    return data

lowercase_yaml_data = convert_keys_to_lowercase(yaml_data)


# Search for a specific key value
target_key1 = 'PerSon'
result1 = lowercase_yaml_data.get(target_key1.lower())

target_key = 'BoOK'
result = lowercase_yaml_data.get(target_key.lower())


if result is not None:
    print(f"Value for key '{target_key}': {result}")
else:
    print(f"Key '{target_key}' not found.")
