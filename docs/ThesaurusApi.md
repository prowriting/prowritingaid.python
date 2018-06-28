# ProWritingAidSDK.ThesaurusApi

All URIs are relative to *https://api.prowritingaid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post**](ThesaurusApi.md#post) | **POST** /api/thesaurus | Returns the thesaurus entries for a specific word


# **post**
> ThesaurusResponse post(request)


Returns the thesaurus entries for a specific word

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
api_instance = ProWritingAidSDK.ThesaurusApi()
request = ProWritingAidSDK.ThesaurusRequest() # ThesaurusRequest | 

try: 
    # Returns the thesaurus entries for a specific word
    api_response = api_instance.post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThesaurusApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ThesaurusRequest**](ThesaurusRequest.md)|  | 

### Return type

[**ThesaurusResponse**](ThesaurusResponse.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

