Here are some description about some of the important files:-

NLU file:
- In NLU.yml file we have added training data for the bot. Provided all the possible inputs and defining entities inside them.

Stories file:
- In stories.yml file we have added two basic stories one for greet and another when user trying to find some covid related data.

Domain file:
- In domain file have defined the slot which we have created and entities same name as slots so that entities values can be stored in slots. Adn also defined intent and greet message as utter.

DateConvertorHelper.py:
- In date convertor helper file we are converting the date entered by user into specific format. In which we are getting data  from API .

RequestHelper.py:
- We are calling our api with the help of request helper file.

Actions.py:
- Firstly we are calling api and fatching all data from the API and storing it in a variable as response.
- Then fatching value which are stored in slot from user input.
- Checking whether date is entered by user or not. If present then filtering data on basic of date(which we have formated) and same for state name. Otherwise if date is not present we are continuing to filtering on basic of state name.
- After showing data to user , We are resetting the slots to None.


Before using this repo make sure to enable the virtual environment.

Now follow the steps given below:

1. Open up your Virtual Environment

2. Git clone this repo
        git clone https://github.com/rax143/bytelearn_assignment.git

3. Now change directory to the folder in which you have cloned this repo.
    
4. From now on it is simple, just run the following commands :-
            rasa train

5. Once this is done, you're supposed to run the actions.py file in another seperate terminal :-
            rasa run actions

6. If your connecting your rasa chatbot with webpage then you the following command :-
            rasa run --enable-api --cors "*" --debug


7. If there aren't any bugs in then you can enter to the place where your can communicate with the bot
    
8. Go to the terminal where you have executed the rasa train and run the following command :-
            rasa shell

9. Or if your using rasa x then :-
            rasa x

