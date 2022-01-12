from typing import List
import json

class Datum:
    id: int
    name: str
    number_of_contacts_in_zoom_info: int
    website: str
    state: str
    city: str
    domainlist:List[str]

    def __init__(self, id: int, name: str, numberOfContactsInZoomInfo: int, website: str, state: str, city: str,domainlist:List[str]) -> None:
        self.id = id
        self.name = name
        self.number_of_contacts_in_zoom_info = numberOfContactsInZoomInfo
        self.website = website
        self.state = state
        self.city = city
        self.domainlist=domainlist


class Input:
    companyid: int

    def __init__(self, companyid: int) -> None:
        self.companyid = companyid


class Result:
    input: Input
    data: List[Datum]
    match_status: str

    def __init__(self, input: Input, data: List[Datum], match_status: str) -> None:
        self.input = input
        self.data = data
        self.match_status = match_status


class Data:
    output_fields: List[List[str]]
    result: List[Result]

    def __init__(self, output_fields: List[List[str]], result: List[Result]) -> None:
        self.output_fields = output_fields
        self.result = result

class companyEnrichItemResult:
    success: bool
    data: Data

    def __init__(self, success: bool, data: Data) -> None:
        self.success = success
        self.data = data
    @staticmethod
    def from_json(json_string:str):
        json_dict = json.loads(json_string)
        return companyEnrichItemResult(**json_dict)
 
