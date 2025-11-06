> It is said that to explain is to explain away. This maxim is nowhere so well
> fulfilled as in the area of computer programming, especially in what is ealled
> heuristic programming and artifieiM intelligence. For in those realms machines
> are made to behave in wondrous ways, often suftieient to dazzle even the most
> experim~eed observer. But once a particular program is unmasked, once its inner
> workings are explained in language sufficiently plain to induce understanding,
> its magic crumbles away...

- Joseph Weizenbaum

![](https://obamawhitehouse.archives.gov/sites/default/files/imagecache/gallery_img_full/image/image_file/42.jpg?itok=bdBOhLvF)

Most of us would think that this picture is funny. We'd come to this realization
at a glance, in no more than a second. And if we were to carefully unravel our
chain of thought behind this reaction, we'd end up with something like this:

* We detect that there are people in the picture
* We see that there's someone standing on a weighing scale. We know, further,
  what weighing scales do.
* We notice that someone is pressing down on the scale, unbeknowst to the person
  standing on it.
* We know how scales work, and we know that most people are conscious of their
  weight, and so we infer that someone is playing a prank.
* We further realzie that the person playing a prank isn't just anyone - he's
  one of the most powerful men in the world. It's made funnier by our collective
  cultural belief that leaders are supposed to be dignified.

That, in short, is the sort of reasoning it takes to comprehend a picture.

Now, when I paste the image into ChatGPT (try it out!) and ask it why it's
funny, here's what it says:

> This picture is funny because it captures a playful moment: a man is standing
> on a scale, and another man (in a suit) is humorously stepping on it, likely
> to make the weight reading higher. The lighthearted teasing, unexpected in a
> formal setting with suits and officials around, makes the scene amusing.

While not as nuanced as the earlier explanation, this is still not bad at all.

I first heard the example above in a lecture by Justin Johnson from a computer
vision course in Stanford University, which in turn was borrowed from a blog
post by Andrej Karpathy - a noted AI researcher.

I've been training machines to see, read and write for 15 years now - since well
before it was cool. I've become jaded, and I suffer from what Steven Pinker
calls the "curse of knowledge". Being intimately familiar with the inner
mechanism of these systems, I'm usually unimpressed (why, really? because you
know that all they're doing is scaling - there's no _real_ innovation going on -
has this out). That's made me cynical. And I therefore become frightfully mad
when people think AI is going to solve all our problems.

---


The idea of thinking machines and anthropmorphized automatons in mythology and
fiction dates back to antiquity. Cultivating some form of intelligence in a
mechanical, automatic, controllable object has captured humanity's imagination
for as long as we can remember. This impulse persists across ages and cultures,
like the search for meaning or the urge to control and master. The pursuit of
artificial intelligence is in some ways a spiritual pursuit—an exploration of
what it means to be intelligent, to be human[^1]. A programmer who sees their
machines learn how to see, write and read for the first time feels like
Hephaestus creating Pandora. Algorithms become alchemy. It's only natural that
we love it.

In the last few decades, AI has become an umbrella term, referring to a broad set of
technologies and methods. But in it's current usage in the media, "AI" refers
almost exclusively to _generative_ AI - stuff that learns from patterns in
language, vision and speech to generate human-like content. Generative AI itself
is a specialized application of a paradigm known as artificial neural
networks—algorithms that use a collection of artificial neurons, which in turn
are inspired by biological neurons. The artificial neuron was first proposed 80
years ago—by neuroscientist Warren McCulloch and logician Walter Pitts. The
history of hype in AI is almost as old as the artificial neuron, as we shall
see.

A biological neuron, or a nerve cell, has dendrites, axons and a soma; which
respectively perform the functions of input stimuli, output stimuli and an
aggregation process on the inputs.


[^1]: Mark Rowlands on the endless pursuit to figure out what separates humans
    from animals.

---


The seeds of AI hype and misinformation started sprouting in popular discourse
long before Instagram was awash with AI slop and every other post on LinkedIn
preyed on AI FOMO. As we've seen before, there was nothing essentially new about
it, but this time, the hype virus found a new ecosystem to infect: social media.

In 2015, Tim Urban, the writer of the popular blog "Wait But Why", wrote a
two-part series on AI, titled ["The AI Revolution: The Road to
Superintelligence"](https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html).
Even if he wasn't the first AI booster[^3] and wouldn't be the last, few people
have been as influential as him in popularizing AI for a layperson. A fantastic
writer and explainer of complex topics, Urban did a great job of collating many
common AI fallacies in one place. What follows might read like a hit piece
against Urban, but it's really a case study. A critique of his posts serves as a
microcosm of much that is wrong with AI hype.

> It's an intimate mixture of rubbish and good ideas, and it's very hard to
> disentangle the two, because these are smart people; they're not stupid.

> —Douglas Hofstadter, [_American
Scientist_](https://web.archive.org/web/20140122012828/https://www.americanscientist.org/bookshelf/pub/douglas-r-hofstadter)

Nearly every bizarre claim about AI can be traced back to the so-called "Law of
Accelerating Returns", proposed by Ray Kurzweil. Kurzweil is a colorful figure
in the history of technology: a pioneer of optical character recognition, speech
synthesis and electronic keyboards, he has long since emerged as a prophet of
technology, complete with his share of acolytes and critics. He introduced the
Law of Accelerating Returns in his 1999 book _The Age of Spiritual Machines_.
Here's an excerpt from a 2001 essay by Kurzweil with the same title:

> ... the history of technology shows that technological change is
> exponential... So we won’t experience 100 years of progress in the 21st
> century — it will be more like 20,000 years of progress (at today’s rate). The
> “returns,” such as chip speed and cost-effectiveness, also increase
> exponentially. There’s even exponential growth in the rate of exponential
> growth. Within a few decades, machine intelligence will surpass human
> intelligence, leading to The Singularity — technological change so rapid and
> profound it represents a rupture in the fabric of human history.

If it sounds like unfalsifiable nonsense, that's because it is. It's not a "law"
of nature, but simply an absurd extrapolation of an observed pattern. Just like
the current AI hype can be traced back to this 'law', the law can in turn be
traced back to another non-law: Moore's Law.

Moore's Law is the observation that the number of transistors (electronic
switches) in an integrated circuit (like a microprocessor in our computers)
doubles every two years. This means that the number of arithmetic and logical
operations a chip can perform in a fixed time doubles every two years - without
growing in size.  Kurzweil's proposal is predicated on the idea (or at least the
bastardization of it) that things—economies, technologies, collective human
knowledge, etc—grow over time. And even if Moore's Law is the cornerstone of his
proposal, he expects everything to show "exponential growth"—something that
cannot be taken for granted. Even if Moore's Law were to continue to hold _ad
infinitum_ (it stopped being true years ago), the assumption that every
desirable component of technological change will continue to grow exponentially
is absurd. The economist Daniel Susskind writes,

> ... our apparent success created the impression that an expanding economy was
> the norm, with any slowdown to be regarded as an unfortunate but temporary
> exception. Today, that assuredness feels misplaced. Almost every country has
> slumped its way into the 21st century, though the timings differ... Most
> economies, battered by two decades of crises—including the dot-com bust, the
> 2007-8 financial crisis and the COVID-19 pandemic—are sluggish shadows of
> former selves. We increasingly realize we cannot take growth for granted.

But even if we grant Kurzweil his premise—that growth is preordained,
unstoppable—the deeper fallacy still remains: the conflation of all growth with
_exponential_ growth.

The adjective "exponential" has a precise mathematical meaning. When we say that
something grows exponentially, we mean that the rate at which it grows is
proportional to its current size. Compound interest is a classic example of
exponential growth. If your wealth grows at 10% today, a year later it would be
growing at 10% of your _then_ wealth—which itself will be higher because of the
_current_ growth of 10%. However, the figure of 10% is a fraction, which means
that while this growth is still exponential, it is relatively slow. In contrast,
if your wealth were to grow at 100% (i.e it doubles every year), the resulting
growth would be: massive, staggering, astronomical—pick an adjective. But that
doesn't mean that everything which grows massively, staggeringly, or
astronomically is exponential. Quite often, the correct adjective is simply
'more'. Every other chart and visual in Urban's post—like stick figures standing
on a time-series curve, seemingly oblivious to the walls next to them, and a GIF
of how fast an empty lake fills up if the water pouring in it doubles every
second—reinforces this idea of the exponential curve.

Even if we concede that something does grow exponentially in the true sense of
the word, we still need to ask whether such growth is _observed_ in specific
time-windows, or whether it is predestined. The exponential decay of a
radioactive element is inevitable. But the growth of an economy or that of human
population are not. They only look exponential if we hold our time-windows to
convenient periods. It is all too easy to confuse the observed effect of some
things with the primal cause of something else.

In a 2005 interview[^1], Gordon Moore himself, with humility and amusement, said
that the semiconductor industry "made it (Moore's Law) a self-fulfilling
prophecy", and that it was, on his part, "lucky extrapolation". But that did
nothing to temper Kurzweil's enthusiasm. Most of his predictions were predicated
almost exclusively on Moore's law—and only a few of them have come true. He has
repeatedly time-shifted and revised his predictions (which hasn't helped), but
never fully retracted them. At best, his predictions can be called inaccurate.
At worst, they are unfalsifiable.

And yet, in as late as 2015, Tim Urban stands squarely on Kurzweil's shoulders
to reiterate the same predictions. Urban's obsequiousness to Kurzweil's ideas
could not be more evident. He quotes Kurzweil more than any other source by far,
and appeals to his authority every step of the way. Nearly half of the footnotes
in the first part of his post are from Kurzweil's book: _The Singularity is
Near_[^2].

There's a sprawling introduction to Kurzweil's law, followed by justifications
of why artificial superintelligence is an inevitable outcome of it. It's
peppered with quotes like

> This isn't science fiction. It's what many scientists smarter and more
> knowledgeable than you or I firmly believe...

By the time Urban comes to talk about the Singularity, or an "intelligence
explosion", he begins by reminding the reader that

> ... every single thing I'm going to say is real—real science and real
> forecasts of the future from a large array of the most respected thinkers and
> scientists. Just keep remembering that.

What in the world are "real forecasts of the future"? Not once does Urban turn a
critical eye towards these ideas—which, even in 2015, would have been doable and
revealing. For instance, he calls Moore's Law a "historically reliable rule"
—something that ought to have been avoided. He takes cheaper and faster
computation for granted, which to him means that we will be able to "reverse
engineer the brain", and then reminds us that "if emulating the brain seems
hopeless, remember the power of exponential growth". This argument, that simply
scaling a computer makes it smarter, has some merit, as we will see in the
following section. But to suggest that scaling alone will make it as smart as
the human brain, and that in turn will
somehow bring forth the rapture, is reductive. It presupposes that the human
brain is nothing more than a giant, parallel computer which can only do
arithmetic and logic operations—and intelligence is the result of enough of
them.

After repeating the same few arguments over and over, with a lot more hubris
("we have a lot of advantages over evolution", and we can build a
superintelligence by trying "to do what evolution did, but this time for us"),
he climaxes with "An Intelligence Explosion—the ultimate example of the Law of
Accelerating Returns." If that is indeed true, then hopefully the explosion will
be as full of gas as the law itself.

In short,

* _if_ Moore's Law continues to hold long enough,
* _and if_ the Law of Accelerating Returns rides well enough on it,
* _and if_ highly scaled computers indeed mimic the human brain,
* _and if_ we actually reverse engineer the human brain,

_then_ we will have superintelligence on our hands.

All of this is supposed to be inevitable, and it will happen before we know it.

It's such an exceptional compounding of fallacies[^4] that I'm tempted to slip up
myself and call this nonsense "exponential". Nearly all of it is based on appeal
to authority and hasty generalization.

But credit where it is due, Tim Urban did write that a "growth spurt might be
brewing right now", and he was right. In 2017, researchers from Google
introduced the transformer architecture—the next big leap in machine learning.
It soon became the workhorse of the large-language-model (LLM) revolution of the
early 2020s.

Before transformers, language models were typically recurrent, meaning they
processed text one word (or token) at a time, each prediction depending on the
one before it. That worked, but it made it hard to handle long passages: the
farther back the context went, the harder it became for the model to remember
and compute efficiently. The transformer solved this bottleneck by replacing
recurrence with attention — a way for the model to look at all words in a
sequence at once and decide which ones matter most to predicting the next. This
made training faster, more parallel, and more scalable.

The implication was that researchers were now ready to test what they had
suspected for ages—the question of whether sheer _scale_ can produce
intelligence. Could we systematically scale training data, computing power and
sizes of models to see if perhaps intelligence emerges? In 2018, OpenAI
published their results from the first of such experiments. The resulting model
was called GPT—Generative Pretrained Transformer. It was this model that would
undergo iteration after iteration of scaling over the next few years. OpenAI's
series of GPT models, Anthropic's Claude, Google's Gemini models are all,
fundamentally, massively scaled transformers.

And that's how we arrived here. Dwarkesh Patel, the host of a popular podcast on
AI calls the period from 2019 to 2025 _the Scaling Era_. Now that we could, it
was time to finally put exponentialism to the test.

---

[^1]: [Excerpts from A Conversation with Gordon
Moore](https://web.archive.org/web/20080218225540/http://download.intel.com/museum/Moores_Law/Video-Transcripts/Excepts_A_Conversation_with_Gordon_Moore.pdf)
[^2]: Kurzweil later wrote another book, called _The Singularity is Nearer_.
Since the Singularity is perpetually just around the corner, it makes sense that
Kurzweil took a serious interest in immortality. At the time Urban wrote his
article, Kurzweil was taking [100 pills every
day](https://www.businessinsider.com/ray-kurzweils-immortality-diet-2015-4).
[^3]: That dubious honor goes, sadly, to Frank Rosenblatt himself.
[^4]: Princeton researchers Arvin Narayanan and Sayash Kapoor came to a similar
    conclusion in their book _AI Snake Oil_. In an entire chapter dedicated to
    such fallacies, they write, "...we've seen in the history of AI research, that once
    one aspect gets automated, other aspects that weren't recognized earlier
    tend to reveal themselves as bottlenecks." Every link in the chain of "ifs"
    above has its own bottlenecks.

---


In August 2025, in the Rajya Sabha, Aam Admi Party MP Raghav Chadha demanded
free access to generative AI tools for all Indians. Undeterred by the question
of who will pay for them, social media hailed Chadha's demand as revolutionary.
It was called "bold", "heroic", "a crucial step towards digital democracy" and a
way to wrest the AI revolution away from Silicon Valley. The irony of how any of
this will happen by purchasing subscriptions from companies already in Silicon
Valley is lost on LinkedIn's "Top Voices". Influencers who would otherwise balk
at affirmative action or public welfare schemes loved the idea of free AI
subscriptions. As much as Chadha's own party has been criticised for appeasement
and "freebies", his proposal on AI subscriptions was unanimously applauded. 

Notably, an earlier speech of Chadha from March 2025, one in which he highlights
the need for infrastructure and funding needed for indigenous AI research, went
relatively unnoticed. In India, where fewer than 10% of households own a laptop
or a computer and internet usage is concentrated among younger, urban, educated and
wealthy Indians, the economic utility of free ChatGPT or Gemini subscriptions is
dubious.

It is not only this kind of collective, misty-eyed delusion that obfuscates the
promise of AI. Even the most earnest estimates of AI's economic impact are
dubious. OpenAI's own charter defines AGI as "highly autonomous systems that
outperform humans at most economically valuable work"; but we don't have
consensus, even between aligned parties, on what constitutes economically
valuable work or outperforming humans. For instance, Hinton famously said
in 2016 that we should stop training radiologists because it was "completely
obvious" that deep learning would be able to outperform them in a decade. If that had
happened, it would have been a good example of both AI outperforming humans as
well as creating economic value. Today, however, the field of radiology is
thriving; in no small part because they have managed to integrate AI tools.
Hinton has acknowledged his error. But many in the community who've made similar
erroneous predictions show barely a soft backpedal—insisting instead that AI
was always meant to be a companion. This pattern shows up distressingly
often—claim that AI will replace humans at something or the other, and when it
turns out that there's no real _replacement_, insist that it was never meant in
that sense.

At the root of this confusion is the fact that terms like AI, AGI,
autonomous systems, superintelligence, etc. are all ill-defined. They all refer
to a very large set of technologies and computing paradigms that are loosely
similar to each other. Asking questions about the economic impact of AI is like
asking questions about the impact of computers or the internet—they certainly
start with a bang, but take decades to diffuse through the economy and show
tangible impact. Deep down, we understand this, but the FOMO around AI makes
us slip up. Take, for instance, Andrej Karpathy's response when asked about how
best to measure AI progress—he said that he was "almost tempted to reject the
question entirely" because it was so ill-posed. He admits that there will always
be jobs that are "amenable to automation sooner or later", but that there's no
interpretation of "AI" or "work" that leads us to a clear and significant
economic impact.

To his credit, Karpathy has refined his outlook to adjust to reality. Only three
years ago, he was having a _very_ different conversation with Lex Fridman. He
said he was bullish on our ability to build AGIs. Three years later he admits
(to Dwarkesh Patel) that he gets triggered by the noise about AI on social
media, and that AI agents are slop. At the end of the Fridman interview, he
predicts (correctly) that the cost of content creation will fall, and excitedly
muses what would happen when we can generate art on demand, and when there's
infinite of it. Today we have arrived at Studio Ghibli-style image generation.
All it has done is generate some short-lived amusement, and a whole lot of
long-term consternation. On-demand video generators show us fake videos of house
cats chasing lions away and stuff that need not have been faked at all, like
journalists polishing politicians' boots.

_Slop._

---
https://youtu.be/ibQ2nmeP-7A?t=720
https://youtu.be/2HMPRXstSvQ


61
87
94
111
112
131
