# ProWritingAidSDK.TextApi

All URIs are relative to *https://api.prowritingaid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](TextApi.md#get) | **GET** /api/async/text/result/{taskId} | Tries to get the result of a request using the task id of the request
[**post**](TextApi.md#post) | **POST** /api/async/text | Analyses text and returns tags for it


# **get**
> AsyncResponseTextAnalysisResponse get(task_id)


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
api_instance = ProWritingAidSDK.TextApi()
task_id = 'task_id_example' # str | 

try: 
    # Tries to get the result of a request using the task id of the request
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


Analyses a text document and returns tags for it  <br /><br /><br /><table><tr><th>Report Name</th><th>Status</th><th>Description</th></tr><tr><td>acronym</td><td>Live</td><td>Shows all the acronyms in your writing and highlights where they haven't been defined, or have been defined after the first occurrence, or have been defined multiple times..</td></tr><tr><td>alliteration</td><td>Live</td><td>Highlights alliterations in your writing. Alliterations are a linguistic tool used by some writers for effect..</td></tr><tr><td>allrepeats</td><td>Development</td><td>Highlights words and phrases that you've used repeatedly in your text.</td></tr><tr><td>allsentences</td><td>Live</td><td>Shows a visual representation of the sentences lengths of your writing. Try and vary the sentence lengths to maintain the interest of the reader..</td></tr><tr><td>bully</td><td>Development</td><td>Highlights bullying and vulgar language in your text..</td></tr><tr><td>cliche</td><td>Live</td><td>Scours your work for cliches and highlights them. Nobody likes to read a cliche so best to avoid them. Redundant expressions can also be removed as they say the same thing twice..</td></tr><tr><td>closerepeat</td><td>Development</td><td>Highlights any words and phrases that you have repeated within a short space of writing. Try and think of something else to say..</td></tr><tr><td>complex</td><td>Live</td><td>Highlights complex words in your writing. Words are broken down by number of syllables..</td></tr><tr><td>consistency</td><td>Live</td><td>Highlights inconsistency in your text. Picking up inconsistencies in your text can be one of the hardest editing tasks..</td></tr><tr><td>core</td><td>Development</td><td>Core findings.</td></tr><tr><td>coreplus</td><td>Development</td><td>Core findings.</td></tr><tr><td>corporate</td><td>Live</td><td>Highlights uses of corporate wording that can be simplified to clarify your document..</td></tr><tr><td>dialog</td><td>Live</td><td>Highlights the dialogue tags in your text. Editors prefer minimal use of all dialogue tags (except for 'said')..</td></tr><tr><td>diction</td><td>Live</td><td>Provides a list of possible diction problems and suggestions on how you might revise them..</td></tr><tr><td>dva</td><td>Live</td><td>Highlights diction problems, vague and abstract words in your text..</td></tr><tr><td>eloquence</td><td>Live</td><td>Designed to help you develop your use of stylistic writing techniques such as alliteration, epistrophe, and hendiadys. The items in this report are not suggestions, just aids to help you along the way..</td></tr><tr><td>grammar</td><td>Live</td><td>Checks your text for grammar errors and potential word mis-use..</td></tr><tr><td>grammarplus</td><td>Live</td><td>Checks your text for grammar errors and potential word mis-use..</td></tr><tr><td>homonym</td><td>Live</td><td>Helps you check for incorrect word usage. Homonyms are words which sound alike yet are spelled differently. For example: there, their and they're or raw and roar..</td></tr><tr><td>house</td><td>Development</td><td>A blank report for you to create your own patterns in. Ideal for a house style. Go to the settings screen to set-up your own patterns. .</td></tr><tr><td>initial</td><td>Live</td><td>Highlights the initial pronouns in your text. Repetitive use of initial pronouns can lead to boring text, e.g. He did this. He did that. He did another thing..</td></tr><tr><td>nlp</td><td>Development</td><td>Our NLP Predicate Words report allows you to easily identify the key modality or representation system of a piece of text. If you are analyzing a document written by someone else then this will give you an idea of their preferred representational system. This may help you tailor your writing in order to build rapport. If you don't know the modality of your reader then try to use a balance of words from each modality. This will broaden the appeal of your writing..</td></tr><tr><td>overused</td><td>Live</td><td>Compares the frequency of commonly overused words in your text to published writing to give you an indication of where you may be over-using words..</td></tr><tr><td>overusedonly</td><td>Live</td><td>Compares the frequency of commonly overused words in your text to published writing to give you an indication of where you may be over-using words..</td></tr><tr><td>overview</td><td>Live</td><td>Gives you an overview of the key metrics for your document..</td></tr><tr><td>pacing</td><td>Live</td><td>Identifies the slower paced parts of your manuscript, such as introspection and backstory so you can spread them out. Try not to have too many slower paced paragraphs in a row as this can get boring..</td></tr><tr><td>paragraph_readability</td><td>Live</td><td>Shows you the relative readability of each paragraph in your text..</td></tr><tr><td>passive</td><td>Live</td><td>Highlights areas where your writing style might be improved, such as use of passive and hidden verbs..</td></tr><tr><td>phrases</td><td>Live</td><td>Provides a summary of all the phrases that you have repeated in your writing. Try and cut down on repeats..</td></tr><tr><td>plagiarism</td><td>Live</td><td>Identifies parts of your text that occur in other documents. Scans millions of web-pages, books, and academic papers..</td></tr><tr><td>plength</td><td>Live</td><td>A visual representation of the paragraph lengths of your writing. Avoid writing more than five or six sentences in a paragraph. Also try to avoid too many short paragraphs..</td></tr><tr><td>preadability</td><td>Live</td><td>Provides a series of readability measures for your text so you can determine if it is suitable for your intended audience..</td></tr><tr><td>readability</td><td>Live</td><td>Provides a series of readability measures for your text so you can determine if it is suitable for your intended audience..</td></tr><tr><td>sentiment</td><td>Live</td><td>Shows a histogram of the sentiment in your story so you can monitor large swings..</td></tr><tr><td>sentimentwords</td><td>Development</td><td>Highlights words that have a sentiment bias in your text, and grades them..</td></tr><tr><td>seo</td><td>Development</td><td>Shows how yout text can be optimized to appear higher in Google rankings..</td></tr><tr><td>slength</td><td>Live</td><td>Shows a visual representation of the sentences lengths of your writing. Try and vary the sentence lengths to maintain the interest of the reader..</td></tr><tr><td>ssentences</td><td>Live</td><td>Shows sticky sentences in your writing. Sticky sentences slow your reader down; try to avoid them..</td></tr><tr><td>ssentences_noglue</td><td>Live</td><td>Shows sticky sentences in your writing. Sticky sentences slow your reader down; try to avoid them..</td></tr><tr><td>structure</td><td>Live</td><td>Highlights the key structure of a document such as sentences and paragraphs..</td></tr><tr><td>thesaurus</td><td>Beta</td><td>Shows possible replacements for nouns, verbs, adjectives and adverbs..</td></tr><tr><td>time</td><td>Live</td><td>Highlights any temporal references in your text so you can check for inconsistency and view the time-line of your text..</td></tr><tr><td>topics</td><td>Live</td><td>Suggested topics that are related to the subject matter of your text..</td></tr><tr><td>transition</td><td>Live</td><td>Highlights the transitions in your report. Transitions help organize ideas. Writing that is short on transitions is often hard to follow. Non-fiction writing that has under 1 transition per 4 sentences tends to be less understandable..</td></tr><tr><td>vague</td><td>Live</td><td>Provides a list of words that may be considered vague or abstract. Consider strengthening them..</td></tr><tr><td>wordcloud</td><td>Live</td><td>Shows you a word cloud of the most commonly occuring words in your text..</td></tr><tr><td>wordsandphrases</td><td>Deprecated</td><td>Highlights any words and phrases that you have repeated within a short space of writing. Try and think of something else to say..</td></tr><tr><td>wordsphrases</td><td>Live</td><td>Highlights any words and phrases that you have repeated within a short space of writing. Try and think of something else to say..</td></tr></table>

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
api_instance = ProWritingAidSDK.TextApi()
requestp = ProWritingAidSDK.TextAnalysisRequest() # TextAnalysisRequest | 

try: 
    # Analyses text and returns tags for it
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

