
import requests
link = "https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E7%88%AC%E8%99%AB&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22489%22,%22kw%22:%22%E7%88%AC%E8%99%AB%22,%22kt%22:%223%22%7D"
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
r = requests.get(link, headers= headers)
print (r.text)