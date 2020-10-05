# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.events import SlotSet
from bertqa import BertQA, BertQA1

class ActionHelloWorld(Action):
     def name(self) -> Text:
         return "action_ask_question"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         if tracker.get_slot("bot_type") == "covid":
             # https://en.wikipedia.org/wiki/Coronavirus_disease_2019
             buttons = [{'title': 'Ask another Covid19 related question', 'payload': '/another_question_covid'},
                        {'title': 'Home', 'payload': '/greet'},
                        {'title': 'Quit', 'payload': '/quit'}]
             question = tracker.latest_message['text']
             answer = BertQA(question)
             dispatcher.utter_template("utter_answer", tracker, answer=answer)
             dispatcher.utter_button_message("Please select below options:", buttons)

         elif tracker.get_slot("bot_type") == "myjbr":
             buttons = [{'title': 'Ask another MyJBR related question', 'payload': '/another_question_myjbr'},
                        {'title': 'Home', 'payload': '/home'},
                        {'title': 'Quit', 'payload': '/quit'}]
             question = tracker.latest_message['text']
             answer = BertQA1(question)
             answer = answer.replace("#", "")
             answer = answer.replace(" #", "")
             answer = answer.replace("  #", "")
             answer = answer.replace(" # ", "")
             answer = answer.replace("# ", "")
             answer = answer.replace("#  ", "")
             answer = answer.replace(" ##", "")
             dispatcher.utter_template("utter_answer", tracker, answer=answer)
             dispatcher.utter_button_message("Please select below options:", buttons)

         return []
