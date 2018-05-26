import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version ='2017-09-21',
    username ='f163ce1a-be0a-4dd8-93f8-17b1b02cc209',
    password ='OUcpFH7JH8rT'
)

text = str(input("Enter text: \n"))
content_type = 'application/json'

tone = tone_analyzer.tone({"text": text},content_type)

print(json.dumps(tone, indent=2))
