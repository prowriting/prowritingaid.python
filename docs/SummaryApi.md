# ProWritingAidSDK.SummaryApi

All URIs are relative to *https://api.prowritingaid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](SummaryApi.md#get) | **GET** /api/async/summary/result/{taskId} | Tries to get the result of a request using the task id of the request
[**post**](SummaryApi.md#post) | **POST** /api/async/summary | Gets the summary analysis of a document


# **get**
> AsyncResponseSummaryAnalysisResponse get(task_id)


Tries to get the result of a request using the task id of the request

### Example 
```python
from __future__ import print_function
import time
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
from pprint import pprint

# Configure API key authorization: licenseCode
ProWritingAidSDK.configuration.api_key['licenseCode'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ProWritingAidSDK.configuration.api_key_prefix['licenseCode'] = 'Bearer'

# create an instance of the API class
api_instance = ProWritingAidSDK.SummaryApi()
task_id = 'task_id_example' # str | 

try: 
    # Tries to get the result of a request using the task id of the request
    api_response = api_instance.get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**AsyncResponseSummaryAnalysisResponse**](AsyncResponseSummaryAnalysisResponse.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> AsyncResponseSummaryAnalysisResponse post(requestp)


Gets the summary analysis of a document

### Example 
```python
from __future__ import print_function
import time
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
from pprint import pprint

# Configure API key authorization: licenseCode
ProWritingAidSDK.configuration.api_key['licenseCode'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ProWritingAidSDK.configuration.api_key_prefix['licenseCode'] = 'Bearer'

# create an instance of the API class
api_instance = ProWritingAidSDK.SummaryApi()
requestp = ProWritingAidSDK.SummaryAnalysisRequest() # SummaryAnalysisRequest | 

try: 
    # Gets the summary analysis of a document
    api_response = api_instance.post(requestp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestp** | [**SummaryAnalysisRequest**](SummaryAnalysisRequest.md)|  | 

### Return type

[**AsyncResponseSummaryAnalysisResponse**](AsyncResponseSummaryAnalysisResponse.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

