# Bigger, Faster... Smarter?

The capacity of learning in an artificial neural network (on which most modern
AI models are based) is measured in _parameters_—a bunch of adjustable numbers,
like knobs and dials, which when carefully tuned, trains the network for a given
task. The more knobs, the more tunable the network becomes, and the better it
can learn complex patterns. It stands to reason that more parameters means a
better ability to learn[^1]. And when more parameters are coupled with higher
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
> move away from deep learning.

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

Even Yann LeCun, one of the champions of deep learning, doubts that scaling LLMs
alone will get us to human-level intelligence[^2]. But another pioneer of
scaling, and co-founder of OpenAI, Ilya Sutskever, appears to be religiously
committed to the idea. Hao wrote in an article in _The Atlantic_,

> Sutskever began to behave like a spiritual leader... His constant,
> enthusiastic refrain was "feel the AGI"... At OpenAI's 2022 holiday party,
> Sutskever led employees in a chant: "Feel the AGI! Feel the AGI!"

His religious zeal for scaling was clearly infectious. Dario Amodei, previously
VP of research at OpenAI and then founder of Anthropic said on Dwarkesh Patel's
podcast[^3],

> One of the first things Ilya Sutskever said to me was, "Look. The models just
> want to learn. You have to understand this. The models just want to learn. It
> was a bit like a Zen koan. I listened to this and I became enlightened.

![](images/twitter_sutskever.png)

Perhaps, this kind of religious fervour is necessary to drive a movement,
anything less would not do. But I wonder if it couldn't have been done without
jingoism and hyperbole. Sutskever is certainly capable of restraint. In a 2023
[interview with Dwarkesh Patel](https://www.youtube.com/watch?v=Yf1o0TQzry8),
when pushed to speculate on AGI timelines, Sutskever carefully, and correctly,
hesitates[^4]. When asked about how seriously he takes scaling laws, he
admits[^5] that there's a fundamental gap between the accuracy of models
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

[^1]: This is not without caveats. Models that are too large are prone to
"overfitting"; the learning task and the data they are given must both be
commensurate with their capacity. Otherwise they either simply memorize their
training data, or don't learn anything useful at all. Overly capable models with
poor training are a bit like awkward geniuses: like Sheldon Cooper's social
skills.
[^2]: "Yann LeCun... had a particular distaste for OpenAI and what he viewed as
its bludgeon approach to pure scaling." -- Karen Hao, _Empire of AI_, p. 159.
[^3]: Page no. 24
[^4]: Page in the book
[^5]: Page in the book
