# ProWritingAidSDK.WordCloudApi

All URIs are relative to *https://localhost:5004*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](WordCloudApi.md#get) | **GET** /api/async/wordcloud/result/{taskId} | Tries to get the result of a request using the task id of the request
[**post**](WordCloudApi.md#post) | **POST** /api/async/wordcloud | Analyses text and returns a word cloud (as an image)


# **get**
> AsyncResponseWordCloudResponse get(task_id)


Tries to get the result of a request using the task id of the request

### Example 
```python
from __future__ import print_function
import time
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ProWritingAidSDK.WordCloudApi()
task_id = 'task_id_example' # str | 

try: 
    # Tries to get the result of a request using the task id of the request
    api_response = api_instance.get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordCloudApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**AsyncResponseWordCloudResponse**](AsyncResponseWordCloudResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> AsyncResponseWordCloudResponse post(requestp)


Analyses text and returns a word cloud (as an image)

### Example 
```python
from __future__ import print_function
import time
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ProWritingAidSDK.WordCloudApi()
requestp = ProWritingAidSDK.WordCloudRequest() # WordCloudRequest | 

try: 
    # Analyses text and returns a word cloud (as an image)
    api_response = api_instance.post(requestp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordCloudApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestp** | [**WordCloudRequest**](WordCloudRequest.md)|  | 

### Return type

[**AsyncResponseWordCloudResponse**](AsyncResponseWordCloudResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

