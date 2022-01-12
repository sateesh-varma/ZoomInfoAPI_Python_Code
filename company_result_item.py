from typing import List
import json

class company_result_item:
    id:int
    name:str
    def __init__(self,id:int,name:str) -> None:
        self.id=id
        self.name=name
 
class company_search_result:
    max_results: int
    total_results: int
    current_page: int
    data: List[company_result_item]
    
    def __init__(self,maxResults:int,totalResults:int,currentPage:int,data:list[company_result_item]) -> None:
        self.max_results=maxResults
        self.current_page=currentPage
        self.total_results=totalResults
        self.data=data
    @staticmethod
    def from_json(json_string:str):
        json_dict = json.loads(json_string)
        return company_search_result(**json_dict)
        
        

