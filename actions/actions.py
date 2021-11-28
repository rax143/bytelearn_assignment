from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
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
        states = tracker.get_slot("state")
        date = tracker.get_slot("date")
        flag = False
        caseStatusMessage = "Covid cases status: "

        if date:
            formatedDate = dateTimeConvertor(date)
            data = response.get("data")
            try:
                for values in data:
                    if values.get("day") == formatedDate:
                        flag = True
                        covidCaseStatus = values.get("summary").get(status)
                        if states:
                            for state in states:
                                for regionalData in values.get("regional"):
                                    if regionalData.get("loc").lower() == state.lower():
                                        covidCaseStatus = regionalData.get(
                                            status)
                                        caseStatusMessage += f"\n{date[0]}\n{state} : {covidCaseStatus} "
                            dispatcher.utter_message(text=caseStatusMessage)
                            return [AllSlotsReset()]
                        break
                if flag == False:
                    dispatcher.utter_message(
                        text=f"Sorry, We don't have any data for {date[0]}")

            except:
                dispatcher.utter_message(
                    text="We are having some issue now please try after some time")

        elif states:
            for state in states:
                for regionalData in response.get("data")[0].get("regional"):
                    if regionalData.get("loc").lower() == state.lower():
                        covidCaseStatus = regionalData.get(status)
                        caseStatusMessage += f"\n{state} : {covidCaseStatus} "
            dispatcher.utter_message(text=caseStatusMessage)

        return [AllSlotsReset()]
