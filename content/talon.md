Title: Talon
Date: 2014-09-18 11:54
Category: Programming
Author: William Mak
Summary: What the hell is Talon and what does it do?

# Talon
Talon is a relatively trivial way of storing latitude and longitude in 4 unicode
characters. It's intent is to shorten location urls when you're mentioning
somewhere to someone and want to send that in a url. Before Talon the only way
to send a location to someone else would be to go into google maps, find that
location and then grab the url which would look something like the following:
<a href="https://www.google.ca/maps/@38.6059681,-28.0261396,16z?hl=en">https://www.google.ca/maps/@38.6059681,-28.0261396,16z?hl=en</a>
Even then the location given is just a region of the map, if you wanted a Marker
at that location the best way to do that is to ask for directions to that spot
and then grab the url again, which looked something like this: <a href="https://www.google.ca/maps/dir//38.603654,-28.0262469/@38.6036228,-28.1636668,11z/data=!3m1!4b1!4m3!4m2!1m0!1m0?hl=en">https://www.google.ca/maps/dir//38.603654,-28.0262469/@38.6036228,-28.1636668,11z/data=!3m1!4b1!4m3!4m2!1m0!1m0?hl=en</a>
These urls are much too long to send to someone over a chat window or within a
tweet or in a text message. This is where Talon comes in, talon takes what would
have been these long urls and shortens them to something nice like this: 
<a href="http://wmak.io/talon.html?♁踷똊Ⴓ齼">http://wmak.io/talon.html?♁踷똊Ⴓ齼</a>
this isn't a url shortener rather Talon encodes a latitude and longitude up to
to seven decimal places. Which means the location stored is 
<a href="http://gis.stackexchange.com/questions/8650/how-to-measure-the-accuracy-of-latitude-and-longitude">accurate up to 11mm.</a>

# So how does Talon work?
Talon has 4 characters to work with, and given the state of the web these
characters can be assumed to be in utf8. This means that there are 65535
possible symbols per character. Talon assumes the first two represent Latitude,
And the second two represent Longitude. The possible combinations per set of
characters then is 4294836225. We also know the range of possible numbers.
Latitude which is from -90.0000000 to 90.0000000 and Longitude which is from
-180.0000000 to 180.0000000. Become of the limitations of the combinations the
first value can be 0, 1, 2, or 3 if the first number was 4 then the second
number would be limited to 2, and so on. In which case the numbers were used as
flags:

* 0 means the number is negative
* 1 means the number is negative and below 90
* 2 means the number is positive
* 3 means the number is positive and above 90

So to store a number n the algorithm would be as follows:

1. Which flag does the number fall under? set the first digit as such.
2. If abs(n) > 90 then let n ±= 90 so that abs(n) <= 90
3. Remove the decimal point from n
4. Append the digits of n to the result
5. Truncate the result so that it's 10 characters long
6. Find the Hexidecimal representation of the result
7. The final result then is the unicode representation of the first 4 characters
   of the hex and the last 4 characters of the hex.

# What's next?
Talon is currently implemented in Python and JavaScript but further
implementations are planned and are currently being worked on. See the 
<a href="http://github.com/wmak/Talon">Github</a> pages for more information
