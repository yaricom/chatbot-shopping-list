#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:15:26 2017

The user's intents definitions. It serves as abstraction to separate NLU processing
logic from response processing routines. Allows to easy register in the system as many
intents as it needed.

@author: yaric
"""

from command import GreetCommand, AddItemCommand, ShowItemsCommand, ClearListCommand, ShowStatsCommand

class Intent(object):
    
    def __init__(self, bot, intent_name):
        """
        Creates new intent for specified chatbot with given name
        Arguments:
            bot the chatbot
            name the intent name
        """
        self.chatbot = bot
        self.name = intent_name
        self.commands = []
        self.initCommands()
        
    def execute(self, nlu_data):
        """
        Executes given intent by applying appropriate command to the given
        parsed NLU data response
        """
        for c in self.commands:
            c.do(self.chatbot, None)
    
    def initCommands(self):
        """
        The method to init specific to particular intent.
        """
        pass
    
class AddItemsIntent(Intent):
    
    def initCommands(self):
        self.confidence_threshold = 0.8
        self.commands.append(AddItemCommand())
        self.commands.append(ShowItemsCommand())
    
    def execute(self, data):
        confidence = data['intent']['confidence']
        if confidence < self.confidence_threshold:
            print('I\'m sorry! Could you please paraphrase!')
            return
        
        # add all intent entities
        for entity in data['entities']:
            self.commands[0].do(self.chatbot, entity['value'])
        
        # show items list
        self.commands[1].do(self.chatbot, None)
        
class HelloIntent(Intent):
    def initCommands(self):
        self.commands.append(GreetCommand())
    
class ShowItemsIntent(Intent):
    def initCommands(self):
        self.commands.append(ShowItemsCommand())
        
class ClearListIntent(Intent):
    def initCommands(self):
        self.commands.append(ClearListCommand())
        self.commands.append(ShowItemsCommand())
        
class ShowStatsIntent(Intent):
     def initCommands(self):
        self.commands.append(ShowStatsCommand())

        
    