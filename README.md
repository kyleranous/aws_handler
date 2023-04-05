# aws_handler
Wrapper for Boto3 AWS Calls

## TOC
1. [param_store](#param-store)


## Modules

### param_store
Param store allows access for reading, updating, and creating parameter store entries

#### get_parameter
**Returns: String**
**Arguments:**
 - parameter_name: *String* - Name of parameter to read

**Example:**
```python
result = param_store.get_paramter('test/parameter')
```

#### get_parameter_dict
**Returns: Dict**
**Arguments:**
 - parameter_name: *String - Name of parameter to rea

**Example:**
```python
result_dict = param_store.get_parameter_dict('test/parameter')
```
 