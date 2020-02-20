from urllib.request import urlopen

f = open("app_ranking_list.json","wb")

response = urlopen("https://sensortower.com/api/ios/rankings/get_category_rankings?category=0&country=US&date=2020-02-20T00%3A00%3A00.000Z&device=IPHONE&limit=50&offset=0")
html = response.read()

f.write(html)
f.close()


