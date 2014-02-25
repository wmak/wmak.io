Title: Iris
Date: 2014-02-24 23:06
Category: Iris
Author: William Mak
Summary: A quick overview of how the image analysis for Iris works

[Iris](https://github.com/IrisConstruct/iris) is an image analysis program that
given a manifest file, and a set of images will return the relative positions of
each capturing camera from one another. For example the follwowin two images
were taken by two phones beside each other. This one on the left: ![left
image](https://github.com/IrisConstruct/iris/blob/master/src/img/a.jpg?raw=true)
and this one on the right: ![right
image](https://github.com/IrisConstruct/iris/blob/master/src/img/b.jpg?raw=true)

So how do i find which picture is which? Well they are very close to one another
so I then used this to my advantage to use opencv to find
the matching landmarks between the two images. It then returns the following
image. ![comparisons](http://wmak.io/images/iris.jpg) 

Now that I have found the matching points in the two images I can find there
distances from the left side of the image. This then tells me there relative
positions. This is because the left camera will see the same landmarks further 
to the left and the right camera will see the landmarks further to the right.
This seems anti intuitive especially if you try moving your head left and right
while staring at an object you will see that on the left the object will appear
furhter to the right. The reason the code is the other way around is that images
are mirrored by the front camera phones.

So there we have it, at the code will return a "matrix" of scores that are then
used by the backend code to crop and position an image or video:
`{'scrs': [{'ip2': u'192.168.0.5', 'ip1': u'192.168.0.5', 'score': 0.0}, {'ip2':
u'192.168.0.6', 'ip1': u'192.168.0.5', 'score': 65.76188568516939}, {'ip2':
u'192.168.0.5', 'ip1': u'192.168.0.6', 'score': -17.09808192707039}, {'ip2':
u'192.168.0.6', 'ip1': u'192.168.0.6', 'score': 241.95999999999995}]}`
