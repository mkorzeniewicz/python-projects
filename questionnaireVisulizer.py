import json
from builtins import print
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def getUnixTimestamp(stringDateTimestamp):
    return datetime.strptime(stringDateTimestamp, DATE_FORMAT).timestamp()


initialJson = '{"qnSet":[{"id":"7a352577-9795-4ef7-8be6-78af05930a4a","name":"CarQuestionnaireSet","extVersion":"A","startDate":"2021-01-01 12:00:00","endDate":"2022-01-01 12:00:00","state":"final"},{"id":"7a352577-9795-4ef7-8be6-78af05930a4a","name":"CarQuestionnaireSet","extVersion":"B","startDate":"2022-01-01 12:00:00","endDate":"2024-01-01 12:00:00","state":"final"},{"id":"7a352577-9795-4ef7-8be6-78af05930a4a","name":"CarQuestionnaireSet","extVersion":"C","startDate":"2024-01-01 12:00:00","endDate":"2026-01-01 12:00:00","state":"final"}]}'

#print(initialJson)

response = json.loads(initialJson)['qnSet']

noMeta = len(response)
print("Found ", noMeta, " sets")
print("Sets name ", response[0]['name'])

earliestUT = getUnixTimestamp(response[0]['startDate'])
latestUT = 0

boxesTimeRange = []

for meta in response:
    startUT = getUnixTimestamp(meta['startDate'])
    endUT = getUnixTimestamp(meta['endDate'])

    boxesTimeRange.append(endUT - startUT)

    if startUT < earliestUT:
        earliestUT = startUT

    if endUT > latestUT:
        latestUT = endUT

    print(startUT)
    print(endUT)
    print()

print("earliest ", earliestUT)
print("latest ", latestUT)
print()

chartRange = latestUT - earliestUT
print("chartRange: ", chartRange)

chartUXWidth = 200
pixelTimeRatio = chartRange/chartUXWidth

print("pixelTimeRatio: ", pixelTimeRatio)

boxesPixelRanges = []

for box in boxesTimeRange:
    boxesPixelRanges.append(round(box/pixelTimeRatio))

print(boxesPixelRanges)


