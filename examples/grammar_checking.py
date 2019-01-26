import nltk
import bs4
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
from pprint import pprint

configuration = ProWritingAidSDK.Configuration()
configuration.host = 'https://api.prowritingaid.com'
configuration.api_key['licenseCode'] = '225C39C4-BC23-43EC-ADC1-3B66E6229363'

# create an instance of the API class
api_instance = ProWritingAidSDK.TextApi(ProWritingAidSDK.ApiClient('https://api.prowritingaid.com'))

wrong_sent = 'He hope that he woll be here.'

try:
    api_request = ProWritingAidSDK.TextAnalysisRequest(wrong_sent,
                                                       ["grammar"],
                                                       "General",
                                                       "en")
    api_response = api_instance.post(api_request)
    
except ApiException as e:
    print("Exception when calling TextAnalysisRequest->get: %s\n" % e)
tags = api_response.result.tags
correct_sentence = wrong_sent
# Apply all the tags to the original string to get a corrected string 
# Important to work through the tags backward to that indexes don't change
for tag in reversed(tags):
    replacement = '' if tag.suggestions[0] == '(omit)' else tag.suggestions[0] 
    correct_sentence = correct_sentence[0:tag.start_pos] + replacement + correct_sentence[tag.end_pos+1:]
print('Incorrect Sentence')
print(wrong_sent)
print('Correct Sentence')
print(correct_sentence)
print('Done')