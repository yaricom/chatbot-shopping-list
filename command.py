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

class Command(object):

    def do(intent):
        """
        Execute command's action for specified intent.
        Arguments:
            intent the Intent context in which this command will be executed.
        """
        pass

