## sleeps_counter
# How many sleep is it until &lt;x>?

With my daughter turning 4 the question of how many sleeps it is until her birthday has become a daily ongoing concern.  She is also just learning her numbers, and we're trying to encourage her in that.  So as usual I turned to technology to take the strain!  I had a Pimoroni scroll hat sitting around that I'd got in a sale a while ago, and of course the Raspberry Pi Zero W is ideal for this kind of application.

The code is pretty simple:

* import the necessary libraries
* set the scroll phat settings that won't change
* then in the forever loop:
  * get the current date
  * put the date you're counting down to into datetime format 
  * work out the delta between the two
  * add 1 to get the number of sleeps required
  * if still not the date you're counting down to - set this to message 
  * if it is the date - set the special message to display

Because the numbers of days is a really short message and can be displayed in it's entirety without scrolling, I also set the scroll delta to 0 when it was displaying the numbers so it stayed still and made it easier for my daughter to read the numbers.
