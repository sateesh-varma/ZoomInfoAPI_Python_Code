import requests
class zoomInfo_company_contacts:
    def __init__(self,token) -> None:
        self.token=token
        self.baseUrl = 'https://api.zoominfo.com/'
        self.relativeUrl='search/contact'
        self.rpp=100  
        pass
    def get_company_contacts(self,companyid:str,page:int=1):
         headers = {'Authorization': f"Bearer {self.token}", 'Accept': "application/json", 'user-agent': ""}
         request_body = { "companyId": companyid,"rpp":self.rpp,"page":page}          
         response = requests.post(self.baseUrl+self.relativeUrl, headers=headers, json=request_body)
         if not response.ok:
            raise RuntimeError(response.text)
         return response.text
        
        