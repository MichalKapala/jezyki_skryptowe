from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
from datetime import datetime, timedelta

current_orders = {}

def getDish(dish: str, menu):
    if not dish:
        return None

    for i in menu["dish"]:
        if i["name"].lower() == dish.lower():
            return i
    return None

class ActionListMenu(Action):

    def name(self) -> Text:
        return "action_list_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        f = open('./cfg/menu.json')
        data = json.load(f)
        response = ""
        for i in data["dish"]:
            response += i["name"] + " price: " + str(i["price"]) + "$" + " preparation time: " + str(i["preparation_time"]) + "h"
            response += "\n\n"

        dispatcher.utter_message("This is our menu: ")
        dispatcher.utter_message(response)

        return []

class ActionListOpenHours(Action):

    def name(self) -> Text:
        return "action_list_open_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        f = open('./cfg/opening_hours.json')
        data = json.load(f)
        response = ""
        for key, val in data["items"].items():
            response += key + ": opens {open_hour} closes {close_hour}".format(open_hour=val["open"], close_hour=val["close"]) + "\n"

        dispatcher.utter_message(response)
        return []

class ActionAnswerOpenHours(Action):

    def name(self) -> Text:
        return "action_answer_open_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        f = open('./cfg/opening_hours.json')
        data = json.load(f)["items"]
        response = ""
        day = tracker.get_slot("week_day")
        hour =  tracker.get_slot("hour")
        print(day, hour)
        if day and hour:
            open_h = data[day.capitalize()]["open"]
            close_h = data[day.capitalize()]["close"]
            if int(hour) >= int(open_h) and int(hour) <= int(close_h):
                response = "Yes, we are open at " + str(hour)
            else:
                response = "I'm sorry, we are closed at " + str(hour)
            dispatcher.utter_message(response)
        elif hour or day.lower() == "today":
            day = datetime.today().strftime('%A')
            if day.capitalize() in data.keys():
             open_h = data[day.capitalize()]["open"]
             close_h = data[day.capitalize()]["close"]
             response = "Today we are open from {open_hour} to {close_hour}".format(open_hour=open_h, close_hour=close_h)
            dispatcher.utter_message(response)
        elif  day.lower() == "tomorrow":
            day = (datetime.today() + timedelta(days=1)).strftime('%A')
            if day.capitalize() in data.keys():
             open_h = data[day.capitalize()]["open"]
             close_h = data[day.capitalize()]["close"]
             response = "Tommorow we are open from {open_hour} to {close_hour}".format(open_hour=open_h, close_hour=close_h)
            dispatcher.utter_message(response)
        if day and day.capitalize() in data.keys():
            open_h = data[day.capitalize()]["open"]
            close_h = data[day.capitalize()]["close"]
            response = "On {week_day} we opens at {open_hours} and closes at {close_hours} ".format(week_day=day, open_hours=open_h, close_hours=close_h)
            dispatcher.utter_message(response)

        return [SlotSet("week_day", None), SlotSet("hour", None)]

class ShowIngredients(Action):

    def name(self) -> Text:
        return "action_list_ingredients"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        f = open('./cfg/menu.json')
        menu = json.load(f)
        dish = tracker.get_slot("dish")

        dishInfo = getDish(dish, menu)

        if dishInfo:
            response = dish + " contains : "
            for ig in dishInfo["ingredients"]:
               response += ig + " "
        else:
            response = "Sorry we don't have this dish in menu :/"

        dispatcher.utter_message(response)

        return [SlotSet("dish", None), SlotSet("extra_ingredients", None)]

class ProcessOrder(Action):

    def name(self) -> Text:
        return "action_process_simple_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        f = open('./cfg/menu.json')
        menu = json.load(f)
        dish = tracker.get_slot("dish")

        dishInfo = getDish(dish, menu)

        if dishInfo:
            response = "Sure adding to your order " + dishInfo["name"]
            current_orders.setdefault(tracker.sender_id, []).append({dish: ""})
        else:
            response = "Sorry we don't have this dish in menu :/"

        dispatcher.utter_message(response)

        return [SlotSet("dish", None)]

class ProcessExtraOrder(Action):

    def name(self) -> Text:
        return "action_process_extra_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        f = open('./cfg/menu.json')
        menu = json.load(f)

        dish = tracker.get_slot("dish")
        additional_ingredients = tracker.get_slot("extra_ingredients")
        less_ingredients = tracker.get_slot("less_ingredients")


        print(additional_ingredients, less_ingredients)
        dishInfo = getDish(dish, menu)

        if dishInfo:
            response = "Sure adding to your order " + dishInfo["name"]
            special_wish = ""

            if additional_ingredients:
                special_wish += " with extra: "
                print(additional_ingredients)
                for ig in set(additional_ingredients):
                    special_wish += str(ig) + " "
                response += special_wish

            if less_ingredients:
                special_wish += " and without: "
                for ig in set(less_ingredients):
                    special_wish += str(ig) + " "
                response += special_wish
            current_orders.setdefault(tracker.sender_id, []).append({dish: special_wish})
        else:
            response = "Sorry we don't have this dish in menu :/"

        dispatcher.utter_message(response)

        return [SlotSet("dish", None), SlotSet("extra_ingredients", None), SlotSet("less_ingredients", None)]

class SummarizeOrder(Action):
    def name(self) -> Text:
        return "action_summarize_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        f = open('./cfg/menu.json')
        menu = json.load(f)

        response = "Your current order contains: \n"
        if tracker.sender_id in current_orders.keys():
            current_order = current_orders[tracker.sender_id]
        else:
            dispatcher.utter_message("You did not order anything!")
            return []

        i = 1
        for order in current_order:
            for dish, wish in order.items():
                dishInfo = getDish(dish, menu)
                response += str(i) + ". " + dish + " " + wish + " costs: " + str(dishInfo["price"]) + "$ waiting time: " + str(dishInfo["preparation_time"]) + "h\n"
                i += 1
        dispatcher.utter_message(response)

        return []

class ConfirmOrder(Action):
    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        f = open('./cfg/menu.json')
        menu = json.load(f)

        response = "Your current order contains: \n"
        if tracker.sender_id in current_orders.keys():
            current_order = current_orders[tracker.sender_id]
        else:
            dispatcher.utter_message("You did not order anything!")
            return []

        cost = 0
        total_time_minutes = 0
        i = 1
        for order in current_order:
            print(type(order))
            print(order)
            for dish, wish in order.items():
                dishInfo = getDish(dish, menu)
                response += str(i) + ". " + dish + " " + wish + " costs: " + str(dishInfo["price"]) + "$ waiting time: " + str(dishInfo["preparation_time"]) + "h\n"
                cost += dishInfo["price"]
                total_time_minutes += dishInfo["preparation_time"] * 60
                i+=1

        dispatcher.utter_message(response)
        dispatcher.utter_message("------------------------------------------------")
        dispatcher.utter_message("It's total " + str(cost) +" $")
        dispatcher.utter_message("Please collect your meal in " + str(round(total_time_minutes)) + " minutes")
        dispatcher.utter_message("Thank you for your order!")

        return []


class ResetOrder(Action):
    def name(self) -> Text:
        return "action_reset_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(("I reset your order, feel free to make another "))

        if tracker.sender_id in current_orders.keys():
            current_orders.pop(tracker.sender_id)

        return []
