def avro_value_schema_to_python_types(inputs: dict, value_schema):
    schema = value_schema.to_json()["fields"]

    avro_schema = {}

    for dic in schema:
        avro_schema[dic["name"]] = dic["type"]

    avro_to_python_types = {
        "int": int,
        "string": str,
        "long": float,
        "float": float,
        "dobule": float,
        "bytes": bytes
    }

    avro_value = None

    for key, val in inputs.items():
        avro_value = avro_schema[key] if not isinstance(avro_schema[key], list) else avro_schema[key][0]
        inputs[key] = avro_to_python_types[avro_value](inputs[key]) if inputs[key] is not None else None

    return inputs