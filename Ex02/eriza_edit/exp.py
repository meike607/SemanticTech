from bs4 import BeautifulSoup
import pycurl
from io import BytesIO
c = pycurl.Curl()
c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0")
buffer = BytesIO()
c.setopt(c.WRITEFUNCTION, buffer.write)
c.setopt(c.URL, "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html")
try:
    c.perform()
except pycurl.error as error:
    print("Curl perform failed: " + str(error))
responseCode = c.getinfo(c.RESPONSE_CODE)
if responseCode != 200:
    print("Response Code is not ok")
soup = BeautifulSoup(buffer.getvalue(), 'html.parser')
allTableEntries = soup.find("table").find("tbody").find_all("tr")
for entry in allTableEntries:
    allColumns = entry.find_all("td")
    name = allColumns[0]
    if(str(name.string) == "Gesamt"):
      print("there are a total of " + str(allColumns[1].string) + " infections.")
