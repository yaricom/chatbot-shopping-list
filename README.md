This is simple chatbot application with Natural Language Understanding to maintain very simple shopping list. It's built using [RASA NLU][rasa_nlu_home] Python library with [Spacy NLP][spacy_nlp_home] backend.
The bot which we will create assumes that anything our bot's users say can be categorized into one of the following intents:
1. Greetings (**greet**)
2. Adding item to the shopping list (**add_item**)
3. Removing all items from shopping list (**clear_list**)
4. Displaying shopping list (**show_items**) 
5. The debug command to return number of items in the list (**_num_items**) 

## System Requirements ##
As it was already mentined we are going to use RASA NLU and Spacy NLP Python libraries which should be installed.

To install current stable version of [RASA NLU][rasa_nlu_home] just run
```python
pip install rasa_nlu
```

To install current version of [Spacy NLP][spacy_nlp_home] execute
```python
pip install -U spacy
```

We will use English language Spacy model which can be installed as following:
```python
python -m spacy download en
```

## Preparing the Training Data ##
To build NLU model able to parse user's intents first we need to create appropriate training data which will allow our chatbot to interpret user's inputs and created structured data (intent/entities). The best way to get training texts is from real users, and the best way to get the structured data is to pretend to be the bot yourself. For the purpose of this experiment we will create small training data corpus in format described at: https://rasa-nlu.readthedocs.io/en/stable/dataformat.html

The best way to create training data in rasa's format and to validate it is to use great [online tool](https://rasahq.github.io/rasa-nlu-trainer/) created by [@azazdeaz](https://github.com/azazdeaz).

The resulting training data file in JSON format can be found in the *data* folder.

## Training a New NLU Model ##
There are two modes to use Rasa NLU models - as a HTTP server or directly from Python. In this experiment taking into account small size of our training data we will train and use NLU model directly from Python. 

To do this first we need to create corresponding Rasa NLU configuration file. We will use Spacy NLP as backend thus configuration file will be:
```json
{
  "pipeline": "spacy_sklearn",
  "path" : "./projects",
  "data" : "./data/shopping-list/rasa/shopping-list-small.json"
}
```

For more details as how to run Rasa NLU models directly from Python refer to: https://rasa-nlu.readthedocs.io/en/stable/python.html

## The Shopping List Chatbot ##
The training data includes extremelly limited knowledge of grocery items to be purchased - eggs, milk, and butter. But it can be easy extended by modifying training data file mentioned above.

The chatbot can be used as following:
```python
In [1]: from shopping_bot import ShoppingBot

In [2]: bot = ShoppingBot()

In [3]: bot.handle("Hello")
How are you!

In [4]: bot.handle("add milk")
Shopping list items:
milk - quantity: 1

In [5]: bot.handle("i need eggs")
Shopping list items:
milk - quantity: 1
eggs - quantity: 1

In [6]: bot.handle("i need eggs and milk")
Shopping list items:
milk - quantity: 2
eggs - quantity: 2

In [7]: bot.handle("my list")
Shopping list items:
milk - quantity: 2
eggs - quantity: 2

In [8]: bot.handle("_num_items")
# of unique items: 2, total # of items: 4

In [9]: bot.handle("clear list")
Items removed from your list!
Your shopping list is empty!

In [10]: bot.handle("_num_items")
shopping list is empty
# of unique items: 0, total # of items: 0
```

The supported grocery items:
* eggs
* milk
* butter

[rasa_nlu_home]:https://rasa-nlu.readthedocs.io/en/stable/
[spacy_nlp_home]:https://spacy.io
