# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Text
from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from actions.utils import confirmar_status_mercado, gerar_uuid, arredondar_numero
import requests

 # Ação para saudar corretamente de acordo com o periodo do dia
class ActionAcolhimento(Action):
    def name(self) -> Text:
        return "action_acolhimento"
 
    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        requestId=gerar_uuid()
        print({"requestId":requestId,"action": self.name(), "sender_id": tracker.sender_id, "status":"started"})
        circle_greeting = tracker.get_slot("saudar_novamente")
        date = datetime.now()
        hour = int(date.hour)
        if 6 <= hour < 12:
            time_greeting = "bom dia"
        elif 12 <= hour < 18:
            time_greeting = "boa tarde"
        else:
            time_greeting = "boa noite"
        if circle_greeting:
            dispatcher.utter_message(response="utter_saudar_novamente_com_acolhimento",time_greeting=time_greeting)
        else:
            dispatcher.utter_message(response="utter_saudar_com_acolhimento",time_greeting=time_greeting)
        print({
            "requestId":requestId,
            "action": self.name(),
            "sender_id": tracker.sender_id,
            "result": {
                "circle_greeting": circle_greeting,
                "date": str(date),
                "hour": hour,
                "time_greeting": time_greeting,
            }}
        )
        print({"requestId":requestId,"action": self.name(), "sender_id": tracker.sender_id, "status":"finished"})
        return [SlotSet("saudar_novamente", time_greeting)]
 
# Ação padrão enviar o fallback do Rasa Core
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"
 
    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        requestId=gerar_uuid()
        print({"requestId":requestId,"action": self.name(), "sender_id": tracker.sender_id, "status":"started"})
        dispatcher.utter_message(response="utter_padrao")
        dispatcher.utter_message(response="utter_menu")
        print({"requestId":requestId,"action": self.name(), "sender_id": tracker.sender_id, "status":"finished"})
        return [UserUtteranceReverted()]

# Ação para informar informações da rodada
class ActionInformarRodada(Action):
    def name(self) -> Text:
        return "action_informar_rodada"
 
    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[Dict[Text, Any]]:
        requestId=gerar_uuid()
        print({"requestId":requestId,"action": self.name(), "sender_id": tracker.sender_id, "status":"started"})
        api_address='https://api.cartola.globo.com/mercado/status'
        response = requests.get(api_address).json()
        times_escalados1 = arredondar_numero(response['times_escalados'])
        try:
            response = requests.get(api_address).json()
            times_escalados = arredondar_numero(response['times_escalados'])
            dispatcher.utter_message(response="utter_rodada",
                rodada_atual=response['rodada_atual'],
                status_mercado=confirmar_status_mercado(response['status_mercado']),
                times_escalados=times_escalados
            )
            print({
                "requestId":requestId,
                "action": self.name(),
                "sender_id": tracker.sender_id,
                "result": {
                    "rodada_atual": response['rodada_atual'],
                    "status_mercado": response['status_mercado'],
                    "fechamento": response['fechamento'],
                    "times_escalados": times_escalados
                }}
            )
        except:
            print({"action": self.name(),"Error":"An exception occurred on request."})
        
        print({"requestId":requestId,"action": self.name(), "sender_id": tracker.sender_id, "status":"finished"})
       
