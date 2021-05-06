# ProWritingAidSDK
Official ProWritingAid API Version 2

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2
- Package version: 2.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://prowritingaid.com/en/App/API#python](https://prowritingaid.com/en/App/API#python)

## Requirements.

Python 2.7 or 3.4+

## Installation & Usage
### pip install

The python package is hosted on Github. You can install directly from Github.

```sh
pip install git+https://github.com/prowriting/prowritingaid.python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/prowriting/prowritingaid.python.git`)

Then import the package:
```python
import ProWritingAidSDK 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ProWritingAidSDK
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
from pprint import pprint

configuration = ProWritingAidSDK.Configuration()
configuration.host = 'https://api.prowritingaid.com'
configuration.api_key['licenseCode'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = ProWritingAidSDK.TextApi(ProWritingAidSDK.ApiClient('https://api.prowritingaid.com'))

try:
    api_request = ProWritingAidSDK.TextAnalysisRequest("I place my cane firmly on the ground and, slowly, with its aid, "
                                                       "I lower myself from the hammock. Now the rains have gone my joints "
                                                       "don't hurt so badly. Today won't be too bad, I think. I'm prone to "
                                                       "be over optimistic. Could this be my last day. At this time the jungle "
                                                       "is strangely subdued. She poke around in the ashes. Every day the "
                                                       "weariness is even worst than beofre. I don't know yett. \n"
                                                       "Whne? What a weka statement. Jaroslav Drabny is a Czech football goalkeeper. "
                                                       "Bhuvnehwar Kumar is a Czech football goalkeeper. I just saw Siyabonga Siyo. "
                                                       "I just saw Siyabonga Seyo. I read this article on RaelSport.",
                                                       ["grammar"],
                                                       "General",
                                                       "en")
    api_response = api_instance.post(api_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling API: %s\n" % e)
```

## Examples

- [Example of correcting a sentence using our grammar checking API](docs/grammar_checking.py). 

## Documentation for API Endpoints

All URIs are relative to *https://api.prowritingaid.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContextualThesaurusApi* | [**get**](docs/ContextualThesaurusApi.md#get) | **GET** /api/async/contextualthesaurus/result/{taskId} | Tries to get the result of a request using the task id of the request
*ContextualThesaurusApi* | [**post**](docs/ContextualThesaurusApi.md#post) | **POST** /api/async/contextualthesaurus | Analyses text and returns contextual thesaurus entries
*HtmlApi* | [**get**](docs/HtmlApi.md#get) | **GET** /api/async/html/result/{taskId} | Tries to get the result of a request using the task id of the request
*HtmlApi* | [**post**](docs/HtmlApi.md#post) | **POST** /api/async/html | Analyses HTML and adds suggestion tags to it
*SummaryApi* | [**get**](docs/SummaryApi.md#get) | **GET** /api/async/summary/result/{taskId} | Tries to get the result of a request using the task id of the request
*SummaryApi* | [**post**](docs/SummaryApi.md#post) | **POST** /api/async/summary | Gets the summary analysis of a document
*TextApi* | [**get**](docs/TextApi.md#get) | **GET** /api/async/text/result/{taskId} | Tries to get the result of a request using the task id of the request
*TextApi* | [**post**](docs/TextApi.md#post) | **POST** /api/async/text | Analyses text and returns tags for it
*ThesaurusApi* | [**post**](docs/ThesaurusApi.md#post) | **POST** /api/thesaurus | Returns the thesaurus entries for a specific word
*WordCloudApi* | [**get**](docs/WordCloudApi.md#get) | **GET** /api/async/wordcloud/result/{taskId} | Tries to get the result of a request using the task id of the request
*WordCloudApi* | [**post**](docs/WordCloudApi.md#post) | **POST** /api/async/wordcloud | Analyses text and returns a word cloud (as an image)


## Documentation For Models

 - [AnalysisSettings](docs/AnalysisSettings.md)
 - [AnalysisSummary](docs/AnalysisSummary.md)
 - [AnalysisSummaryGraph](docs/AnalysisSummaryGraph.md)
 - [AnalysisSummaryGraphItem](docs/AnalysisSummaryGraphItem.md)
 - [AnalysisSummaryItem](docs/AnalysisSummaryItem.md)
 - [AnalysisSummarySubItem](docs/AnalysisSummarySubItem.md)
 - [AsyncResponseContextualThesaurusResponse](docs/AsyncResponseContextualThesaurusResponse.md)
 - [AsyncResponseHtmlAnalysisResponse](docs/AsyncResponseHtmlAnalysisResponse.md)
 - [AsyncResponseSummaryAnalysisResponse](docs/AsyncResponseSummaryAnalysisResponse.md)
 - [AsyncResponseTextAnalysisResponse](docs/AsyncResponseTextAnalysisResponse.md)
 - [AsyncResponseWordCloudResponse](docs/AsyncResponseWordCloudResponse.md)
 - [ContextualThesaurusRequest](docs/ContextualThesaurusRequest.md)
 - [ContextualThesaurusResponse](docs/ContextualThesaurusResponse.md)
 - [DocTag](docs/DocTag.md)
 - [EntryMeaning](docs/EntryMeaning.md)
 - [HtmlAnalysisRequest](docs/HtmlAnalysisRequest.md)
 - [HtmlAnalysisResponse](docs/HtmlAnalysisResponse.md)
 - [SuggestionCategory](docs/SuggestionCategory.md)
 - [SummaryAnalysisRequest](docs/SummaryAnalysisRequest.md)
 - [SummaryAnalysisResponse](docs/SummaryAnalysisResponse.md)
 - [TextAnalysisRequest](docs/TextAnalysisRequest.md)
 - [TextAnalysisResponse](docs/TextAnalysisResponse.md)
 - [ThesaurusRequest](docs/ThesaurusRequest.md)
 - [ThesaurusResponse](docs/ThesaurusResponse.md)
 - [WordCloudRequest](docs/WordCloudRequest.md)
 - [WordCloudResponse](docs/WordCloudResponse.md)


## Documentation For Authorization


## licenseCode

- **Type**: API key
- **API key parameter name**: licenseCode
- **Location**: HTTP header


## Author

prowritingaid.com

