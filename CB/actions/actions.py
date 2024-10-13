import os
from dotenv import load_dotenv
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

load_dotenv()

class ActionCheckSeatAvailability(Action):

    def name(self) -> Text:
        return "action_check_seat_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        departure = tracker.get_slot('departure_station')
        destination = tracker.get_slot('destination_station')
        travel_date = tracker.get_slot('travel_date')
        class_type = tracker.get_slot('class_type')
        train_number = tracker.get_slot('train_number')  # Optional

        api_url = os.getenv('SEAT_AVAILABILITY_API_URL', 'http://localhost:5001/seat_availability')

        params = {
            'from': departure,
            'to': destination,
            'date': travel_date,
            'class': class_type
        }

        if train_number:
            params['train_number'] = train_number

        try:
            response = requests.get(api_url, params=params)
            data = response.json()

            seats = data.get('seats_available')

            if seats is not None:
                dispatcher.utter_message(text=f"Seats available in {class_type} from {departure} to {destination} on {travel_date}: {seats}")
            else:
                dispatcher.utter_message(text="I'm unable to fetch seat availability at the moment. Please try again later.")

        except Exception as e:
            dispatcher.utter_message(text="Sorry, I encountered an error while checking seat availability.")
            dispatcher.utter_message(text=str(e))

        return []

class ActionBookTicket(Action):

    def name(self) -> Text:
        return "action_book_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        departure = tracker.get_slot('departure_station')
        destination = tracker.get_slot('destination_station')
        travel_date = tracker.get_slot('travel_date')
        number_of_passengers = tracker.get_slot('number_of_passengers')
        class_type = tracker.get_slot('class_type')
        payment_method = tracker.get_slot('payment_method') 
        ticket_type = tracker.get_slot('ticket_type')        
        user_name = tracker.get_slot('user_name')            
        age = tracker.get_slot('age')                        
        travel_time = tracker.get_slot('travel_time')        
        gender = tracker.get_slot('gender')                  
        train_number = tracker.get_slot('train_number') 

        try:
            booking_reference = "ABC123"

            dispatcher.utter_message(text=f"Your booking reference number is {booking_reference}. Your ticket has been successfully booked from {departure} to {destination} on {travel_date} for {number_of_passengers} passengers in {class_type} class.")

        except Exception as e:
            dispatcher.utter_message(text="Sorry, I encountered an error while booking your ticket.")
            dispatcher.utter_message(text=str(e))

        return []
