Earlier this year, claims like these went viral all over LinkedIn:

![](https://media.licdn.com/dms/image/v2/D5622AQGBvBHwQyZbXA/feedshare-shrink_1280/B56Z0_gr1lG8AM-/0/1774887026323?e=1787788800&v=beta&t=M1-ZOWjQPYthNYenOWRL7SWPCtBjjIfgiIh-iiKRpRc)

Source: https://linkedin.com


> In the beginning... was the command line.

\- Neal Stephenson

Well, not really. Before the command line was the punch card, and before that
were the various knobs and dials and patch cords of early computers. Today we
use graphical user interfaces (GUIs) - things you can see and point to and click
on. Even as the means of interacting with a computer have grown easier, the
ability to program them has become all the more specialized[^1].

Nevertheless, for every currently living computer programmer, in the beginning
there was indeed the command line. For better or for worse, skill at the command
line remains, even today, the litmus test of a good programmer. I doubt if that
is universally true. I've seen enough good programmers who can't (or don't) use
the command line, and prefer pointing and clicking. But I'd wager it's
statistically true. Being dexterous at typing commands instead of navigating
menus and dialogs is huge time saver. It's similar to the difference between
touch-typing and hunt-and-peck typing. Imagine trying to teach your nephew how
to play Call of Duty: after he manages to kill his own teammates six times in a
row, it takes all the restraint you can muster to not snatch the controller
away.

I myself hate taking my hands off the keyboard towards the mouse - so I'm
certainly heavily biased towards the command line. But I don't judge those who
are not. There are better programmers who are not particularly invested in the
command line experience, but they'd still know their way around it. Secondly,
while getting good at the command line takes years, getting started is not
all that hard. What really exasperates me, however, are those who doggedly
avoid the command line in favour of GUIs, and _still_ end up fumbling
around, wasting time and ultimately making mistakes.

I recently encountered an intern doing something similarly exasperating. He'd
been asked to debug a program. After repeated attempts, the variety of bugfixes
didn't work. Standing behind him[^2], I noticed many places where he could have
been significantly more efficient. Here, a distinction needs to be made between
the reasoning skills needed to debug a program, and the dexterity needed to
deploy the solution. My disappointment was directed solely at the latter. He
kept clicking on the wrong thing in the wrong menu. At first, he was gently
nudged towards using the command line. Then he was encouraged, and finally
sternly warned. He was made a full-time employee soon after, but didn't survive
the probationary period. His peers were more productive by far, and decided that
they'd rather invest in someone who wasn't doggedly avoiding learning an
obviously high-RoI skill.

But as I write this, I realize that I myself was perhaps not so different when I
was an intern, fourteen years ago. Just as one feels embarrassed looking at
their old photographs, I'm embarrassed at my old coding habits. Particularly
embarrassing is my Stack Overflow profile. I've asked a grand total of five
questions; two of which have been deleted. One of the remaining three is
outright embarrassing - the kind of question that today I would fire myself for
asking. The other two, while not as silly, are still the desperate attempts of
someone who doesn't know how to perform a good web search. And then there are my
answers. Far less embarrassing, but still answers to precisely those questions
that a person like the past me would have asked. In fact, I was precisely
someone who deserved to have their job taken away by AI. Even today, there are
enough such people around in workplaces that it feels like AI is just around the
corner, ready to blindside the naive knowledge worker.

Many developers have very interesting Stack Overflow stories. A friend once told
me how during his internship he was tasked with a particularly difficult
problem, and no matter how far and wide he looked on Stack Overflow, the only
related questions he saw were from other interns before him who'd failed to fix
the problem, and the only answers he saw were from his boss: the very person who
gave him the problem in the first place.

![](https://imgs.xkcd.com/comics/wisdom_of_the_ancients.png)

It's an institution that's hallowed and controversial at the same time. For no
small number of programmers, their reputation on Stack Overflow has translated
into real professional reputation, to the point that reputation-farming on
Stack Overflow was even a valid strategy for career progress. On the other hand
people also have stories about how the platform made them feel unwelcome, to the
point of being positively toxic. I'm not proud to admit this, but it's not
entirely impossible that I myself might have played some part in shaming an
unsuspecting novice. But, all in all, Stack Overflow has been, for the better
part of the last 20 years, quite central to software engineering.

So, as transformative[^3] as LLMs have been, claims that ChatGPT has 'killed' or
'destroyed' Stack Overflow seem quite overblown—not least because they are viral
and loud in the first place, but also because a reduced volume of transactions
is by itself hardly good enough as a measure of the health of that platform.
Luckily, this is something for which data is readily available.

---

As a source of information, Stack Overflow is rich in more than one way: not
only as a place where answers to popular programming questions are concentrated,
but also as an organization that conducts annual user surveys, and regularly
archives its own data in a publicly accessible, structured format. The survey
data has long been seen as the pulse of the profession, but also, many suspect,
has a strong self-selection bias—in that respondents are already more likely to be
active on Stack Overflow. On the other hand, the data dumps are a treasure.
Every question, every answer, every edit and everything there is to know about
every user lies buried somewhere in the archive which is nearly half a terabyte.

And like every large social network, what is fascinating about it is the sheer
nonlinearity of it. For example, even with my sparse set of questions and
answers, I have a reputation of 3,144. This means[^4] that I'm at the 99.68th
percentile. Only _a third of a percent of all Stack Overflow_ users have a higher
reputation. But here's the kicker: there are nearly a hundred thousand of them!
The highest reputation ever is at a million and a half: three orders of magnitude
higher than where I am. Even if I were so inclined, scaling that peak is going
to take me multiple lifetimes.

No matter how large the data grows, the _information_ contained in it is
concentrated in a tiny manifold—much like the nucleus of an
atom. Once we are no longer overwhelmed by the sheer magnitude of things, the
pattern here is surprisingly common: the Power Law distribution. In every
socioeconomic system, influence and reputation are almost always highly
concentrated in a vanishingly small fraction of the population. In wealth and
income distribution, this is exactly what we refer to when we say that the rich
keep getting richer. So when people say that ChatGPT and other LLMs destroyed
Stack Overflow, it's worth asking whether it was the nucleus that was destroyed,
or the cloud of possibilities around it.

It's not hard to imagine that generative AI could indeed destroy the
astronomically long tail. But could it also destroy the nucleus, and in doing
so, _properly_ kill Stack Overflow?

At the outset, let's acknowledge that monthly activity on Stack Overflow _did_
decline. There is indeed a steep drop in the number of questions asked since the
end of 2022. The question, however, is whether that particular point in time had
anything to do with the drop. Imagine, for instance, that the release of ChatGPT
was _not_ annotated on the graph. Then we could still see the drop, but we would be
tempted to trace it all the way back to the peak of the COVID-19 pandemic (which
is also annotated on the graph). Would we then say that the pandemic, like so
many other people and organizations, killed Stack Overflow too? If anything,
that would be a more plausible explanation, especially since activity peaked
drastically at the peak of the pandemic—the taller it stood, the harder it fell.
The point is that annotating graphs with events makes for really good
storytelling, but it also leads the witness. So the simple antidote to this is
to stop comparing data from before and after a fixed timestamp, and look at the
trajectory as a whole. When seen this way, even the pandemic appears as an
inflection point.

Moreover, ChatGPT wasn't the only disruption that happened after the pandemic.
First, Stack Overflow was acquired by Prosus in June 2021. Around the same time,
Github released their AI coding assistant, Copilot, which would certainly have
made asking _some_ questions on Stack Overflow pointless. Later in mid-2023,
there were a series of layoffs, an AI moderation policy, and moderators went on
strike. In 2024, Stack Overflow announced strategic partnerships with
Google and OpenAI—which meant, at the very least, that partners did not have to
scrape training data off Stack Overflow anymore, they could acquire it
officially. Ultimately, each of these events can be seen as a candidate explanation (albeit
of varying strengths), and the "before
and after" narrative ends up being entirely qualitative, no matter which
disruption event we're looking at—including ChatGPT. The more interesting
possibility is that we're looking at a much longer trend that predates
all these disruptions, and that there are factors that aren't visible
through monthly activity.

# Substitute for Another Guy

Six months ago, in an interview with Nilay Patel of The Verge, Stack Overflow
CEO Prashanth Chandrasekar said that the decline was primarily in simpler
questions—more complex and advanced questions continue to be asked just as much,
since LLMs are only as good as the available knowledge. This gives us a good
heuristic—not all questions are equal. We then distinguish "good" questions, as
questions that were never marked as duplicates (something that plagues Stack
Overflow significantly) and remained highly upvoted later[^5].

![](assets/questions-time-series/genuine_vs_all.png)

Through this lens, we see that even the good questions have been declining since
2017—but steadily, not drastically. There's not a single steep drop anywhere.
This, perhaps, indicates that while we may attribute declining volume to various
events, the nucleus began eroding a long time ago. Have people been gradually
running out of good questions to ask? That seems like a good explanation, but it
does not stand up to scrutiny.

![](assets/questions-time-series/saturation.png)

Extrapolating from pre-ChatGPT trends, we can see that only a year after the
release of ChatGPT, good questions were at only half their expected volume. By 2025, they
were at 7% of where they would have been. So even if users were gradually
running out of good questions, that process cannot explain what happened next.
Around the release of ChatGPT, the series breaks sharply from a trend that had
held for years. This calls for further refinement: if asking 
good questions didn't help the survival of activity, then perhaps we need to
look at what these presumably good questions were _about_.

Short of analyzing the textual content of questions and answers (which would be
exceptionally rewarding, but prohibitively expensive for me), the best place to
look for the "about" is the tags which users and editors attach to questions.
The researcher Nadia Eghbal mentions a classification of software tools into
frameworks, languages, libraries and web and application servers. She used this
taxonomy in the context of open source software projects on
GitHub[^roadsbridges], but the same can be extended to Stack Overflow tags. This
helps us understand _what_ was affected most.

![](assets/tag_heatmap.png)

And the overwhelming answer is: everything. The technologies had very different
histories before 2022, but by 2025 almost every part of the programming
ecosystem represented on Stack Overflow had fallen to a small fraction of its
2022 volume. A minor nuance is that of all categories, libraries were hit the
hardest, more than frameworks and languages. Some frameworks did gain traffic
temporarily, but those were, unsurprisingly, LLM frameworks themselves.

An explanation for this near-universal collapse comes from a study by Robert
DeLine[^deline]. He studied the kinds of questions programmers actually ask
while working, some of which are general and portable: how to use an API, what a
function does, how to express some operation in a language. Others are intensely
contextual: why a particular piece of code exists, what state caused a failure, what
the program is supposed to do, or why something was designed a certain way.

Stack Overflow is extraordinarily well suited to the first kind. Its great
achievement was to take programming problems that arose in one person's work and
turn them into reusable public knowledge. Once phrased correctly, a question
could be detached from the program that motivated it and answered for everyone.
This also explains why the categories above matter less than one might expect.
What languages, frameworks, libraries and servers have in common is not their
subject matter, but that much of the general knowledge surrounding them can be made
portable.

LLMs are unusually good substitutes for precisely this kind of knowledge. They
do not need the programmer to locate the canonical question, discover the right
vocabulary, or translate their problem into somebody else's. The slightly larger
collapse in libraries fits this interpretation: questions of the form “how do I
use this API?” are among the easiest to detach from local context. But more
crucially, the effect extends far beyond libraries. Mark Guzdial wrote about a
study where the researchers found that people are surprisingly capable of
describing programming procedures; the
difficulty was not in the expression, but in navigating the abstractions
imposed by programming languages. Coding agents are meant _precisely_ to remove
this hurdle.

However, that alone does not mean that LLMs have forever solved software engineering.
Fred Brooks offers a useful way of seeing what this collapse of peer-to-peer
discourse does *not* mean. He distinguished the accidental difficulties of
programming—the machinery needed to express and manipulate software—from its
essential difficulties: deciding what a system should do and managing the
complexity inherent in it. Stack Overflow became a vast public repository for
overcoming a great deal of the accidental difficulties. This means that even
though traffic fell to a tenth of its previous volumne, this does not
automatically mean that software engineering is an order of magnitude easier
than it was before ChatGPT. LLMs or coding agents do little to attack the
_essential_ difficulties of programming. [Brooks
writes](https://jaidevd.com/posts/no-silver-bullet),

> The hard thing about building software is deciding what to say, not saying it.
> No facilitation of expression can give more than marginal gains.

Anyhow, as we return to our original question, we must admit (for my part,
somewhat begrudgingly) that ChatGPT _does_ appear to have killed Stack Overflow.
But before we hang up our Bayesian hats[^9], there is a third aspect to
consider. Stack Overflow isn't just the questions and answers, it's also a
community. It's not just a knowledge repository, it's a social network. Just as
we have seen _what_ changed and _when_ it changed, we must also ask _who_ changed.

---

# The Who By Numbers

It has been a mass exodus. Askers, answerers and editors[^usertypes] all
returned less and less often. After ChatGPT, they did not simply have lower
individual activity—there was instead a very conspicuous absence. I would have
thought that casual users would be the first to leave (which did happen), and
then the tide would slow. But even the presence of the highly reputed elite
core—who tried hard to not go gentle into that good night—halved. This is a sign
of the decay making its way through the electron cloud and reaching the nucleus.

![](assets/community/survival.png)

The community has always been extremely unequal (long-tailed Pareto
distributions): a tiny elite atop a huge casual base. The top 1% often produced
anywhere between one-third and two-thirds of all answers. But the exodus was
across not just reputation, but also by experience. Everyone, from first-timers
through the most seasoned veterans (100+ posts) fell by more than 90%. This alone invalidates the idea that ChatGPT removed only novices.

But alongside the concentrated core, there was another vulnerability that got exploited: Stack
Overflow, by many accounts, made newcomers feel quite unwelcome[^10].

![](assets/community/hostility.png)

Long before ChatGPT, the driving away of newcomers rose from 5% to ~18% over a
decade; while newcomers' return rates fell from ~58% to 42%. Unfortunately we
cannot read more into the casual lurker cohort of users, since their footprint
is hard to measure. But those would be exactly the kind of user who'd rather get
a non-humiliating answer from a machine that could (pretend to) be both patient and quick.

# Won't Get Fooled Again

What do we learn from this? Why would something like Stack Overflow work in the
first place? And why would it fall apart?

The first question is harder to answer. I think that people are often [motivated
by unreasonable things](https://youtu.be/5aH2Ppjpcho). There aren't
many ways of explaining why, for decades since the internet became mainstream, millions
of people shared knowledge for free. A lot of that content took hours to
produce, not to mention all the effort involved in editing it and moderating the
community. None of this is exactly rational behaviour.

But money wasn't the only currency. Daniel Pink divides the motivations for
doing difficult wor for free into autonomy, mastery and purpose. The digital
commons offered all three. You could choose where to participate, demonstrate
your skill, acquire a reputation and most crucially, have a shared purpose.
The digital knowledge commons turned individual autonomy,
mastery and purpose into a public good[^coasepenguin]. And it did so at an unprecedented scale.

César Hidalgo offers many useful ways of thinking about why this matters. An
individual cannot possess the knowledge and knowhow required to build a 
moderately complicated software system. Knowledge therefore has to be spread
across people. What determines, more than anything else, how much knowledge a group can collectively
possess is how easily they can form
links with one another. Expensive links produce small, heavy and slow networks. Cheap links
allow knowledge to be distributed faster among vastly more people. And trust makes those
links cheaper still.

Stack Overflow was, among other things, an extraordinary machine for lowering
the cost of such links. Voting, reputation and accepted answers supplied enough
trust to make advice from an anonymous stranger useful—the toxicity
notwithstanding. And Stack Overflow has forever had the best SEO. Google made that one interaction available to the next million programmers with the same
problem.

All of this what makes the role of AI generated answers rather paradoxical.

On the one hand we have low-cost peer-to-peer links, but on the other hand, LLMs
have established _even_ cheaper links between a programmer and
the accumulated output of the network. And that, too, is a very awkward thought
because ultimately, the accuumulated knowledge of an LLM is not, after all, a
network. So the question remains, what do we lose when we replace a network with
a single, albeit much stronger, node? How long do links last when they're not
between two nodes of a large, distributed network?

Every private interaction with an LLM is one interaction that does not become a
public question. And every question that is never asked is one fewer opportunity
for someone else to answer it, earn reputation, practise their craft, help a
stranger, or simply have a reason to return tomorrow. Our data suggests exactly
this kind of unwinding. As question volume fell, answerers returned less often.
The questions that remained received fewer answers and waited longer for them.
A weaker service gives future askers still less reason to come back. What had
been a virtuous cycle could run equally well in reverse.

This distinction also resolves a puzzle about the long tail. AI is spectacularly
good at dealing with long tails mechanically: it can ingest amounts of text that
no person could hope to read and retrieve obscure fragments of it on demand.
But there is another healthy sense in which a long tail exists. It is the consequence of
millions of people each knowing, noticing and contributing tiny things that no
central planner would ever have thought to collect.

Making the long tail easier to consume is clearly useful. Taken to its logical
extreme, the best possible interface would make the long tail disappear
altogether: no searching, no browsing, just the answer. And therein lies the
trap. If making the tail invisible also removes the reasons people have to keep
adding to it, we may eventually destroy the process that creates it in the first
place. We don't want to eat our own long tail, after all. The long tail is the
necessary evil. The cost of searching for a needle in a haystack is also the
cost of serendipity.

That doesn't, of course, mean that Stack Overflow was the best possible place to
create knowledge and knowhow. It already had trouble with that process. Long
before ChatGPT, newcomers were increasingly likely to have their first questions
rejected and increasingly unlikely to return. The mechanisms that kept the
archive clean also made participation expensive. That did not cause the collapse
after 2022, but it meant that when an extraordinarily attractive outside option
arrived, the community was not particularly good at replenishing itself.

This is where my original suspicion was wrong. Stack Overflow was indeed in
decline before ChatGPT. Good questions had been falling for years. Newcomer
retention had deteriorated. The community was heavily dependent on a remarkably
small core. All of that made the viral claim that ChatGPT had suddenly
"destroyed" Stack Overflow seem much too convenient.

But the data is unequivocal. The decay has reached the nucleus.

That still does not mean that AI has solved programming. Fred Brooks's 40-year-old
distinction survives remarkably well. Tools can remove enormous amounts of the
accidental difficulty of software—remembering syntax, finding an API,
translating an intention into code—without eliminating its essential
difficulty: deciding what the software ought to do, understanding the world it
inhabits, and managing the complexity of the thing itself. In other words, the disappearance of
90% of Stack Overflow's traffic does not mean that software engineering became
90% easier.

It means something more specific, and perhaps more consequential. Stack Overflow
built a commons in which the act of solving one person's problem also produced
knowledge for everybody else. ChatGPT made it possible to consume the fruits of
that commons without participating in it.

So, did ChatGPT kill Stack Overflow? It would seem so.

The harder question is who will bother to write the next answer down.

---

[^1]: We're being told that that's about to change: AI can write all the code
you want, and programming is a job ripe for automation. We'll see about that.
[^2]: Having someone looking over your shoulder as you write code is extremely
unnerving even to the most seasoned programmer.
[^3]: There are many not-so-modest views of how transformative genAI is—from
    simply making everything we know obsolete to curing cancer, solving
    climate change and ushering in an era of abundance.
[^4]: Based on the official data explorer.
[^5]: Specifically, questions here are scored by their net upvote tally (upvotes
    minus downvotes) and then filtered by whether they remained in the top
    quartile of all questions asked in the same year.
[^usertypes]: defined by the predominant activity over a user's lifetime on the
    platform.
[^10]: That one YouTube video.
