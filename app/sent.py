import json
from watson_developer_cloud import ToneAnalyzerV3

colors = {'Anger':'#FFE0E6', 'Confident':'#FEE7C1', 'Analytical':'#EBE1FE', 'Fear':'#DCF2F2', 'Tentative':'#FFEEFE', 'Sadness':'#D8ECFA', 'Joy':'#FFF5DF'}

def colorText(text):
  tone_analyzer = ToneAnalyzerV3(
      version ='2017-09-21',
      username ='f163ce1a-be0a-4dd8-93f8-17b1b02cc209',
      password ='OUcpFH7JH8rT'
  )
  content_type = 'application/json'

  tone = tone_analyzer.tone({"text": text},content_type)
  ans = ""
  try:
    for sentence in tone['sentences_tone']:
      if len(sentence['tones']) > 0:
        ans += colorSentence(sentence['text'], sentence['tones'][0]['tone_name'])
      else:
        ans += sentence['text']
      ans+= ' '
  except:
    ans = text
  return ans

sents = ["Anger", "Sadness", "Joy", "Fear", "Analytical", "Confident", "Tentative"]
def sentList(text):
  tone_analyzer = ToneAnalyzerV3(
      version ='2017-09-21',
      username ='f163ce1a-be0a-4dd8-93f8-17b1b02cc209',
      password ='OUcpFH7JH8rT'
  )
  content_type = 'application/json'

  tone = tone_analyzer.tone({"text": text},content_type)
  sentiments = [0,0,0,0,0,0,0]
  for sentiment in range(len(sents)):
    for senti in tone['document_tone']['tones']:
      if senti['tone_name'] == sents[sentiment]:
        sentiments[sentiment] = senti['score']
  return sentiments

def colorSentence(sentence, emotion):
	return('<FONT style=\"BACKGROUND-COLOR: ' + colors[emotion] + '\">' + sentence + "</FONT>")
