# UserDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the document | [optional] 
**created** | **datetime** | Document creation date/time | [optional] 
**id** | **int** | Document ID | [optional] 
**content** | **str** | Document contents, as HTML or text (see ContentType) | [optional] 
**content_type** | **str** | Document content type: \&quot;T\&quot; for text, null or empty for HTML | [optional] 
**preview** | **str** | Preview of the document content, as text | [optional] 
**last_modified** | **datetime** | Date/time of the last document modification | [optional] 
**document_id** | **str** | Internal document ID (GUID) | [optional] 
**document_type** | **str** | Internal document Type (string) | [optional] 
**auto_save_last_modified** | **datetime** | Date/time of the last document auto save | [optional] 
**grammar_score** | **int** | Grammar score | [optional] 
**style_score** | **int** | Style score | [optional] 
**spelling_score** | **int** | Spelling score | [optional] 
**term_score** | **int** | Term score | [optional] 
**overall_score** | **int** | Overall score, based on the previous scores | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


