import math
from company_contact_result_item import company_contact_item
import json
from zoominfo_company_contacts import zoomInfo_company_contacts

class company_contacts:
    def __init__(self,token) -> None:
        self.token=token        
        pass
    
    def ge_company_contacts(self,compantId:str):
        max_result_per_request =100        
        zoomInfo_company_contacts_client = zoomInfo_company_contacts(self.token)
        result = company_contact_item.from_dict(json.loads(zoomInfo_company_contacts_client.get_company_contacts(compantId)))
        company_contacts=[]
        for c in result.data:
            company_contacts.append(c)
        if(result.max_results > max_result_per_request):
             batches:int =0
             batches= math.ceil(result.max_results / max_result_per_request)
             for index in range(batches):
                temp = index +1
                if temp > 1:
                    search_result = zoomInfo_company_contacts_client.get_company_contacts(compantId,temp)
                    converted_data = company_contact_item.from_dict(json.loads(search_result))
             for u in converted_data.data:
                 company_contacts.append(u)           
        return company_contacts