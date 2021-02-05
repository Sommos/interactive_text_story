# importing any additional library resources #
import textwrap
import time

# the story text is stored in the variable 'story_text', then we use the textwrap library to print it to the terminal with line breaks automatically #
story_text = "As the sun started to set down and the sky turned jet black. Tony, who is a former CIA operative, and his daughter Sarah were snatched from their homes in the middle of the night and locked in a 20 by 20-foot cube shaped cell with a dimmed light bulb, stained mattresses and an old computer which only uses binary. The only way for him to be able to escape and spare himself and his daughter is to figure out a list of binary numbers which he will need to convert to English text. Time was the biggest enemy as he only had 30 minutes to complete and sprint for the exit door of the cell."
print("\n".join(textwrap.wrap(story_text, 60)))

# instantiate the variables for the timer used #
time_start = time.time()
seconds = 0
minutes = 0

# function for a countdown (this is posted in the terminal, and reduced by 1 second every 1 second) #
def countdown(time_input):
    while time_input:
        # instantiates the fact that the time_input is divided by 60 to achieve one minute of time #
        mins, secs = divmod(time_input, 60)
        # formatting used for minutes and seconds #
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # prints the timer, and pushes the users cursor to the next line #
        print(timer, end="\r")
        # forces the timer to sleep for 1 second #
        time.sleep(1)
        # removes 1 second from the time input variable, thereby reducing the timer by 1 second #
        time_input -= 1
        
    print("End of countdown, you have failed to complete the game in time.")

# if we want the user to adjust the time that they have? #
# time_input = input("Enter the time in seconds: ")

# we can change the countdown here, if we decide 30 minutes is too much/ too little time for the average user #
seconds_for_countdown = 1800
# instantiates the countdown function, and casts the argument to an int (1800 is the number of seconds in 30 minutes) #
countdown(int(seconds_for_countdown))
