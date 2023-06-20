import json
import fileinput
import sys
import base64

# USAGE: ./TS-HAR-Parse.py file.har output.ts
# A small utility to parse streaming files from received network traffic in a Google Chrome HAR file: https://support.google.com/admanager/answer/10358597?hl=en
# File can be translated from .ts to .mp3 with "ffmpeg -i file-in.ts file-out.mp3"
# Lots of comments below to assist with learning notes + future dev

# open the HAR file
f = open(sys.argv[1])
j = json.load(f)

######################################
# Some notes on JSON access below
# ACCESS REQUESTED URL
#print(j['log']['entries'][1]['request']['url'])
# ACCESS RESPONSE MIMETYPE
#print(j['log']['entries'][1]['response']['content']['mimeType'])
# ACCESS RESPONSE CONTENT
#print(j['log']['entries'][1]['response']['content']['text'])
# DECODE & SAVE RESPONSE CONTENT
#c = j['log']['entries'][1]['response']['content']['text']
#r = base64.b64decode(c)
#o = open("test.ts", "wb")
#o.write(r)
#o.close()
# LOOP OVER INDEXES WITHIN A JSON STRUCTURE
# for i in j['log']['entries']:
# print(i['response']['content']['mimeType'])
# This is because the content of the index gets saved to i, and we must then access sub-keys within i. Splits up the JSON access visually.
######################################

# open file for output
o = open(sys.argv[2], "wb")

# check if the entry is for video/mp2t content
for i in j['log']['entries']:
if i['response']['content']['mimeType'] == "video/mp2t":

# base64 decode content
c = i['response']['content']['text']
r = base64.b64decode(c)

# append the chunks to the output file, as .ts is a streaming format & can be concatenated
o.write(r)
o.close()
