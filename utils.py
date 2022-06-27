import os 

HEADERS = {
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.bcorporation.net',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'bx1p6tr71m-dsn.algolia.net',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
        AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    # 'Content-Length': '398',
    'Accept-Language': 'es-419,es;q=0.9',
    'Connection': 'keep-alive',
}

MAIN_URL = 'https://bx1p6tr71m-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.11.0)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.40.6)%3B%20react%20(17.0.2)%3B%20react-instantsearch%20(6.26.0)%3B%20react-instantsearch-hooks%20(6.26.0)%3B%20JS%20Helper%20(3.8.2)&x-algolia-api-key=51a96f5c236cb12087a548630ebecc79&x-algolia-application-id=BX1P6TR71M'

def url_data(page_num) -> str:
    URL_DATA = '{"requests":[{"indexName":"companies-production-en-us-latest-certification-desc","params":"query=&maxValuesPerFacet=500&hitsPerPage=25&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page='+ str(page_num) +'&facets=%5B%22bftwCategories%22%2C%22bftwYears%22%2C%22bftwCategoryYears%22%2C%22countries%22%2C%22hqCountry%22%2C%22demographicsList%22%2C%22size%22%2C%22industry%22%5D&tagFilters="}]}'
    return URL_DATA

PROXY_HOST = "proxy.zyte.com"
PROXY_PORT = "8011"
### Get your own zyte key at https://www.zyte.com
PROXY_AUTH = f'{os.getenv("ZYTE_KEY")}:' # Make sure to include ':' at the end

PROXIES = {"https": "http://{}@{}:{}/".format(PROXY_AUTH, PROXY_HOST, PROXY_PORT),
           "http": "http://{}@{}:{}/".format(PROXY_AUTH, PROXY_HOST, PROXY_PORT)}

### Get your own zyte certificate at https://www.zyte.com
VERIFY_PATH = './zyte-smartproxy-ca.crt' ## Already added to .gitignore :P 

COLUMN_NAMES = ["name", 
                "headquarters", 
                "certified_since", 
                "industry", 
                "website"]
