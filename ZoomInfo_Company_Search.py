 
import requests

class ZoomInfo_Company_Search:
    def __init__(self,token):
        self.token = token
        self.baseUrl='https://api.zoominfo.com/'
        self.relativeUrl = 'search/company'
        
    def do_company_search(self,searchKey:str,page_num:int=1):
         max_results_per_request =100
         headers = {'Authorization': f"Bearer {self.token}", 'Accept': "application/json", 'user-agent': ""}
        # response = requests.post(self.baseUrl+self.relativeUrl, headers=headers)
         request_body = { "companyName": searchKey, 'page':page_num,'rpp':max_results_per_request,'sortBy':'name','sortOrder':'asc'}          
         response = requests.post(self.baseUrl+self.relativeUrl, headers=headers, json=request_body)
         if not response.ok:
            raise RuntimeError(response.text)
         return response.text
        
        
    
    

    
    