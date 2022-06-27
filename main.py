from utils import url_data, MAIN_URL, HEADERS, PROXIES, VERIFY_PATH, COLUMN_NAMES
import requests
import json
import pandas as pd
from datetime import datetime

def run():
    df = pd.DataFrame(columns=COLUMN_NAMES)

    for i in range(0,50):
        DATA = url_data(i)
        try:
            r = requests.post(url=MAIN_URL, 
                              headers=HEADERS, 
                              data=DATA,
                              proxies=PROXIES,
                              verify=VERIFY_PATH)
        except requests.exceptions.RequestException:
            print(f'Problem processing page {i}')
            continue

        res = json.loads(r.text)
        if len(res['results'][0]['hits']) == 0:
                print('No existing data')
                break

        for result in res['results'][0]['hits']:            
            name = result['name']
            headquarters = f'{result["hqProvince"]},{result["hqCountry"]}'
            certified_date = datetime.fromtimestamp(result['initialCertificationDateTimestamp']/1000)
            certified_since = f'{certified_date.strftime("%B")} {certified_date.strftime("%Y")}'
            industry = result['industry']
            website = f'{result["website"]}'

            row = [name, headquarters, certified_since, industry, website]
            new_df = pd.DataFrame([row], columns=COLUMN_NAMES)
            df = pd.concat([df, new_df], ignore_index=True)

    df.to_csv('bccorp_data.csv', index=False)

if __name__ == "__main__":
    run()