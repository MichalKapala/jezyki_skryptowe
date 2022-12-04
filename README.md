# Zadanie1 Bash



---------------------------------------------------

# Zadanie 2 Chatbot 

## 1.Purpose of project
Main purpose of this project is to write chat bot, using RASA framework. As a part of this activity integration to one of
the mentioned platform were expected as well

## 2 Chatbot current capabilities
-
-
-

## 3. Project structure
````bash
  ├── actions 
  │   ├── actions.py  # Defined custom rasa actions to proper handle client intents
  │   ├── __init__.py
  │   └── __pycache__
  │       ├── actions.cpython-38.pyc
  │       └── __init__.cpython-38.pyc
  ├── cfg  # Contains configurable files as menu.json and opening_hours.json
  │   ├── convertToYaml.py  # Simple converter that create .yaml file with dishes names. It is used later as lookup table for dish entity
  │   ├── menu.json # Contains restaurant's menu. (I extended this by adding ingredients to each dish)
  │   └── opening_hours.json  # Contains restaurant's opening hours
  ├── config.yml  # Rasa config, pretty simmilar to default one but added RegexEntityExtractor to proper extract entity from lookuptable
  ├── credentials.yml
  ├── data
  │   ├── ingredients.yml  # Ingredients lookup table
  │   ├── menu.yml # Menu lookup table
  │   ├── nlu.yml  # Training data
  │   ├── rules.yml # Rasa rules
  │   └── stories.yml # Simple stories
  ├── domain.yml # Rasa domain file
  ├── endpoints.yml
  └── story_graph.dot
````

## 4.1 Project setup ubuntu
To run project we need to set up enviroment properly. It could be done using docker but I made it python venv way.
It's recomended to use python 3.6 - 3.8 as on other pythons rasa face some working issues. I will try to present installation steps
dedicated for ubuntu machine.
    
    Go to project home path (ChatBot folder)
    
    sudo apt install python3.8
    
    python3.8 -m pip install virtualenv
    
    python3.8 -m venv venv
    
    source venv/bin/activate
    
    pip install rasa
    
If the menu.json file was modifed (if new dishes were added) we should extract it to build lookup table
    
     cd cfg
     
     python convertToYaml.py 
     
     cd ..
   
    
After this steps our virtual enviroment is setup and ready to work

## 4.2 Project discord setup

    TODO

## 5.1 Ubuntu terminal run

To run chatbot in ubuntu terminal we should do following steps

At first we need to train our model (make sure you sourced venv)

    rasa train
    
Then we need to run our rasa actions server to handle custom actions (recomended on separate console)

    rasa run actions
    
Finally we can launch our chatbot by:
    
    rasa shell
    
    
    
 ## 5.2 Discord run
 
 TODO
 
 ## 6 Known issues
 
- Was observed that rasa RegexEntityExtractor does not work properly with DietClassifier once slot is mapped from entity and does not have exactly same
  name. Problem is visible once we try to order dish with extra/ without some ingredient that is contained in lookup table but no train example was
  provided for this ingredient. As googled it seems by common issue.
  For example, by running
  
      ras shell nlu
      
    And typing 

      I would like to order burger with extra salt
      
      
  We can see that RegexEntityExtractor extract entity properly but DietClassifier can not extract slot properly.
  
  This problem is not vissible once ingredient was provided in train examples.
  
 



