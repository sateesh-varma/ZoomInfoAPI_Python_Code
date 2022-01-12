import requests

class ZoomInfo_Company_Enrich:
    def __init__(self,token) -> None:
        self.token = token
        self.baseUrl='https://api.zoominfo.com/'
        self.relativeUrl='enrich/company'
    
    def get_company_enrich(self,companyid:str):         
         headers = {'Authorization': f"Bearer {self.token}", 'Accept': "application/json", 'user-agent': ""}
        # response = requests.post(self.baseUrl+self.relativeUrl, headers=headers)
         request_body = ''' 
         {
            "matchCompanyInput": 
            [
    	        {
    		    "companyId": '''+companyid+'''    		 
        	    }
            ],
            "outputFields":
            [
                "id",
                "name",
                "numberOfContactsInZoomInfo",
                "website",
                "state",
                "city",
                "domainlist"
             ]
        }'''   
         response = requests.post(self.baseUrl+self.relativeUrl, headers=headers, data=request_body)
         if not response.ok:
            raise RuntimeError(response.text)
         return response.text
        
        
    