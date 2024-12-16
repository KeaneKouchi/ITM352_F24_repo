Prof. Kazman,
Both this readme and the requirements.txt were submitted to GitHub repo after the deadline,
I cannot expect credit for these but I felt it was important to include them.
I could not for the life of me figure out the virtual environment in Python, after following
the first couple of steps I got an error and decided to try testing the install package 
manually and deleted the VE folder but then every time I tried to run the app it would refer 
to the virtual environment that was supposedly not even working. Honestly I can't even remember
how I got it to work. But while I'm here I wanted to say thank you for a great semester! I took
ICS 111 like 9 years ago (when it was Java) and was actually convinced to not pursue computer science 
because of it (those darn semicolons). But you have made learning Python both enjoyable and mentally
fulfilling so thank you again!

With Best Regards,
Keane

Setup:
1. Open VScode and open the terminal
2. Change the directory to where the Flask app is stored
3. Run this command in the terminal-

   pip install -r requirements.txt

*** Note this may take a while depending on which dependencies you already have installed.

4. After the required packages are successfully installed, run the flask app by typing the
   following into the terminal-
   
   For windows users:
   python main.py

   For MAC users:
   python3 main.py

5. Upon seeing the following in the terminal:

 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 415-086-633

Open your web browser and go to:
   http://127.0.0.1:5000/

The webpage titled "Stock Information" should be displayed.

Instructions for use:
1. Type in the ticker symbol of the company whose stock information you want to see.
2. Click on the "Get Info" button.
3. If you want to add the currently viewed stock to your Favorites list, click the 
   grey star next to the "Get Info" button. To access the favorites list, click on the
   blue favorites button to the left of the search bar. To remove a stock from the favorites,
   click the red X.
4. For metrics customization, first choose a display font size or leave on the default size.
   All boxes (metrics) will be checked by default, uncheck any that you want to remove from
   view. Recheck them to display them again.
5. Social Media sentiment and news sentiment will update when selecting a stock.
   --- See note on lack of data display for social media sentiment (all stocks) and
       News sentiment (only available for AAPL) due to API demo mode limiitations.
          --- Please search for AAPL when initially selecting a stock and scroll down to the
              News Sentiment section for an example of what both sentiment tools should display
              with the non demo API. 
       -- Note in comments of the code also.
6. The historical data candlestick chart will show the stock that was initially selected
   and will update when either a new stock is selected or the same one is reentered.
   - Use the dropdown menu to select a time period to view.
7. In the Compare Stocks section, enter 1(min)-3(max) different ticker symbols (in separate boxes), 
   choose the timeframe from the dropdown menu, and click the "Compare" button.

Thank you for using my app!