# Complex-Number-Bot
Code for a Discord Complex Number Bot


Bot Commands:

$inputRectangular takes in two numbers, the real and imaginary components, and returns the magnitude, phase, and the polar representation while $inputPol takes in r, theta values 
and returns the rectangular representation.

Use the $powerRect command to raise a complex number in rectangular form to an integer power. Format: $powerRect Re Im exponent
For example:
$powerRect 1 1 2 is (1+j)^2 which equals 2j

Use the $multRect command to multiply two complex numbers in rectangular form. Format $multRect Re1 Im1 Re2 Im2
Use the $powerPolar to raise a complex number in polar form to an integer exponent. Format: $powerPolar r theta exponent

Use the $multPolar to multiply two complex numbers that are in polar form together. Format $multPolar r1 theta1 r2 theta2

The code for the Bot is in main.py.

The Bot is run on Repl.It and Flask and Uptime Robot are used to ensure that the bot is available nearly continuously, even when I am logged off. 

This Bot is already used in two academic Discord channels related to Signal Processing classes, with a combined membership of 250 people. 

To add to your discord channel, visit https://discord.com/api/oauth2/authorize?client_id=805595312131539004&permissions=0&scope=bot
