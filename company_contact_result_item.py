
from enum import Enum
from typing import Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Name(Enum):
    TCS_COMMUNICATIONS = "TCS Communications"


class Company:
    id: int
    name: Name

    def __init__(self, id: int, name: Name) -> None:
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'Company':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = Name(obj.get("name"))
        return Company(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = to_enum(Name, self.name)
        return result


class LastUpdatedDate(Enum):
    EMPTY = ""
    THE_12182021904_AM = "12/18/2021 9:04 AM"
    THE_132022618_AM = "1/3/2022 6:18 AM"


class Datum:
    id: int
    first_name: str
    middle_name: str
    last_name: str
    valid_date: str
    last_updated_date: str
    job_title: str
    contact_accuracy_score: float
    has_email: bool
    has_supplemental_email: bool
    has_direct_phone: bool
    has_mobile_phone: bool
    has_company_industry: bool
    has_company_phone: bool
    has_company_street: bool
    has_company_state: bool
    has_company_zip_code: bool
    has_company_country: bool
    has_company_revenue: bool
    has_company_employee_count: bool
    company: Company

    def __init__(self, id: int, first_name: str, middle_name: str, last_name: str, valid_date: str, last_updated_date: LastUpdatedDate, job_title: str, contact_accuracy_score: float, has_email: bool, has_supplemental_email: bool, has_direct_phone: bool, has_mobile_phone: bool, has_company_industry: bool, has_company_phone: bool, has_company_street: bool, has_company_state: bool, has_company_zip_code: bool, has_company_country: bool, has_company_revenue: bool, has_company_employee_count: bool, company: Company) -> None:
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.valid_date = valid_date
        self.last_updated_date = last_updated_date
        self.job_title = job_title
        self.contact_accuracy_score = contact_accuracy_score
        self.has_email = has_email
        self.has_supplemental_email = has_supplemental_email
        self.has_direct_phone = has_direct_phone
        self.has_mobile_phone = has_mobile_phone
        self.has_company_industry = has_company_industry
        self.has_company_phone = has_company_phone
        self.has_company_street = has_company_street
        self.has_company_state = has_company_state
        self.has_company_zip_code = has_company_zip_code
        self.has_company_country = has_company_country
        self.has_company_revenue = has_company_revenue
        self.has_company_employee_count = has_company_employee_count
        self.company = company

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        first_name = from_str(obj.get("firstName"))
        middle_name = from_str(obj.get("middleName"))
        last_name = from_str(obj.get("lastName"))
        valid_date = from_str(obj.get("validDate"))
        last_updated_date = from_str(obj.get("lastUpdatedDate")) # LastUpdatedDate(obj.get("lastUpdatedDate"))
        job_title = from_str(obj.get("jobTitle"))
        contact_accuracy_score = from_float(obj.get("contactAccuracyScore"))
        has_email = from_bool(obj.get("hasEmail"))
        has_supplemental_email = from_bool(obj.get("hasSupplementalEmail"))
        has_direct_phone = from_bool(obj.get("hasDirectPhone"))
        has_mobile_phone = from_bool(obj.get("hasMobilePhone"))
        has_company_industry = from_bool(obj.get("hasCompanyIndustry"))
        has_company_phone = from_bool(obj.get("hasCompanyPhone"))
        has_company_street = from_bool(obj.get("hasCompanyStreet"))
        has_company_state = from_bool(obj.get("hasCompanyState"))
        has_company_zip_code = from_bool(obj.get("hasCompanyZipCode"))
        has_company_country = from_bool(obj.get("hasCompanyCountry"))
        has_company_revenue = from_bool(obj.get("hasCompanyRevenue"))
        has_company_employee_count = from_bool(obj.get("hasCompanyEmployeeCount"))
        company = Company.from_dict(obj.get("company"))
        return Datum(id, first_name, middle_name, last_name, valid_date, last_updated_date, job_title, contact_accuracy_score, has_email, has_supplemental_email, has_direct_phone, has_mobile_phone, has_company_industry, has_company_phone, has_company_street, has_company_state, has_company_zip_code, has_company_country, has_company_revenue, has_company_employee_count, company)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["firstName"] = from_str(self.first_name)
        result["middleName"] = from_str(self.middle_name)
        result["lastName"] = from_str(self.last_name)
        result["validDate"] = from_str(self.valid_date)
        result["lastUpdatedDate"] = from_str(self.last_updated_date)   
        result["jobTitle"] = from_str(self.job_title)
        result["contactAccuracyScore"] = to_float(self.contact_accuracy_score)
        result["hasEmail"] = from_bool(self.has_email)
        result["hasSupplementalEmail"] = from_bool(self.has_supplemental_email)
        result["hasDirectPhone"] = from_bool(self.has_direct_phone)
        result["hasMobilePhone"] = from_bool(self.has_mobile_phone)
        result["hasCompanyIndustry"] = from_bool(self.has_company_industry)
        result["hasCompanyPhone"] = from_bool(self.has_company_phone)
        result["hasCompanyStreet"] = from_bool(self.has_company_street)
        result["hasCompanyState"] = from_bool(self.has_company_state)
        result["hasCompanyZipCode"] = from_bool(self.has_company_zip_code)
        result["hasCompanyCountry"] = from_bool(self.has_company_country)
        result["hasCompanyRevenue"] = from_bool(self.has_company_revenue)
        result["hasCompanyEmployeeCount"] = from_bool(self.has_company_employee_count)
        result["company"] = to_class(Company, self.company)
        return result


class company_contact_item:
    max_results: int
    total_results: int
    current_page: int
    data: List[Datum]

    def __init__(self, max_results: int, total_results: int, current_page: int, data: List[Datum]) -> None:
        self.max_results = max_results
        self.total_results = total_results
        self.current_page = current_page
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'company_contact_item':
        assert isinstance(obj, dict)
        max_results = from_int(obj.get("maxResults"))
        total_results = from_int(obj.get("totalResults"))
        current_page = from_int(obj.get("currentPage"))
        data = from_list(Datum.from_dict, obj.get("data"))
        return company_contact_item(max_results, total_results, current_page, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["maxResults"] = from_int(self.max_results)
        result["totalResults"] = from_int(self.total_results)
        result["currentPage"] = from_int(self.current_page)
        result["data"] = from_list(lambda x: to_class(Datum, x), self.data)
        return result


def company_contact_item_from_dict(s: Any) -> company_contact_item:
    return company_contact_item.from_dict(s)

  
