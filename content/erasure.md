Title: Erasure Code
Date: 2014-02-14 21:43
Category: Hermes
Author: William Mak
Summary: Wnat is Erasure code? Why are we using it for Hermes?

# Forard Error Correction
To first understand Erasure Code, one must first understand [Forward Error
Correction](http://en.wikipedia.org/wiki/Forward_error_correction) code, which
erasure code is a type of. Forward Error Correction is commonly used to solve 
the issue of repairing data lost in a network transfer. This is done by sending 
a file with additional redundancy. A very simplistic example of Forward Error 
Correction is to send each bit of data three times and choose the most common 
occurrence of what is received aka "democratic voting" or "majority vote". For
example if the source bit was **1**, and after being sent an error occurred it 
could end up as **0**. **But** with Democratic voting if the bit is sent three 
times then it would require it to fail at least twice in order for the receiver
to interpret the data incorrectly. Though simple to implement, this type of
Forward Error Correction is relatively... very terrible since this
implementation would take triple the bandwidth and only really allows the signal
to fail once. 

# Erasure Code
Erasure code which is a type of FEC can take a message and encode it in such a
way so that the original message can be decoded even if parts of the message are
lost in transmission. Erasure code does this by treating the original message as
a set of k symbols. It then extends these symbols to a longer set of symbols n,
these are then the symbols transmitted. Which so long as k` of the symbols are
transmitted the original set of k symbols can be reconstructed. A great
example of this is Polynomial Oversampling. If I wanted to transmit the symbols
'1020' I would do the following:

1. Split the message into two parts ["10", "20"]
2. Extend the the message by [interpolating the
function](http://en.wikipedia.org/wiki/Polynomial_interpolation) so 
now the message might be something like ["10", "20", "30", "40"]
3. transmit the message as something like "1=10", "2=20", "3=30", "4=40"

Now on the receiving end

1. If the receiving side only receives 2 of the messages ie ["2=20", "4=40"]
these values too can be interpolated (ie f(i) = 10i)
2. using the resulting function the first two values can then be recalculated
so f(1)=10 and f(2)=20
3. now the original message can be reformed by joining the two values "1020"

Now erasure codes come in varying degrees of efficiency, normally measured as 
k/n known as the code rate since the smaller this number is the less extra data 
needs to be transmitted. So with the Polynomial Overampling example above since
twice the number of symbols were generated it would have a rate of 1/2. 


There is also this other type or erasure known are rateless erasure codes of
fountain codes which has been covered
[here](http://mattolan.com/blog/the-basics-of-fountain-rateless-code.html) quite
well and which I will go over in a future porst at some time along with the Go
implementation of it that is being put in place for the
[Hermes](https://github.com/olanmatt/hermes) project.
