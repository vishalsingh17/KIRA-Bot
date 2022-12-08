# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, ActionExecuted, EventType, AllSlotsReset
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionCourseDetails(Action):

    def name(self) -> Text:
        return "action_course_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    	course_name = tracker.get_slot('course')

    	if course_name == None:
            dispatcher.utter_message(text = "We have wide range of courses available like Full stack Data Science, Full Stack Data Analytics, Full Stack JavaScript, Cyber Security Masters and many more...")
            return [SlotSet("course", None)]



    	course_dict = {"data analytics" : "The Full Stack Data Analytics course assists you in becoming a skilled data analyst. Learn how to deal with SQL databases, develop data visualisations, and apply predictive analytics and statistics using the best analytics tools and methodologies.",
    	"data science" : "In this course you will learn the entire stack required to work in the data science, data analytics, and big data domain, including machine learning, deep learning, computer vision NLP and Big data including MLOps and cloud infrastructure, along with real-time industry projects and product development with the iNeuron product development team, which will enable you to contribute on various levels.",
    	"java": "Java is one of the most widely used programming languages, owing to its versatility and compatibility. This Java course will teach you all you need to know to get started with Java.",
    	"cyber security" : "This is an ISO 27001 government-certified course that covers Bug Bounty & Web Pentesting, system exploitation, network pentesting, android pentesting, Forensics, etc. From this course, our students have found bugs in big organizations like Harvard, Huawei, Nike, BMW, Doordarshan, Nykaa, GoodRx etc.",
    	"javascript" : "Learn everything about JavaScript with React, Vue, Angular, Nodejs, MongoDB, NextJS, Tailwind, etc. Build industry ready projects"}

    	if course_name.lower() in course_dict:
    		dispatcher.utter_message(text = course_dict[course_name.lower()])
    		return [SlotSet("course", None)]

    	else:
    		dispatcher.utter_message(text = "We have wide range of courses available like Full Stack Data Science, Full Stack Data Analytics, Full Stack JavaScript, Cyber Security Masters and many more...!")
    		return [SlotSet("course", None)]


class ActionCoursePrice(Action):

    def name(self) -> Text:
        return "action_course_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    	course_name = tracker.get_slot('course')

    	if course_name == None:
    		dispatcher.utter_message(text = "Please visit official website for course price details")
    		return [SlotSet("course", None)]

    	course_dict = {"data analytics" : 4000,
    	"data science" : 17700,
    	"java": 4000,
    	"cyber security" : 4000,
    	"javascript" : 17700}

    	if course_name.lower() in course_dict:
    		dispatcher.utter_message(text = 'Course Price : ' + str(course_dict[course_name.lower()]))
    		return [SlotSet("course", None)]

    	else:
    		dispatcher.utter_message(text = "Please visit official website for course price details")
    		return [SlotSet("course", None)]

# class ActionCourseDate(Action):

#     def name(self) -> Text:
#         return "action_course_date"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         course_name = tracker.get_slot('course')

#         if course_name == None:
#             dispatcher.utter_message(text = "Please Visit official Website for Course start dates")
#             return [SlotSet("course", None)]

#         course_dict = {"data analytics" : '25-12-2022',
#         "data science" : '25-11-2022',
#         "java": '25-10-2022',
#         "cyber security" : '25-09-2022',
#         "javascript" : '25-08-2022'}

#         if course_name.lower() in course_dict:
#             dispatcher.utter_message(text = 'Course Start Date : ' + course_dict[course_name.lower()])
#             return [SlotSet("course", None)]

#         else:
#             dispatcher.utter_message(text = "Please Visit official Website for Course start dates")
#             return [SlotSet("course", None)]

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]
     

