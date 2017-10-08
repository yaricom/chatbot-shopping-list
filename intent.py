#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:15:26 2017

The user's intents definitions. It serves as abstraction to separate NLU processing
logic from response processing routines. Allows to easy register in the system as many
intents as it needed.

@author: yaric
"""

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
        # the ordered list of commands to be executed by this intent
        self.commands = [] 
        
    def execute(self, nlu_data):
        """
        Executes given intent by applying appropriate command to the given
        parsed NLU data response
        """
        pass