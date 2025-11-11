# Introduction

> It is the internet remixed... it is language atomized by tokens and vectors. A
> million-layered neural network sandwich that is held together by calculus,
> linear algebra, and probability—also known as wild hope.

[Compasswallah](https://youtu.be/99tU_hkw9hk)


> It is said that to explain is to explain away. This maxim is nowhere so well
> fulfilled as in the area of computer programming, especially in what is ealled
> heuristic programming and artifieiM intelligence. For in those realms machines
> are made to behave in wondrous ways, often suftieient to dazzle even the most
> experim~eed observer. But once a particular program is unmasked, once its inner
> workings are explained in language sufficiently plain to induce understanding,
> its magic crumbles away...

- Joseph Weizenbaum

I've been training machines to see, read and write for 15 years now - since well
before it was cool. I've become jaded, and I suffer from what Steven Pinker
calls the "curse of knowledge". Being intimately familiar with the inner
mechanism of these systems, I'm usually unimpressed (why, really? because you
know that all they're doing is scaling - there's no _real_ innovation going on -
has this out). That's made me cynical. And I therefore become frightfully mad
when people think AI is going to solve all our problems.

---

# The History of AI Hype

The idea of thinking machines and anthropmorphized automatons in mythology and
fiction dates back to antiquity. Cultivating some form of intelligence in a
mechanical, automatic, controllable object has captured humanity's imagination
for as long as we can remember. This impulse persists across ages and cultures,
like the search for meaning or the urge to control and master. The pursuit of
artificial intelligence is in some ways a spiritual pursuit—an exploration of
what it means to be intelligent, to be human. The philosopher Mark Rowlands
argues that the only thing that makes humans humans is the desire to separate
ourselves from other animals. We haven't been particularly successful in this
pursuit. Over the years, we realized that language, tool use, rationality are
all displayed by various other animals. So then we thought we're unique in our
ability to self-reflect. But primates, elephants and—to our disappointment—even
pigeons can identify themselves and know their place in the world[^1]. All
anthorpomorphism, thus, is a matter of _degrees_ of similarity to human
behaviour. There isn't a qualitative threshold beyond which a being is deemed
human. So when it comes to human-level intelligence, emotion or behaviour,
researchers probably should just call it a day and move on to better-defined
problems.


Nevertheless, a programmer who sees their
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
aggregation process on the inputs. McCulloch & Pitts recognized that this
simplified interpretation of a biological function was still powerful enough
to be _programmed_ into a
computer. A machine could be instructed to accept a bunch of numerical inputs,
aggregate them (like summing or averaging them), and if the aggregate value was
higher than a fixed threshold, the neuron "fires", relaying ahead an impulse.
This idea, of interpreting a neuron as a miniature calculator, could be
generalized further by arranging multiple neurons in a network—thus, _neural
networks_. But this model was limited to only being programmed with explicit
instructions. McCulloch & Pitts hadn't suggested how it could be _trained_. That
flash of genius came in 1957 from the psychologist Frank Rosenblatt. He called
his invention the _perceptron_ - an artificial neuron that could be programmed
to train itself.

The perceptron was... _beautiful_—there's no other word for it. It was almost
magical. Few algorithms are as elegant as the one used to train the perceptron.
It is a binary classification algorithm—inputs to it are
categorized into one of two classes. The algorithm itself can be written in no
more than three sentences. And best of all, it came with a _guarantee_: if the
categories presented to it while training can be separated by drawing a straight
line (or plane) between then, then the perceptron _will necessarily_ find that
separating line. The implications are far reaching: if any two statistical patterns
are presented such that they have a straight gap between then, the perceptron
_will_, eventually, but _automatically_, find that gap. When I was a student I was
[obsessed](https://jaidevd.com/posts/perceptron-convergence/) with how something
so simple and straightforward, something that could be programmed with only a
few lines of code, could weild such power[^2].

In a
public demonstration in 1958, Rosenblatt showed how the perceptron learnt to
distinguish between paper sheets marked on the right versus those marked on the
left. In a later experiment, it could tell circles apart from squares. The media
lapped it up, Rosenblatt would say in hindsight, "with all of the exuberance and
sense of discretion of a pack of happy bloodhounds". The New
York time carried a piece titled "Electronic Brain Teaches Itself". The New
Yorker magazine went further and claimed that the perceptron is capable of
original thought. Rosenblatt himself thought that his invention would one day be
capable of conscious thought, but would later admit a certain "lack of
mathematical rigor in preliminary reports."[^3]

Unfortunately, this was also the first instance of overpromising and
under-delivering in the history of AI. As powerful as the perceptron's guarantee
of separating patterns was, it did not take long for people to realize that
there are enough classification problems that cannot possibly be expressed as
separable patterns. Indeed, _most_ interesting problems in machine learning were
of the sort where it's not possible to separate patterns by drawing straight
lines between them. In 1969, Marvin Minsky and Seymour Papert highlighted some
of the most apparent limitations of the perceptron. They were aware that these
gaps could be plugged, but it was the criticism that went viral. Their often
mis-cited work so definitively punctured the AI bubble that interest and funding
dried up, and the field plunged into the _AI Winter_. The next few decades were
peppered with incremental, standalone innovations. In 1986, Geoffrey Hinton with his
collaborators Rumelhart and Williams figured out how to train neural networks
with a process known as error backpropagation. A decade later, Yann LeCun
created "convolutional" neural networks - an architectures that allowed neural
networks to "see".

The early 2010s saw a series of fortuitous events for AI research. An evolved
CNN architecture named AlexNet was developed, which broke records in visual
recognition. Nvidia published a software platform named CUDA, which allowed
programmers to use GPUs for not just graphics, but general purpose computing.
GPUs are massively parallel computers. As such, they were exceptionally well
suited to the task of training neural networks (neurons can process their inputs
independent of what most other neurons are doing at the same time). Coursera was
founded in 2012 - and one of their two introductory courses was on machine
learning. This meant that anybody could study machine learning, practically for free.
Around this time, in the background, the popularity of open source software
was growing, resulting in various open-source deep learning frameworks that are
thriving to this day. For me, too, the stars had aligned. I was in
the final year of engineering school in 2011, and I took a course in artificial
neural networks. The most expensive lab on campus (to which I had unfettered
access), contained six Nvidia workstations armed with top-of-the-line GPUs which
a professor had managed to procure as part of a research grant. Although nobody
could have predicted what was on the horizon, the early 2010s were a great time
to be studying deep learning (it wasn't called AI yet).

Since then, the field has seen an insane growth. As an undergraduate, I would
well have believed that AGI was our manifest destiny. Today, the discourse
around AGI shocks me.

# The Superintelligence Prophecy

The seeds of AI hype and misinformation started sprouting in popular discourse
long before Instagram was awash with AI slop and every other post on LinkedIn
preyed on AI FOMO. As we've seen before, there was nothing essentially new about
it, but this time, the hype virus found a new ecosystem to infect: social media.

In 2015, Tim Urban, the writer of the popular blog "Wait But Why", wrote a
two-part series on AI, titled ["The AI Revolution: The Road to
Superintelligence"](https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html).
Even if he wasn't the first AI booster[^4] and wouldn't be the last, few people
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
> former selves. We increasingly realize we cannot take growth for granted.[^5]

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

In a 2005 interview[^6], Gordon Moore himself, with humility and amusement, said
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
Near_[^7].

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

It's such an exceptional compounding of fallacies that I'm tempted to slip up
myself and call this nonsense "exponential". Nearly all of it is based on appeal
to authority and hasty generalization. Princeton researchers Arvin Narayanan and
Sayash Kapoor came to a similar conclusion in their book _AI Snake Oil_. In an
entire chapter dedicated to such fallacies, they write, "...we've seen in the
history of AI research, that once one aspect gets automated, other aspects that
weren't recognized earlier tend to reveal themselves as bottlenecks." Every link
in the chain of "ifs" above has its own bottlenecks[^8].

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

# Bigger, Faster... Smarter?

The capacity of learning in an artificial neural network (on which most modern
AI models are based) is measured in _parameters_—a bunch of adjustable numbers,
like knobs and dials, which when carefully tuned, trains the network for a given
task. The more knobs, the more tunable the network becomes, and the better it
can learn complex patterns. It stands to reason that more parameters means a
better ability to learn[^9]. And when more parameters are coupled with higher
quality data and faster compute... Hallelujah!

GPT-1 had 117 million parameters. Its 10x scaled successor, GPT-2, could
actually generate coherent text! GPT-3, with 175 billion parameters, was made
receptive to prompting and called 'InstructGPT'; which in turn formed the basis
of ChatGPT. GPT-4 was rumoured to have nearly 1.8 trillion parameters.
Between 2018 and 2024, exponentialism played out impressively. In late 2022, AI
researcher and educator Andrej Karpathy said on the Lex Fridman podcast that the
zeitgeist was "don't touch the transformer, touch everything else; scale up
data; scale up evaluations". Even experts were fascinated by scaling leading
to emergent capabilities. Many felt that there could, after all, be a magical
number of parameters on the horizon, which would unlock true intelligence. The
journalist Karen Hao has dedicated an entire chapter in her book, _Empire of
AI_, to scaling. She writes,

> The scaling doctrine had become so ingrained that some are even beginning to
> view it as something of a natural phenomenon. Scaling compute is _the_ way,
> not just _a_ way, to reach more advanced AI capabilities. ...the neglected
> paths of improving the neural network itself or even the quality of its
> training data can significantly reduce the amount of expensive compute needed
> to reach the same performance. That's not even considering the approaches that
> move away from deep learning.[^10]

Drawing a parallel to Moore's Law, she further writes,

> OpenAI's Law, or what the company would later replace with an even more
> fevered pursuit of so-called scaling laws, is exactly the same (as Moore's
> Law). It is not a natural phenomenon. It's a self-fulfilling prophecy.

Even if this outright equivalence to Moore's Law, and Kurzweil's Law is
accepted, there's a more fundamental idea which needs to be questioned. Is deep
learning—as pioneered by McCulloch & Pitts, improved by Rosenblatt, and
generalized by Hinton—a good approximation of the human brain? To what extent
can hyperconnected, massive networks of artificial neurons be grown to match
human intelligence? They certainly lend themselves to scaling, but how far can
we stretch this approximation?

Even Yann LeCun, one of the champions of deep learning, [doubts](https://youtu.be/4__gg83s_Do) that scaling LLMs
alone will get us to human-level intelligence[^11]. But another pioneer of
scaling, and co-founder of OpenAI, Ilya Sutskever, appears to be religiously
committed to the idea. Hao wrote in an article in _The Atlantic_,

> Sutskever began to behave like a spiritual leader... His constant,
> enthusiastic refrain was "feel the AGI"... At OpenAI's 2022 holiday party,
> Sutskever led employees in a chant: "Feel the AGI! Feel the AGI!"

His religious zeal for scaling was clearly infectious. Dario Amodei, previously
VP of research at OpenAI and then founder of Anthropic said on Dwarkesh Patel's
podcast[^12],

> One of the first things Ilya Sutskever said to me was, "Look. The models just
> want to learn. You have to understand this. The models just want to learn. It
> was a bit like a Zen koan. I listened to this and I became enlightened.

![](images/twitter_sutskever.png)

Perhaps, this kind of religious fervour is necessary to drive a movement,
anything less would not do. But I wonder if it couldn't have been done without
jingoism and hyperbole. Sutskever is certainly capable of restraint. In a 2023
[interview with Dwarkesh Patel](https://www.youtube.com/watch?v=Yf1o0TQzry8),
when pushed to speculate on AGI timelines, Sutskever carefully, and correctly,
hesitates[^13]. When asked about how seriously he takes scaling laws, he
admits[^14] that there's a fundamental gap between the accuracy of models
predicated on scaling laws and the emergence of actual reasoning capability.

And as of today, the music seems to have stopped.

In November 2024, Sutskever reportedly [told
Reuters](https://www.reuters.com/technology/artificial-intelligence/openai-rivals-seek-new-path-smarter-ai-current-methods-hit-limitations-2024-11-11/)
that results from the scaling laws have plateaued. It was around the same time
that Satya Nadella proposed the emergence of a _new_ scaling law, based on
letting models take longer to think before responding. Going a step further, in
March 2025, Jensen Huang suggested that the entire world got the scaling laws
wrong, and the amount of compute needed now was "easily a hundred times more
than we thought we needed this time last year."

If you're tempted to believe either of them, remember only Upton Sinclair's
famous line,

> It is difficult to get a man to understand something when his salary depends
> on his not understanding it.

Already in the fall of 2025, GPT-5 released to lukewarm reviews. What people
were led to believe would be a vindication of scaling turned out to be not
significantly better than it's predecessor. Meta delayed the release of their AI
model named "Behemoth" or "Llama 4", citing scaling limitations. xAI's grok
series of models, too, saw delayed releases and disappointing results.

Nadella and Huang seem just to be putting a positive spin on all of it - not to
mention the multiple times Sam Altman has turned on a dime after the release of
GPT-5.

In short, it's worth asking whether LLMs today are as good as they're going to
be for a long, long time.

---


In August 2025, in the Rajya Sabha, Aam Admi Party MP Raghav Chadha [demanded
free access to generative AI tools](https://www.youtube.com/watch?v=rWeSb7-NBD0) for all Indians. Undeterred by the question
of who will pay for them, social media hailed Chadha's demand as revolutionary.
It was called "bold", "heroic", "a crucial step towards digital democracy" and a
way to wrest the AI revolution away from Silicon Valley. The irony of how any of
this will happen by purchasing subscriptions from companies already in Silicon
Valley is lost on LinkedIn's "Top Voices". Influencers who would otherwise balk
at affirmative action or public welfare schemes loved the idea of free AI
subscriptions. As much as Chadha's own party has been criticised for appeasement
and "freebies", his proposal on AI subscriptions was unanimously applauded. 

Notably, an [earlier speech](https://www.youtube.com/watch?v=awqpznqqV4Y) of Chadha from March 2025, one in which he highlights
the need for infrastructure and funding needed for indigenous AI research, went
relatively unnoticed. In India, where fewer than 10% of households own a laptop
or a computer[^15] and internet usage is concentrated among younger, urban, educated and
wealthy Indians[^16], the economic utility of free ChatGPT or Gemini subscriptions is
dubious.

It is not only this kind of collective, misty-eyed delusion that obfuscates the
promise of AI. Even the most earnest estimates of AI's economic impact are
dubious. OpenAI's own charter defines AGI as "highly autonomous systems that
outperform humans at most economically valuable work"; but we don't have
consensus, even between aligned parties, on what constitutes economically
valuable work or outperforming humans. For instance, Hinton famously said
in 2016 that we should [stop training radiologists](https://youtu.be/2HMPRXstSvQ) because it was "completely

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
news anchors polishing politicians' boots.

_Slop._

---
https://youtu.be/ibQ2nmeP-7A?t=720


61
87
94
111
112
131



---  <!--Footnotes-->

[^1]: Mark Rowlands, *The Happiness of Dogs: Why the Unexamined Life is Most
    Worth Living* (Granta, 2024), p. 78
[^2]: It would take me a while to learn that elegance and simplicity are
    hallmarks of mathematical wisdom. George Polya often said, "_Simplex sigillum
    veri_—simplicity is the seal of the truth."
[^3]: Brian Christian, *The Alignment Problem* (Atlantic Books, 2020), p 31
[^4]: That dubious honour goes, sadly, to Frank Rosenblatt himself.
[^5]: Daniel Susskind, *Growth: A Reckoning* (Allen Lane, 2024), p. xiv
[^6]: [Excerpts from A Conversation with Gordon
Moore](https://web.archive.org/web/20080218225540/http://download.intel.com/museum/Moores_Law/Video-Transcripts/Excepts_A_Conversation_with_Gordon_Moore.pdf)
[^7]: Kurzweil later wrote another book, called _The Singularity is Nearer_.
Since the Singularity is perpetually just around the corner, it makes sense that
Kurzweil took a serious interest in immortality. At the time Urban wrote his
article, Kurzweil was taking [100 pills every
day](https://www.businessinsider.com/ray-kurzweils-immortality-diet-2015-4).
[^8]: Arvind Narayanan & Sayash Kapoor, *AI Snake Oil* (Princeton University
    Press, 2024), p. 152
[^9]: This is not without caveats. Models that are too large are prone to
"overfitting"; the learning task and the data they are given must both be
commensurate with their capacity. Otherwise they either simply memorize their
training data, or don't learn anything useful at all. Overly capable models with
poor training are a bit like awkward geniuses: like Sheldon Cooper's social
skills.
[^10]: Karen Hao, *Empire of AI* (Allen Lane, 2025), p. 115
[^11]:"Yann LeCun... had a particular distaste for OpenAI and what he viewed as
its bludgeon approach to pure scaling." _Ibid._, p. 159. 
[^12]: Dwarkesh Patel & Gavin Leech, *The Scaling Era: An Oral History of AI,
    2019-2025* (Stripe Press, 2025), p. 24
[^13]: _Ibid._, p. 168
[^14]: _Ibid._, p. 26
[^15]: _Computer ownership and usage_ by Abhishek Waghmare, Data For India (July 2025): https://www.dataforindia.com/computers/
[^16]: _Access to phones and the internet_ by Abhishek Waghmare, Data For India (February 2024): https://www.dataforindia.com/comm-tech/
