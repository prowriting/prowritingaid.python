# swagger_client.TextApi

All URIs are relative to *https://localhost:5004*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](TextApi.md#get) | **GET** /api/async/text/result/{taskId} | 
[**post**](TextApi.md#post) | **POST** /api/async/text | 


# **get**
> AsyncResponseTextAnalysisResponse get(task_id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: licenseCode
swagger_client.configuration.api_key['licenseCode'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['licenseCode'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TextApi()
task_id = 'task_id_example' # str | 

try: 
    api_response = api_instance.get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**AsyncResponseTextAnalysisResponse**](AsyncResponseTextAnalysisResponse.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> AsyncResponseTextAnalysisResponse post(requestp)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: licenseCode
swagger_client.configuration.api_key['licenseCode'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['licenseCode'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TextApi()
requestp = swagger_client.TextAnalysisRequest() # TextAnalysisRequest | 

try: 
    api_response = api_instance.post(requestp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestp** | [**TextAnalysisRequest**](TextAnalysisRequest.md)|  | 

### Return type

[**AsyncResponseTextAnalysisResponse**](AsyncResponseTextAnalysisResponse.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
