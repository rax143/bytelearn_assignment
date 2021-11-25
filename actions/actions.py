from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from helpers.requestHelper import RequestUtility
from configs.config import API_URL
from helpers.dateConvertor import dateTimeConvertor



class ActionGetCovidDetails(Action):

    def name(self) -> Text:
        return "action_get_covid_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request_utility = RequestUtility()
        response = request_utility.send_request(
            "GET", API_URL)
        response = (response.json())
        status = tracker.get_slot("status")
        state = tracker.get_slot("state")
        date = tracker.get_slot("date")

        if date:
            formatedDate = dateTimeConvertor(date)
            data = response.get("data")
            for values in data:
                if values.get("day") == formatedDate:
                    covidCaseStatus=values.get("summary").get(status)
                    if state:
                        for item in state:
                            for regionalData in values.get("regional"):
                                if regionalData.get("loc").lower() == item.lower():
                                    covidCaseStatus=regionalData.get(status)
                                    dispatcher.utter_message(text = f"Covid case on {formatedDate} in {item} is {covidCaseStatus}")
                                    return []
                    dispatcher.utter_message(text = f"Covid case status on {formatedDate} is {covidCaseStatus}")

        elif state:
            for value in state:
                for regionalData in response.get("data")[0].get("regional"):
                    if regionalData.get("loc").lower() == value.lower():
                        covidCaseStatus=regionalData.get(status)
                        dispatcher.utter_message(text = f"Covid case status in {value} is {covidCaseStatus}")
            
        return []
