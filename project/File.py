from datetime import time

from googlesearch import search
result=list(search("אוטובוס קרוב קו 10 תל שבע"))
print(result)



from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
url=result[2]
client = Request(url, headers={"User-Agent" : "Mozilla/5.0"})

page = urlopen(client).read()
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
k=soup.find_all("input")
#print(k)
companies = [com.text for com in soup.find_all('b')]
#print(companies)
# city_state0 = []
# city_state1 = []
# for p in soup.find_all('p', {'class': 'location'}):
#     city_state0.append(p.text.split(',')[0].strip())
#     city_state1.append(p.text.split(',')[1].strip())
#
# df = pd.DataFrame({
#     'city_state1': city_state0,
#     'city_state2': city_state1,
#     'companies': companies,
#     'positions': positions
# })
