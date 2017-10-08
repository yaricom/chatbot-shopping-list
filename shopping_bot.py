#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 22:52:04 2017

@author: yaric
"""

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

class ShoppingBot(object):
    def __init__(self, training_data_file = "./data/shopping-list/rasa/shopping-list-small.json",
                 config_file = "./config/shopping-list/config_spacy.json"):
        training_data = load_data(training_data_file)
        
        trainer = Trainer(RasaNLUConfig(config_file))
        self.interpreter = trainer.train(training_data)
        self.shopping_list = []
        
    
    def handle(self, message):
        """
        Handles incoming message using trained NLU model and prints response to
        the system out
        Arguments:
            message the message from user to be handled with known intents 
            (greet, add_item, clear_list, _num_items)
        """
        if message == '_num_items':
            print(len(self.shopping_list))
        else:
            res = self.interpreter.parse(message)
            intent = res['intent']['name']
            if res['intent']['confidence'] < .8:
                print('I\'m sorry! Could you please paraphrase!')
                return
            
            if intent == 'add_item':
                self.addItems(res['entities'])
            elif intent == 'clear_list':
                self.shopping_list.clear()
            elif intent == 'greet':
                print('Hello!')
            else:
                print('I\'m sorry! Could you please paraphrase!')
        
            print(out)

    def addItems(self, entities):
        for entity in entities:
                    size = len(self.shopping_list)
                    if self.shopping_list.count(entity['value']) == 0:
                        self.shopping_list.append(entity['value'])
                if len(self.shopping_list) == size:
                    print('You already have this item in your list')
                else:
                    print(self.shopping_list)
        
    def clearList(self):
        