#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 22:52:04 2017

The shopping bot main class which provides routines to maintain NLU model,
parse user's intents and execute corresponding commands in response.

@author: yaric
"""

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

from intent import HelloIntent, AddItemsIntent, ClearListIntent, ShowItemsIntent, ShowStatsIntent

class ShoppingBot(object):
    def __init__(self, training_data_file = "./data/shopping-list/rasa/shopping-list-small.json",
                 config_file = "./config/shopping-list/config_spacy.json"):
        training_data = load_data(training_data_file)
        
        trainer = Trainer(RasaNLUConfig(config_file))
        self.interpreter = trainer.train(training_data)
        self.shopping_list = {}
        
        # Create supported intents
        self.intents = {
                "greet"     : HelloIntent(self, "greet"),
                "add_item"  : AddItemsIntent(self, "add_item"),
                "clear_list": ClearListIntent(self, "clear_list"),
                "show_items": ShowItemsIntent(self, "show_items"),
                "_num_items": ShowStatsIntent(self, "_num_items")
            }
        
    
    def handle(self, message):
        """
        Handles incoming message using trained NLU model and prints response to
        the system out
        Arguments:
            message the message from user to be handled with known intents 
            (greet, add_item, clear_list, show_items, _num_items)
        """
        if message == '_num_items':
            self.intents['_num_items'].execute(None)
        else:
            nlu_data = self.interpreter.parse(message)
            intent = nlu_data['intent']['name']
            if self.intents[intent] is not None:
                self.intents[intent].execute(nlu_data)
        

        