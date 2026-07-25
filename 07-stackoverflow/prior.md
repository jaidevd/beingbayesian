
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
while getting the good at the command line takes years, getting started is not
all that hard. What really exasperates me, however, are those who doggedly
avoid the command line in favour of GUIs, and _still_ end up fumbling
around, wasting time and ultimately making mistakes.

I recently encountered an intern doing something similarly exasperating. He'd
been asked to debug program. After repeated attempts, the variety of bugfixes
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
embarassing is my Stackoverflow profile. I've asked a grand total of five
questions; two of which have been deleted. One of the remaining three is
outright embarassing - the kind of question that today I would fire myself for
asking. The other two, while not as silly, are still the desperate attempts of
someone who doesn't know how to perform a good web search. And then there are my
answers. Far less embarassing, but still answers to precisely those questions
that a person like the past me would have asked. In fact, I was precisely
someone who deserved to have their job taken away by AI. Even today, there are
enough such people around in workplaces that it feels like AI is just around the
corner, ready to blindside the naive knowledge worker.

Many developers have very interesting Stackoverflow stories. A friend once told
me how during his internship he was tasked with a particularly difficult
problem, and no matter how far and wide he looked on Stackoverflow, the only
related questions he saw were from other interns before him who'd failed to fix
the problem, and the only answers he saw were from his boss: the very person who
gave him the problem in the first place.

![](https://imgs.xkcd.com/comics/wisdom_of_the_ancients.png)

It's an institution that's hallowed and controversial at the same time. For no
small number of programmers, their reputation on Stackoverflow has translated
into real professional reputation, to the point that reputation-farming on
Stackoverflow was even a valid strategy for career progress. On the other hand
people also have stories about how the platform made them feel unwelcome, to the
point of being positively toxic. I'm not proud to admit this, but it's not
entirely impossible that I myself might have played some part in shaming an
unsuspecting novice. But, all in all, Stackoverflow has been, for the better
part of the last 20 years, quite central to software engineering.


---

What's fascinating about a platform like Stackoverflow is it's nonlinear
dynamics. Even with my sparse set of questions and answers, I have a reputation
of 3,144. This means[^3] that I'm at the 99.68th percentile. Only _a third of a
percent of all Stackoverflow_ users have a higher reputation. But here's the
kicker: there are nearly a hundred thousand of them! The highest reputation ever
is at a million and half: three orders of magnitude higher from where I am.
Even if I were so inclined, scaling that peak is going to take me multiple lifetimes.

But, once we are no longer overwhelmed by the sheer magnitude of things, the
pattern here is surprisingly common: the Power Law distribution. In every
socioeconomic system, influence and
reputation are almost always highly concentrated in a vanishingly small fraction of the
population. In wealth and income distribution, this is exactly what we refer to
when we say that the rich keep getting richer.

It's not hard, then, for LLMs to destroy the astronomically long tail.

<!--- self note: two views of long tails: how you found them hard to deal with
yourself in the PlotCaptions project, but AI could have destroyed it, if you'd
let it. Has AI destroyed the long-tail of reputations (by users)? Worth checking
out. Would there be a credible pre- and post-ChatGPT artifact there?

But here we've got to be cautious: When we say that AI destroys the long tail,
do we mean that:

  * it makes mechanically and logistically addressing the long tail easier?
    We're referring here to the sheer volume of information that AI can gobble
    up[^^].
  * or does it render ineffective / obsolete the very processes, the underlying
    primal causes, that _create_ the long tail.


[^^]: Information getting gobbled up? Producing what? As per Cesar Hidalho,
    would this gobbling up create info or destroy it?

-->

---

[^1]: We're being told that that's about to change: AI can write all the code
you want, and programming is a job ripe for automation. We'll see about that.
[^2]: Having someone looking over your shoulder as you write code is extremely
unnerving even to the most seasoned programmer.
[^3]: Based on the official data explorer.
