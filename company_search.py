import math
from ZoomInfo_Company_Search import ZoomInfo_Company_Search
from company_result_item import company_search_result
import json


class companySearch:
    def __init__(self,token:str) -> None:
        self.token=token
        pass
    
    def perfom_search(self,searchKey:str):
        search_term=searchKey   
        max_result_per_request =100
        ZoomInfo_Company_Search_client =  ZoomInfo_Company_Search(self.token)
        search_result = ZoomInfo_Company_Search_client.do_company_search(search_term)
        converted_data = company_search_result.from_json(search_result)
        search_result_items=[]
        for u in converted_data.data:
            search_result_items.append(u)

        if converted_data.max_results > max_result_per_request:
            batches:int =0
            batches= math.ceil(converted_data.max_results / max_result_per_request)
            for index in range(batches):
                temp = index +1
                if temp > 1:
                    search_result = ZoomInfo_Company_Search_client.do_company_search(search_term,temp)
                    converted_data = company_search_result.from_json(search_result)
            for u in converted_data.data:
                search_result_items.append(u)  
        return search_result_items

        