# intrinio_sdk.DataPointApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_point_number**](DataPointApi.md#get_data_point_number) | **GET** /data_point/{identifier}/{item}/number | Get a Data Point (Number)
[**get_data_point_text**](DataPointApi.md#get_data_point_text) | **GET** /data_point/{identifier}/{item}/text | Get a Data Point (Text)


# **get_data_point_number**
> DataPointNumber get_data_point_number(identifier, item)

Get a Data Point (Number)

Returns a numeric value for the given `item` and the entity with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api-key'] = 'YOUR_API_KEY'

data_point_api = intrinio_sdk.DataPointApi()

identifier = 'identifier_example' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
item = 'item_example' # str | An Intrinio data tag or other item

try:
    api_response = data_point_api.get_data_point_number(identifier, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPointApi->get_data_point_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) | 
 **item** | **str**| An Intrinio data tag or other item | 

### Return type

[**DataPointNumber**](DataPointNumber.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_point_text**
> DataPointText get_data_point_text(identifier, item)

Get a Data Point (Text)

Returns a text value for the given `item` and the entity with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api-key'] = 'YOUR_API_KEY'

data_point_api = intrinio_sdk.DataPointApi()

identifier = 'identifier_example' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
item = 'item_example' # str | An Intrinio data tag or other item

try:
    api_response = data_point_api.get_data_point_text(identifier, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPointApi->get_data_point_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) | 
 **item** | **str**| An Intrinio data tag or other item | 

### Return type

[**DataPointText**](DataPointText.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

