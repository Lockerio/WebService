from typing import Dict, List, Any


class JSONParser:
    @staticmethod
    def read_json_data(json_dict: Dict[str, Any],
                       fields_to_extract: List[str]) -> Dict[str, Any]:

        data = {
            field: json_dict[field]
            for field in fields_to_extract
            if field in json_dict
        }
        return data
