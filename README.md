Connecting Wikipedians
======================

**This is a work in progress. I admit that I don't quite know the enviroment that the wikipedia editors "live" so there is a strong possibility of stupid things being said bellow.**

The ideia of connection by editions:
------------------------------------

Suppose there are three [wikipedians][]: Alice, Bob and Charles. Alice is mainly a content editor of Physics related pages. She has made editions to improve the quality of the [Mechanics][] and [Archimede's principle][] pages. Bob has done some research at college about Greek Culture and has contributed by editing the Archimede's principle and [Greece][] pages. Charles is only interested in History right now and has made changes in the Greece and [Archeology][] pages.

![Alice, Bob and Charles' connections][graph]

[wikipedians]: http://en.wikipedia.org/wiki/Wikipedia:Wikipedians
[Mechanics]: http://en.wikipedia.org/wiki/Mechanics
[Archimede's principle]: http://en.wikipedia.org/wiki/Archimedes%27_principle
[Greece]: http://en.wikipedia.org/wiki/Greece
[Archeology]: http://en.wikipedia.org/wiki/Archeology
[graph]: https://github.com/ludug3r0/wiki_relations/blob/master/graph.png

Alice is connected to Bob through the Archimede's principle page. And Bob is connected to Charles through the Greece page. We can connect those people by interest using theirs editions. If two users edited the same page, they are, somehow, connected.

The target is to create a kind of social network over this concept. More precisely a interest network where the users are connected to each other by the contents that grab their intellectual interest.

Transmitting bits of knowledge:
-------------------------------

Suppose Alice has some doubt or something to say about the Archimede's principle. Bob is connected to her so it is interesting to him to see what Alice has to say. Alice's message is then trasmitted to Bob. Charles, on the contrary, does not share interests with Alice, so the message is not exposed to him.

There is a flaw in the example above. If Alice want to talk about mechanics, Bob will still receive the message even so he is not interested in mechanics (remember Bob is only interested in Archimede's principle and Greece).

The example given is a bit too simple to fully expose the concept. The truth is that there are lots of wikipedians and lots of pages edited by each one of them. This would result in a lot of users connected to Alice receiving the message. The concept of connection should be improved by adding some weight reflecting the interest level of the user over a content. This way, it is possible to sort users by connection strenght and a message created by Alice is shown only to just a few, minimizing the flaw.


Effects of the ideia:
---------------------

There are some expected effects of a proper implementation of this ideia.

*   Exchange of knowledge made easy

	This is basically the example given above. Alice's message is exposed only to a corpus of people that hopefully knows something about the subject. This way the others users are not cluttered with lots of messages that don't concern them.

*   Growth in the wikipedians population

	This can be a two edged sword. Even so, it would be a good thing to increase the number of wikipedians by bringing new users and theirs different views about the world, a flood of new users can be quite daunting.

*   Clustering users around an expertise area

	There is already some experiment around this ideia. It consists to [cluster the users][] based on the pages edited by then. This could provide a easy way to find a corpus of specialists about an specific subject. 

*   Connecting and clustering pages

	 The same way people are connected through the pages they edit. Pages can be connected through editors. With this concept pages can be clustered around a bigger subject. The Mechanics and Archimede's principle can be grouped in a cluster of Physics related pages. This way, a user can receive suggestions on pages that he could contribute if he wishes.

[cluster the users]: http://jace.zaiki.in/files/2009/05/19/cis-wikipedia-report1.pdf
