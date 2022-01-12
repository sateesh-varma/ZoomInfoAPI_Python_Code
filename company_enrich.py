import json
import jwt
from ZoomInfo_Company_Enrich import ZoomInfo_Company_Enrich
from company_enrich_result_item import companyEnrichItemResult

class companyEnrich:
    def __init__(self,token:str) -> None:
        self.token=token
        pass
    
    def company_enrich_details(self,companyId:str):
        ZoomInfo_Company_Enrich_client = ZoomInfo_Company_Enrich(self.token)
        enrich_result =  ZoomInfo_Company_Enrich_client.get_company_enrich(companyId)
        converted_enrich_data = companyEnrichItemResult.from_json(enrich_result)
        result= converted_enrich_data.data['result']
        return result
        
        