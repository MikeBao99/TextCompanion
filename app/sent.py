import json
from watson_developer_cloud import ToneAnalyzerV3

colors = {'Anger':'#FF8F8F', 'Confident':'#FFDB8F', 'Analytical':'#8FF6FF', 'Fear':'#8FFF99', 'Tentative':'#FF8FFB', 'Sadness':'#8FB6FF', 'Joy':'#FDFF8F'}

def colorText(text):
  tone_analyzer = ToneAnalyzerV3(
      version ='2017-09-21',
      username ='f163ce1a-be0a-4dd8-93f8-17b1b02cc209',
      password ='OUcpFH7JH8rT'
  )
  content_type = 'application/json'

  tone = tone_analyzer.tone({"text": text},content_type)
  ans = ""
  for sentence in tone['sentences_tone']:
    if len(sentence['tones']) > 0:
      ans += colorSentence(sentence['text'], sentence['tones'][0]['tone_name'])
    else:
      ans += sentence['text']
    ans+= ' '
  return ans

def colorSentence(sentence, emotion):
	return('<FONT style=\"BACKGROUND-COLOR: ' + colors[emotion] + '\">' + sentence + "</FONT>")
