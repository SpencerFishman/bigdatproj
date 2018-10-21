import json
fileName = 'test.json'

testData = '[{"Cardinals":["2012":{"stadium":"UniversityofPhoenixStadium","lat":"33.5276","long":"-112.2626"},"2013":{"stadium":"UniversityofPhoenixStadium","lat":"33.5276","long":"-112.2626"},"2014":{"stadium":"UniversityofPhoenixStadium","lat":"33.5276","long":"-112.2626"},"2015":{"stadium":"UniversityofPhoenixStadium","lat":"33.5276","long":"-112.2626"},"2016":{"stadium":"UniversityofPhoenixStadium","lat":"33.5276","long":"-112.2626"}],"Falcons":["2012":{"stadium":"GeorgiaDome","lat":"33.7577","long":"-84.4008"},"2013":{"stadium":"GeorgiaDome","lat":"33.7577","long":"-84.4008"},"2014":{"stadium":"GeorgiaDome","lat":"33.7577","long":"-84.4008"},"2015":{"stadium":"GeorgiaDome","lat":"33.7577","long":"-84.4008"},"2016":{"stadium":"GeorgiaDome","lat":"33.7577","long":"-84.4008"}]}]'

jData = json.loads(testData)

for doc in jData:
    for key, value in doc.items():
        print (key, value)

print (jData[0])
