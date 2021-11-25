Before using this repo make sure to enable the virtual environment.

Now follow the steps given below:

1. Open up your Virtual Environment

2. Git clone this repo
        git clone https://github.com/narenltk/Rasa_chatbot_narenltk.git

3. Now change directory to the folder in which you have cloned this repo.
    
4. From now on it is simple, just run the following commands
            rasa train

5. Once this is done, you're supposed to run the actions.py file in another seperate terminal,
            rasa run actions

6. If your connecting your rasa chatbot with webpage then you the following command,
            rasa run --enable-api --cors "*" --debug


7. If there aren't any bugs in then you can enter to the place where your can communicate with the bot
    
8. Go to the terminal where you have executed the rasa train and run the following command,
            rasa shell

9. Or if your using rasa x then
            rasa x

