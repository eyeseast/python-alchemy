Alchemy in Python
=================

Alchemy is a utility for extracting text from web pages. Give it a URL and it will return the main block of text.

Usage:
-----

    >>> from alchemy import Alchemy
    >>> alchemy = Alchemy(API_KEY)
    >>> alchemy.url_get_text('http://www.pbs.org/newshour/rundown/2010/09/x-prize-winning-automobile.html')
    "For even the biggest projects, the devil is always in the details. In late August, the NewsHour profiled a small group of race car enthusiasts in Lynchburg, Va., who have made what they say is a revolutionary new automobile. Its diamond shape and extended wheels look quite different from anything you see on the road today -- but it's all the little parts that have been redesigned and manufactured by Edison2 to allow their car to get the equivalent of 100 miles per gallon. Oliver Kuttner, a real estate developer who has owned and driven race cars, founded his team of engineers and mechanics to win the Progressive Automotive X Prize. To win the mainstream category, Edison2 needed to design and build a car that can get the equivalent of 100 miles per gallon in all driving conditions, travel at least 200 miles without refueling, and seat four passengers. Initially convinced the solution would be an electric or hybrid vehicle, Kuttner and team soon discovered the key to efficiency was light weight and aerodynamics. So, their "Very Light Car" is just that, very light. It weighs in at less than 800 pounds, in part because of an emphasis on a simple design. But the team also made all their parts much lighter. Many of the components of the Edison2 car are just one-tenth of the weight of similar parts you would find on your automobile. Here's a clip of the car on a test track and of our correspondent Judy Woodruff giving the ultra light vehicle a push: We thought we'd follow up with some of the nuts and bolts. Well, at least the nuts. Edison2 gave the NewsHour a lugnut from the "Very Light Car" as we left their Lynchburg factory. It looks like your average lugnut until you put it in your hand. Instantly, you notice it is much lighter than it looks. We decided to drop it on a scale and compare it to a lugnut from one of our cars. The results -- an ordinary lugnut weighs about 36 grams and the Edison 2 X Prize lugnut was 11 grams -- reveal how rethinking, and building from scratch contribute to the much bigger goal of making an extremely efficient car."


