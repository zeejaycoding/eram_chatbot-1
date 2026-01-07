from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionDetectLanguage(Action):
    def name(self) -> str:
        return "action_detect_language"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        text = tracker.latest_message.get("text", "").lower()

        roman_urdu_keywords = {
'kya', 'kia', 'ky', 'hai', 'ha', 'haa', 'hota', 'ka', 'ke', 'mein', 'se', 'aur', 'nahi', 'bhi', 'ki', 'tha', 'hain', 'ho', 'koi', 'mera', 'meri', 'ko', 'par', 'ya', 'kyun', 'kaise', 'kab', 'kidhar', 'kon', 'shukriya', 'jee', 'han', 'bilkul', 'thik', 'acha', 'alvida', 'phir', 'madad', 'bataen', 'alamat', 'ilaj', 'wajah', 'lakshan', 'faide', 'ilaaj', 'theek', 'farq', 'shaadi', 'khail', 'matadi',  'dair', 'khatarnak', 'khatarnaak', 'ankh', 'dohrana', 'khelta', 'rishtydaar', 'pachtawa', 'zindagi',  'baat'        }

        if any(word in text.split() for word in roman_urdu_keywords):
            return [SlotSet("language", "roman_urdu")]
        else:
            return [SlotSet("language", "english")]