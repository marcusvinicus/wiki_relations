wiki_relations
==============

Explore two ideias:
-------------------

The first ideia is to do something similar to [wikiviz][], but with a different approach. There is also a wikipedia's page elected as the center point from where our analysis begin. The difference is that instead of using the links to other pages found in the central point, see what are the other pages edited by the editors of the central point.

The other one seems to be already developed. It consists to [cluster the users][] based on the pages edited by then. If two users edited the same page, they are, somehow, connected. The extension of the ideia is to build a social network around this concept. There is some study about [wikipedia editors][] and how they behave.

Using the WikiMedia API
-----------------------
*   Listing the last 100 users that edited the page Physics:

    [http://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Physics&rvprop=user&rvlimit=100]

*   Listing the last 100 editions by user Filelakeshoe:

    [http://en.wikipedia.org//w/api.php?action=query&list=usercontribs&format=xml&uclimit=100&ucuser=Filelakeshoe]

*   Link to the API Sandbox:

    [http://en.wikipedia.org/wiki/Special:ApiSandbox]


Other details:
-------------

There should be some way to calculate weights from the connections. Probably there are users that edit lots of pages and users that edit just a few related pages.



[wikiviz]: http://www.chrisharrison.net/projects/wikiviz/
[dumps]: http://dumps.wikimedia.org/enwiki/
[dbpedia]: http://dbpedia.org/About
[article at hackdiary]: http://www.hackdiary.com/2012/04/05/extracting-a-social-graph-from-wikipedia-people-pages/
[cluster the users]: http://jace.zaiki.in/files/2009/05/19/cis-wikipedia-report1.pdf
[wikipedia editors]: http://ai.stanford.edu/~west1/pubs/wikiedits.pdf