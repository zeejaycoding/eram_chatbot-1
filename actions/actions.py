import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import re

class ActionCustomFallback(Action):
    def name(self) -> Text:
        return "action_custom_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I'm here to help with autism-related questions. Please ask about symptoms, therapies, or support!")
        return []

class ActionUtterGreet(Action):
    def name(self) -> Text:
        return "action_utter_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"
        response = "utter_greet_ur" if lang == "roman_urdu" else "utter_greet_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterGoodbye(Action):
    def name(self) -> Text:
        return "action_utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"
        response = "utter_goodbye_ur" if lang == "roman_urdu" else "utter_goodbye_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterThanks(Action):
    def name(self) -> Text:
        return "action_utter_thanks"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"
        response = "utter_thanks_ur" if lang == "roman_urdu" else "utter_thanks_en"
        dispatcher.utter_message(response=response)
        return []

class ActionHandleAffirm(Action):
    def name(self) -> Text:
        return "action_handle_affirm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        last_intent = tracker.get_slot("last_intent")
        if last_intent == "ask_symptoms":
            response = "utter_more_symptoms_ur" if lang == "roman_urdu" else "utter_more_symptoms_en"
            dispatcher.utter_message(response=response)
            return [SlotSet("last_intent", None)]
        elif last_intent == "ask_daily_tips":
            response = "utter_more_daily_tips_ur" if lang == "roman_urdu" else "utter_more_daily_tips_en"
            dispatcher.utter_message(response=response)
            return [SlotSet("last_intent", None)]
        elif last_intent == "ask_visual_aids":
            response = "utter_more_visual_aids_ur" if lang == "roman_urdu" else "utter_more_visual_aids_en"
            dispatcher.utter_message(response=response)
            return [SlotSet("last_intent", None)]
        elif last_intent == "ask_causes":
            response = "utter_more_causes_ur" if lang == "roman_urdu" else "utter_more_causes_en"
            dispatcher.utter_message(response=response)
            return [SlotSet("last_intent", None)]
        elif last_intent == "ask_triggers":
            response = "utter_more_triggers_ur" if lang == "roman_urdu" else "utter_more_triggers_en"
            dispatcher.utter_message(response=response)
            return [SlotSet("last_intent", None)]
        else:
            response = "utter_affirm_ur" if lang == "roman_urdu" else "utter_affirm_en"
            dispatcher.utter_message(response=response)
            return []

class ActionUtterDeny(Action):
    def name(self) -> Text:
        return "action_utter_deny"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_deny_ur" if lang == "roman_urdu" else "utter_deny_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskDefinition(Action):
    def name(self) -> Text:
        return "action_utter_ask_definition"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_definition_ur" if lang == "roman_urdu" else "utter_ask_definition_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskPrevalence(Action):
    def name(self) -> Text:
        return "action_utter_ask_prevalence"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_prevalence_ur" if lang == "roman_urdu" else "utter_ask_prevalence_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskBot(Action):
    def name(self) -> Text:
        return "action_ask_bot"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_iamabot_ur" if lang == "roman_urdu" else "utter_iamabot_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskGenderPrevalence(Action):
    def name(self) -> Text:
        return "action_utter_ask_gender_prevalence"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_gender_prevalence_ur" if lang == "roman_urdu" else "utter_ask_gender_prevalence_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskCauses(Action):
    def name(self) -> Text:
        return "action_utter_ask_causes"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_causes_ur" if lang == "roman_urdu" else "utter_ask_causes_en"
        dispatcher.utter_message(response=response)
        return [SlotSet("last_intent", "ask_causes")]

class ActionUtterAskDoctors(Action):
    def name(self) -> Text:
        return "action_utter_ask_doctors"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in tracker.latest_message.get("text").lower() for keyword in roman_urdu_keywords) else "english"
        response = "utter_ask_doctors_ur" if lang == "roman_urdu" else "utter_ask_doctors_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskGames(Action):
    def name(self) -> Text:
        return "action_utter_ask_games"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in tracker.latest_message.get("text").lower() for keyword in roman_urdu_keywords) else "english"
        response = "utter_ask_games_ur" if lang == "roman_urdu" else "utter_ask_games_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskGenetics(Action):
    def name(self) -> Text:
        return "action_utter_ask_genetics"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_genetics_ur" if lang == "roman_urdu" else "utter_ask_genetics_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskDiagnosis(Action):
    def name(self) -> Text:
        return "action_utter_ask_diagnosis"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_diagnosis_ur" if lang == "roman_urdu" else "utter_ask_diagnosis_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskSymptoms(Action):
    def name(self) -> Text:
        return "action_utter_ask_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_symptoms_ur" if lang == "roman_urdu" else "utter_ask_symptoms_en"
        dispatcher.utter_message(response=response)
        return [SlotSet("last_intent", "ask_symptoms")]

class ActionUtterAskStimming(Action):
    def name(self) -> Text:
        return "action_utter_ask_stimming"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_stimming_ur" if lang == "roman_urdu" else "utter_ask_stimming_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskWhyStimming(Action):
    def name(self) -> Text:
        return "action_utter_ask_why_stimming"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_why_stimming_ur" if lang == "roman_urdu" else "utter_ask_why_stimming_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskTherapy(Action):
    def name(self) -> Text:
        return "action_utter_ask_therapy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_therapy_ur" if lang == "roman_urdu" else "utter_ask_therapy_en"
        dispatcher.utter_message(response=response)
        return [SlotSet("last_intent", "ask_therapy")]

class ActionUtterAskAbaTherapy(Action):
    def name(self) -> Text:
        return "action_utter_ask_aba_therapy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_aba_therapy_ur" if lang == "roman_urdu" else "utter_ask_aba_therapy_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskVisualAids(Action):
    def name(self) -> Text:
        return "action_utter_ask_visual_aids"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_visual_aids_ur" if lang == "roman_urdu" else "utter_ask_visual_aids_en"
        dispatcher.utter_message(response=response)
        return [SlotSet("last_intent", "ask_visual_aids")]

class ActionUtterAskDailyTips(Action):
    def name(self) -> Text:
        return "action_utter_ask_daily_tips"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_daily_tips_ur" if lang == "roman_urdu" else "utter_ask_daily_tips_en"
        dispatcher.utter_message(response=response)
        return [SlotSet("last_intent", "ask_daily_tips")]

class ActionUtterAskSupport(Action):
    def name(self) -> Text:
        return "action_utter_ask_support"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_support_ur" if lang == "roman_urdu" else "utter_ask_support_en"
        dispatcher.utter_message(response=response)
        return [SlotSet("last_intent", "ask_support")]

class ActionUtterAskAdultAutism(Action):
    def name(self) -> Text:
        return "action_utter_ask_adult_autism"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_adult_autism_ur" if lang == "roman_urdu" else "utter_ask_adult_autism_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskResources(Action):
    def name(self) -> Text:
        return "action_utter_ask_resources"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_resources_ur" if lang == "roman_urdu" else "utter_ask_resources_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskMyths(Action):
    def name(self) -> Text:
        return "action_utter_ask_myths"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_myths_ur" if lang == "roman_urdu" else "utter_ask_myths_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskCure(Action):
    def name(self) -> Text:
        return "action_utter_ask_cure"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_cure_ur" if lang == "roman_urdu" else "utter_ask_cure_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskEyeTracking(Action):
    def name(self) -> Text:
        return "action_utter_ask_eye_tracking"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_eye_tracking_ur" if lang == "roman_urdu" else "utter_ask_eye_tracking_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterNoDiagnosis(Action):
    def name(self) -> Text:
        return "action_utter_no_diagnosis"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_no_diagnosis_ur" if lang == "roman_urdu" else "utter_no_diagnosis_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterLanguageSupport(Action):
    def name(self) -> Text:
        return "action_utter_language_support"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_language_support_ur" if lang == "roman_urdu" else "utter_language_support_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskTriggers(Action):
    def name(self) -> Text:
        return "action_utter_ask_triggers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_triggers_ur" if lang == "roman_urdu" else "utter_ask_triggers_en"
        dispatcher.utter_message(response=response)
        return [SlotSet("last_intent", "ask_triggers")]

class ActionUtterAskTriggerTypes(Action):
    def name(self) -> Text:
        return "action_utter_ask_trigger_types"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_trigger_types_ur" if lang == "roman_urdu" else "utter_ask_trigger_types_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskWhyTriggers(Action):
    def name(self) -> Text:
        return "action_utter_ask_why_triggers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_why_triggers_ur" if lang == "roman_urdu" else "utter_ask_why_triggers_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskManagingTriggers(Action):
    def name(self) -> Text:
        return "action_utter_ask_managing_triggers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_managing_triggers_ur" if lang == "roman_urdu" else "utter_ask_managing_triggers_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAppFeatures(Action):
    def name(self) -> Text:
        return "action_utter_ask_app_features"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_app_features_ur" if lang == "roman_urdu" else "utter_ask_app_features_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAutismEmployment(Action):
    def name(self) -> Text:
        return "action_utter_ask_autism_employment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_autism_employment_ur" if lang == "roman_urdu" else "utter_ask_autism_employment_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAutismMarriage(Action):
    def name(self) -> Text:
        return "action_utter_ask_autism_marriage"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_autism_marriage_ur" if lang == "roman_urdu" else "utter_ask_autism_marriage_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskIfContagious(Action):
    def name(self) -> Text:
        return "action_utter_ask_if_contagious"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_if_contagious_ur" if lang == "roman_urdu" else "utter_ask_if_contagious_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskIfChildCanHave(Action):
    def name(self) -> Text:
        return "action_utter_ask_if_child_can_have"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_if_child_can_have_ur" if lang == "roman_urdu" else "utter_ask_if_child_can_have_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskIfAutismAdhdSame(Action):
    def name(self) -> Text:
        return "action_utter_ask_if_autism_adhd_same"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_if_autism_adhd_same_ur" if lang == "roman_urdu" else "utter_ask_if_autism_adhd_same_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskDiagnosisAge(Action):
    def name(self) -> Text:
        return "action_utter_ask_diagnosis_age"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_diagnosis_age_ur" if lang == "roman_urdu" else "utter_ask_diagnosis_age_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskLateSpeech(Action):
    def name(self) -> Text:
        return "action_utter_ask_late_speech"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_late_speech_ur" if lang == "roman_urdu" else "utter_ask_late_speech_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskTestAvailable(Action):
    def name(self) -> Text:
        return "action_utter_ask_test_available"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_test_available_ur" if lang == "roman_urdu" else "utter_ask_test_available_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskIfNormalOrDangerous(Action):
    def name(self) -> Text:
        return "action_utter_ask_if_normal_or_dangerous"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_if_normal_or_dangerous_ur" if lang == "roman_urdu" else "utter_ask_if_normal_or_dangerous_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskEyeContactSign(Action):
    def name(self) -> Text:
        return "action_utter_ask_eye_contact_sign"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_eye_contact_sign_ur" if lang == "roman_urdu" else "utter_ask_eye_contact_sign_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskRepeatingWords(Action):
    def name(self) -> Text:
        return "action_utter_ask_repeating_words"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_repeating_words_ur" if lang == "roman_urdu" else "utter_ask_repeating_words_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskNotPlayingWithOthers(Action):
    def name(self) -> Text:
        return "action_utter_ask_not_playing_with_others"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_not_playing_with_others_ur" if lang == "roman_urdu" else "utter_ask_not_playing_with_others_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskWhichDoctor(Action):
    def name(self) -> Text:
        return "action_utter_ask_which_doctor"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_which_doctor_ur" if lang == "roman_urdu" else "utter_ask_which_doctor_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskSchoolAdjustment(Action):
    def name(self) -> Text:
        return "action_utter_ask_school_adjustment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_school_adjustment_ur" if lang == "roman_urdu" else "utter_ask_school_adjustment_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskNormalSchool(Action):
    def name(self) -> Text:
        return "action_utter_ask_normal_school"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_normal_school_ur" if lang == "roman_urdu" else "utter_ask_normal_school_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskExplainToRelatives(Action):
    def name(self) -> Text:
        return "action_utter_ask_explain_to_relatives"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_explain_to_relatives_ur" if lang == "roman_urdu" else "utter_ask_explain_to_relatives_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskParentGuilt(Action):
    def name(self) -> Text:
        return "action_utter_ask_parent_guilt"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_parent_guilt_ur" if lang == "roman_urdu" else "utter_ask_parent_guilt_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskNormalLife(Action):
    def name(self) -> Text:
        return "action_utter_ask_normal_life"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_normal_life_ur" if lang == "roman_urdu" else "utter_ask_normal_life_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskTantrums(Action):
    def name(self) -> Text:
        return "action_utter_ask_tantrums"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_tantrums_ur" if lang == "roman_urdu" else "utter_ask_tantrums_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskIfWillSpeak(Action):
    def name(self) -> Text:
        return "action_utter_ask_if_will_speak"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_if_will_speak_ur" if lang == "roman_urdu" else "utter_ask_if_will_speak_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskTherapyImpact(Action):
    def name(self) -> Text:
        return "action_utter_ask_therapy_impact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_therapy_impact_ur" if lang == "roman_urdu" else "utter_ask_therapy_impact_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskHowToCommunicate(Action):
    def name(self) -> Text:
        return "action_utter_ask_how_to_communicate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_how_to_communicate_ur" if lang == "roman_urdu" else "utter_ask_how_to_communicate_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskIndependence(Action):
    def name(self) -> Text:
        return "action_utter_ask_independence"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_independence_ur" if lang == "roman_urdu" else "utter_ask_independence_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskBestTherapy(Action):
    def name(self) -> Text:
        return "action_utter_ask_best_therapy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_best_therapy_ur" if lang == "roman_urdu" else "utter_ask_best_therapy_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAbaDetails(Action):
    def name(self) -> Text:
        return "action_utter_ask_aba_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_aba_details_ur" if lang == "roman_urdu" else "utter_ask_aba_details_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskHomeExercises(Action):
    def name(self) -> Text:
        return "action_utter_ask_home_exercises"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_home_exercises_ur" if lang == "roman_urdu" else "utter_ask_home_exercises_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskOnlinePrograms(Action):
    def name(self) -> Text:
        return "action_utter_ask_online_programs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_online_programs_ur" if lang == "roman_urdu" else "utter_ask_online_programs_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskSpeechTherapyTime(Action):
    def name(self) -> Text:
        return "action_utter_ask_speech_therapy_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_speech_therapy_time_ur" if lang == "roman_urdu" else "utter_ask_speech_therapy_time_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAnxietySleep(Action):
    def name(self) -> Text:
        return "action_utter_ask_anxiety_sleep"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_anxiety_sleep_ur" if lang == "roman_urdu" else "utter_ask_anxiety_sleep_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskBilingualTherapy(Action):
    def name(self) -> Text:
        return "action_utter_ask_bilingual_therapy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_bilingual_therapy_ur" if lang == "roman_urdu" else "utter_ask_bilingual_therapy_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskSpectrumMeaning(Action):
    def name(self) -> Text:
        return "action_utter_ask_spectrum_meaning"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_spectrum_meaning_ur" if lang == "roman_urdu" else "utter_ask_spectrum_meaning_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskHighLowFunctioning(Action):
    def name(self) -> Text:
        return "action_utter_ask_high_low_functioning"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_high_low_functioning_ur" if lang == "roman_urdu" else "utter_ask_high_low_functioning_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAutismSpdDifference(Action):
    def name(self) -> Text:
        return "action_utter_ask_autism_spd_difference"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_autism_spd_difference_ur" if lang == "roman_urdu" else "utter_ask_autism_spd_difference_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskLoudSounds(Action):
    def name(self) -> Text:
        return "action_utter_ask_loud_sounds"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_loud_sounds_ur" if lang == "roman_urdu" else "utter_ask_loud_sounds_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskSpecialVsInclusive(Action):
    def name(self) -> Text:
        return "action_utter_ask_special_vs_inclusive"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_special_vs_inclusive_ur" if lang == "roman_urdu" else "utter_ask_special_vs_inclusive_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAdultLife(Action):
    def name(self) -> Text:
        return "action_utter_ask_adult_life"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_adult_life_ur" if lang == "roman_urdu" else "utter_ask_adult_life_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAiTechRole(Action):
    def name(self) -> Text:
        return "action_utter_ask_ai_tech_role"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_ai_tech_role_ur" if lang == "roman_urdu" else "utter_ask_ai_tech_role_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskLongTermPlan(Action):
    def name(self) -> Text:
        return "action_utter_ask_long_term_plan"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_long_term_plan_ur" if lang == "roman_urdu" else "utter_ask_long_term_plan_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAwarenessPakistan(Action):
    def name(self) -> Text:
        return "action_utter_ask_awareness_pakistan"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_awareness_pakistan_ur" if lang == "roman_urdu" else "utter_ask_awareness_pakistan_en"
        dispatcher.utter_message(response=response)
        return []

class ActionUtterAskAcceptance(Action):
    def name(self) -> Text:
        return "action_utter_ask_acceptance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get("text").lower()
        roman_urdu_keywords = ['kya', 'hai', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat']
        lang = "roman_urdu" if any(keyword in user_message for keyword in roman_urdu_keywords) else "english"

        response = "utter_ask_acceptance_ur" if lang == "roman_urdu" else "utter_ask_acceptance_en"
        dispatcher.utter_message(response=response)
        return []