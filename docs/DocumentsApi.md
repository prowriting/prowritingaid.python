# swagger_client.DocumentsApi

All URIs are relative to *https://localhost:5004*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](DocumentsApi.md#create_document) | **POST** /api/documents | Create document
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /api/documents | Delete document
[**export_document**](DocumentsApi.md#export_document) | **GET** /api/documents/export | Export document
[**get_document**](DocumentsApi.md#get_document) | **GET** /api/documents/{id} | Get a document
[**get_document_list**](DocumentsApi.md#get_document_list) | **GET** /api/documents | Get user documents
[**update_document**](DocumentsApi.md#update_document) | **PUT** /api/documents/{id} | Update document
[**upload_document**](DocumentsApi.md#upload_document) | **POST** /api/documents/upload | Upload document file
[**upload_document_with_filename**](DocumentsApi.md#upload_document_with_filename) | **POST** /api/documents/upload/{fileName}/{extension} | Upload document file


# **create_document**
> UserDocument create_document(requestp)

Create document

Create a new document.

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
api_instance = swagger_client.DocumentsApi()
requestp = swagger_client.DocumentsRequest() # DocumentsRequest | Document to create

try: 
    # Create document
    api_response = api_instance.create_document(requestp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestp** | [**DocumentsRequest**](DocumentsRequest.md)| Document to create | 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(id)

Delete document

Delete a document.

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
api_instance = swagger_client.DocumentsApi()
id = 789 # int | ID of the document to delete

try: 
    # Delete document
    api_instance.delete_document(id)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the document to delete | 

### Return type

void (empty response body)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_document**
> file export_document(doc_id, extension, merge_original_document)

Export document

The resulting document file is streamed.

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
api_instance = swagger_client.DocumentsApi()
doc_id = 789 # int | ID of the document to export
extension = 'extension_example' # str | The file extension for the exported document
merge_original_document = true # bool | Specifies whether to merge with the original document file, to preserve formatting

try: 
    # Export document
    api_response = api_instance.export_document(doc_id, extension, merge_original_document)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->export_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **int**| ID of the document to export | 
 **extension** | **str**| The file extension for the exported document | 
 **merge_original_document** | **bool**| Specifies whether to merge with the original document file, to preserve formatting | 

### Return type

[**file**](file.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> UserDocument get_document(id)

Get a document

Gets a document by ID.

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
api_instance = swagger_client.DocumentsApi()
id = 789 # int | ID of the document to retrieve

try: 
    # Get a document
    api_response = api_instance.get_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the document to retrieve | 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_list**
> list[UserDocument] get_document_list()

Get user documents

Get an array with the user's documents.

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
api_instance = swagger_client.DocumentsApi()

try: 
    # Get user documents
    api_response = api_instance.get_document_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserDocument]**](UserDocument.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> update_document(id, document)

Update document

Update a document.

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
api_instance = swagger_client.DocumentsApi()
id = 789 # int | 
document = swagger_client.DocumentsRequest() # DocumentsRequest | Document update

try: 
    # Update document
    api_instance.update_document(id, document)
except ApiException as e:
    print("Exception when calling DocumentsApi->update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **document** | [**DocumentsRequest**](DocumentsRequest.md)| Document update | 

### Return type

void (empty response body)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document**
> UserDocument upload_document(file)

Upload document file

Upload a document file.

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
api_instance = swagger_client.DocumentsApi()
file = '/path/to/file.txt' # file | File to upload

try: 
    # Upload document file
    api_response = api_instance.upload_document(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->upload_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File to upload | 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_with_filename**
> UserDocument upload_document_with_filename(file_name, extension, file)

Upload document file

Upload a document file allowing the user to supply a file name.

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
api_instance = swagger_client.DocumentsApi()
file_name = 'file_name_example' # str | 
extension = 'extension_example' # str | 
file = '/path/to/file.txt' # file | File to upload

try: 
    # Upload document file
    api_response = api_instance.upload_document_with_filename(file_name, extension, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->upload_document_with_filename: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **extension** | **str**|  | 
 **file** | **file**| File to upload | 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[licenseCode](../README.md#licenseCode)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

