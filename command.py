#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:24:39 2017

The stateless command allows to encapsulate processing logic for specic 
intent's command. Allows to easy build response processing pipelines with
multiple stages of intent data processing. The stateless commands may be shared
among various intents.

@author: yaric
"""

import random

class Command(object):

    def do(self, bot, entity):
        """
        Execute command's action for specified intent.
        Arguments:
            bot the chatbot
            entity the parsed NLU entity
        """
        pass


class GreetCommand(Command):
    """
    The command to greet user
    """
    
    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """
        self.greetings = ["Hey!", "Hello!", "Hi there!", "Hallo!", "How are you!"]
    
    def do(self, bot, entity):
        print(random.choice(self.greetings))

class AddItemCommand(Command):
    """
    The command to add item to the list
    """   
    def do(self, bot, entity):
        count = 0
        if entity in bot.shopping_list:
            count = bot.shopping_list[entity]
        
        bot.shopping_list[entity] = count + 1
        
        
class ShowItemsCommand(Command):
    """
    The command to display shopping list
    """
    
    def do(self, bot, entity):
        if len(bot.shopping_list) == 0:
            print("Your shopping list is empty!")
            return
        
        print("Shopping list items:")
        for k, v in bot.shopping_list.items():
            print("%s - quantity: %d" % (k, v))
            
class ClearListCommand(Command):
    """
    The command to clear shopping list
    """
    
    def do(self, bot, entity):
        bot.shopping_list.clear()
        print("Items removed from your list!")
        
class ShowStatsCommand(Command):
    """
    The command to show shopping list statistics
    """
    
    def do(self, bot, entity):
        unique = len(bot.shopping_list)
        if unique == 0:
            print("shopping list is empty")
            
        total = 0
        for v in bot.shopping_list.values():
            total += v
            
        print("# of unique items: %d, total # of items: %d" % (unique, total))
        