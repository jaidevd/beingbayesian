# TUS Investigation

The 2024 Time Use Survey covers the entire country apart from some inaccessible
parts of Andaman & Nicobar, and is administered over the whole year to account
for seasonal variations. For each respondent, it records the time spent on
_everything_ in the last 24 hours in 30 minute intervals. As such, it presents a
exceptionally detailed view of how people spend their time. The
survey data is rich beyond an analyst's dreams... after losing myself for weeks
in the labyrinth of the various possibilities of filtering the data and designing
sample cohorts, I've settled down on a ruthlessly simplified but still rigorous
approach to the data.

For one, I will be writing about that subset of the population which is most
likely to be at the recieving end of productivity-shaming: salaried white-collar workers. 
The TUS helpfully includes a field which
records whether each respondent was involved in an economic activity, and if so,
whether they were self-employed or salaried. In addition, the survey also
records the industrial classification (NIC 2008) of the relevant economic activity.
With a combination of these two and the typical working age (15-60
years), I created filters which indicate whether someone can be asked to work
for 90 hours a week with a straight face.

Even this modestly-sized sample of the white-collar workforce is still quite
fertile. Fortunately, there's no demographic which is excluded from it. People
of all religions, castes, educational backgrounds, ages and genders (three of them) find decent
representations in the sample. Of these, some are more indicative (meaning,
correlated with) the use of time in specific activities than others, as we shall
see. The effects of some of these demographic variables are subtle, they show up
only in very nuanced conditions and with smaller effects. Others jump right off
the computer screen. The biggest example of the latter is gender. The _fact_
that time use is gendered wouldn't surprise anyone, but the _extent_ of the
effect of gender is staggering. Gender beats all other attributes of the
respondent by far, and there's no way you can manipulate the data
which makes this effect disappear.

![](assets/week.png)

If we simply look at the average time men and women spend on different types of
activities and adjust it for the week, the picture doesn't look bad at all. Both
men and women spend about 85 hours a week on self-care and maintenance. This
includes activities like sleep, personal care and hygiene and non-social eating
and drinking. Men work nearly 56 hours a week, and women work 48.6 hours a week.
This translates into women working only an hour less than men every day. If
you've wondered if your female colleagues seem to consistently leave the office
earlier, here is statistical proof.

It's in the next category of activities that things get interesting. Women spend
four times as much time on chores (they're designated as "unpaid domestic services for
household and family members" under ICATUS) than men. Activities under this
category involve working in the kitchen, doing the laundry and other
miscellaneous household management. In our quest for the 90 hour workweek, it's
pointless to look at anything but the largest component of chores, and that is
the kitchen. 

![](assets/kitchen.png)

Here, too, the magnitude is more surprising than the direction. We'd expect that
men spend much less time in the kitchen than women overall in the country - and
we'd be right. But to see that happen even in the a small, presumably
emancipated section of the population is shocking. Even among the salaried class
with skilled jobs, men barely spend an hour cooking. Moreover, cooking is only
a part of kitchen work - there are also the allied activities of serving food and
cleaning up after, where men are insultingly absent. This is reminiscent of a
scene from the Malayalam movie _The Great Indian Kitchen_ (which was also
captured well in it's Hindi remake) where an overbearing relative decides to
make dinner and leaves the kitchen in a mess.

Other factors associated with kitchen time - like marital status, education and
household weath - also influence it in expected ways. But the relationship
between them and time spent in the kitchen isn't just monotonic - it is
_extreme_. The women who come from the wealthiest quartile spend nearly three
hours less in the kitchen than those from the second wealthiest quartile. Women
with graduate degrees spend nearly 12.5 hours per week in the kitchen, and as
education drops to higher secondary, the time spent almost _doubles_. Going from
being single to being married increases the time spent in the kitchen by a
whopping ten hours per week.

The time spent in chores (particularly in the
kitchen and otherwise in cleaning and laundry) is inversely correlated to the
presence of labour-saving devices and methods in the household. This is not
surprising, but it _is_ statistically significant. What is surprising is that
these devices don't have as large an effect as we'd expect. Come to think of it,
washing machines, refrigerators, microwave ovens and vacuum cleaners are
technologies that are old enough to have revolutionized chores. They are
generally reasonably priced, too. Given that we're talking about a relatively
better off section of the population - why don't we see a larger effect? I don't
have a clear answer, but I did get a very interesting perspective from Krish
Ashok, in one of his most interesting podcast moments...

> ...optimizing cooking time with appliances is a progression. My grandfather
> didn't like rice cooked in a pressure cooker. A generation before they didn't
> like stoves, and preferred wood fires. Nowadays they don't like microwaves
> and air fryers and say that refrigerated food loses nutrition. Whenever
> there's a new tool for improving kitchen productivity, there will be an
> entire generation of men and women resisting it...

Anyhow, for the sake of argument, let us allow ourselves, for the time being, to
dream of a world where both men and women spend significantly less time on
chores. Let's say, optimistically, that both genders spend no more than an hour
a day on chores, and pump all the remaining time into work. Even in this
ridiculous world, women's work time would grow only to 67 hours a week. The
situation for men would not change since they already work less than an hour per
day on chores. To hit the 90 hour / week target, there's still a large deficit -
22 hours for women and 34 hours for men. At this point, work has no choice but
to eat into sleep and leisure.

![](assets/remaining-time.png)

This is probably the only chart in my entire analysis which looks gender
balanced. In fact the only small imbalance I see is that men watch TV for a
couple of hours longer than women (presumably when their wives are in the
kitchen). Otherwise both genders spend comparable amounts of time sleeping,
talking, eating and otherwise chilling. It must be noted, however, that I've
wrought an anomaly here by cherrypicking a specific cohort - otherwise, in general,
time spent on leisure and self-care is also heavily gendered. For instance,
women take 2.3 times as long as men to use the toilet - there's no way that
personal care and hygiene costs both genders the same amount of time across the
country. Even socialization and
relaxing can mean different things to both genders. In her book _Whole Numbers and
Half Truths_, Rukmini S writes some very interesting examples of how leisure
means different things to different sets of Indians, particularly to men and
women.

But as far as this cohort of salaried white-collar workers is concerned, this
chart tells us that there's a lot of productivity still to be squeezed out. For
example, both men and women could do with an hour less of sleep everyday. For
one, seven hours a night is by no means cruelly short. For another, every
productivity guru worth their salt will tell you that it's the quality of
sleep that matters more than the duration. That's seven hours added to the respective deficits right there! 

When it comes to talking, chatting and texting, 15 hours a week looks
downright excessive. All 10-12 hours of watching TV could be cut down. There's
certainly some some creative incentive that managers can come up with to get
people to cancel their Netflix subscriptions and delete their Instagram
accounts. In fact I'll go so far as to say that even personal care and hygiene
can be sacrificed. Ask Bhavish Agarwal - for someone who claims to work 20 hours
a day, he certainly looks quite well groomed. Of course, haters could always
ask why 20 hours a day isn't enough for him to make his customers happy. If
we're going to make reasonable arguments that time spent on work is no guarantee
of quality, this whole post is moot.

---

A colleague of mine once took a picture of a couple of his teammates sitting with
their laptops open in the back of an autorickshaw, all in the middle of a busy
Hyderabad street. The marketing team picked it up and used it in a social media
campaign with hashtags like #hustle, #dedication, #productivity, etc. All I
could think of was what a potential client might think about the quality of our
work if we were so busy hustling.

Another colleague once posted a picture of himself sitting on his desk, hunched up
over his laptop with the
caption, "burning the midnight oil after everyone has gone home." Someone
asked him who took the picture if everyone had gone home. He didn't reply.

I don't honestly think that people actually confuse time with productivity.
Nobody is that stupid. But knowledge workers aren't turning out widgets on an
assembly line. Time spent is perhaps the only lead metric of productivity we have.

The single most enjoyable thing about being a programmer is the obsessive
pursuit of a complex problem. Every good programmer has a lot of experience
with spending hours and days holed up in a room with an unhealthy disregard
for food, sleep and general well-being. It is the cost of what we do. It is why
we're able to take any pride in our craft. It's the rite of passage of every
true hacker. And they suffer from it, too. I recently ran into some old
friends at a conference. A decade ago, we could talk of nothing but the hustle.
This time we only complained about our backs, our necks and our cholesterol
levels. So, I understand only too well the appeal of working longer hours. It's not that
I'd never sell long hours to my younger colleagues.

But I see bullshit when I see it. Long hours were never sold to me on a
platter of nation building. It took me a while, but I recognized what enables
me to work long hours - I acknowledged my privilege. And the best way to sum up
the acknowledgement is this quote from Stephen King:

> The combination of a healthy body and a stable relationship with a
> self-reliant woman who takes zero shit from me or anyone else has made the
> continuity of my working life possible.

But when people ask you to work ridiculously long hours, healthy bodies and stable
relationships are exactly the kinds of things they want you to give up.

It will never work.
