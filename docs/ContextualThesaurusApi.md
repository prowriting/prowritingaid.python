# ProWritingAidSDK.ContextualThesaurusApi

All URIs are relative to *https://localhost:5004*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ContextualThesaurusApi.md#get) | **GET** /api/async/contextualthesaurus/result/{taskId} | Tries to get the result of a request using the task id of the request
[**post**](ContextualThesaurusApi.md#post) | **POST** /api/async/contextualthesaurus | Analyses text and returns contextual thesaurus entries


# **get**
> AsyncResponseContextualThesaurusResponse get(task_id)


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
api_instance = ProWritingAidSDK.ContextualThesaurusApi()
task_id = 'task_id_example' # str | 

try: 
    # Tries to get the result of a request using the task id of the request
    api_response = api_instance.get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextualThesaurusApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**AsyncResponseContextualThesaurusResponse**](AsyncResponseContextualThesaurusResponse.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> AsyncResponseContextualThesaurusResponse post(requestp)


Analyses text and returns contextual thesaurus entries

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
api_instance = ProWritingAidSDK.ContextualThesaurusApi()
requestp = ProWritingAidSDK.ContextualThesaurusRequest() # ContextualThesaurusRequest | 

try: 
    # Analyses text and returns contextual thesaurus entries
    api_response = api_instance.post(requestp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextualThesaurusApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestp** | [**ContextualThesaurusRequest**](ContextualThesaurusRequest.md)|  | 

### Return type

[**AsyncResponseContextualThesaurusResponse**](AsyncResponseContextualThesaurusResponse.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

