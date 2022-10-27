
import requests
import json
import coloredlogs, logging
coloredlogs.install()
 
def formatOutput(output):
 sourceName = output['source'][0]['annotations']['source_name']
 numOfYears = len(output['data']) 
 startYear = output['data'][numOfYears-1]['ID Year']
 endYear = output['data'][0]['ID Year']
 population = output['data']
 peak = 0
 for count in range(0, (len(population)-1)):
    growth = population[count]['Population']- population[count+1]['Population']
    if growth > peak:
       peak = growth
       year = population[count]['ID Year']
       peakValue = (peak/population[count]['Population'])*100
    else:
        lowest = growth  
        lowestyear = population[count]['ID Year']
        lowestValue = (lowest/population[count]['Population'])*100  

 logging.info("According to %s, in %s years from %s to %s,peak population growth was %s in %s and lowest population increase was %s in %s."
     %(sourceName,numOfYears,startYear,endYear,f"{round(peakValue,2)}%",year,f"{round(lowestValue,2)}%",lowestyear))

URL = "https://datausa.io/api/data?drilldowns=Natio&measures=Population"

response = requests.get(url=URL)
outputres = json.loads(response.text)
if response.status_code >= 300 or len(outputres['data']) == 0:
    logging.error(f"Please check the API.Status code is {response.status_code} and response contains empty value.")
    raise Exception ()    
else:    
  
  formatOutput(outputres)

