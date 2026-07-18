### Page 69
While it feels obvious today that we want to freely share the things we make, the early success of open source captivated scholars and economists because it defied everything we thought we knew about how and why people create. Once companies started using open source for commercial purposes, and people realized that these hobby projects were able to compete with the software made by paid employees, scholars had to come up with a new framework to explain this behavior.

### Page 69
Previously, our understanding of how and why people make things was modeled after Ronald Coase's theory of the firm, which proposes that firms — that is, companies, organizations, and other institutions with centralized resources — naturally emerge as a way to reduce transaction costs in the market. Coase would have told us that only companies make software, because from a coordination standpoint, managing the resources required to pull off such a feat would be most efficiently handled within the same organization.

> **Self-note (p. 69):** What did Hidalgo say about this?

### Page 71
Through her research, Ostrom identified eight design principles that contribute to a well-managed, successful commons: (1) membership boundaries are clearly defined; (2) the rules that govern the commons should match the actual condition; (3) those who are affected by the rules can participate in modifying them; (4) those who monitor the rules are either community members or are accountable to the community rather than outsiders; (5) those who violate the rules are subject to graduated sanctions, which vary depending on the seriousness and the context of the offense; (6) conflicts should be resolved within the community using low-cost methods; (7) external authorities recognize the right of community members to devise their own institutions; (8) if the commons is a part of a larger system, its governing rules are organized into multiple nested layers of authority.

> **Self-note (p. 71):** What do all of these mean for Stack Overflow?

### Page 75
The modular, granular approach to software is embodied by the Unix philosophy, originating from the developers of the Unix operating system, which heavily influenced the design of open source software. As Doug McIlroy, one of its developers, counsels: write programs that do one thing and do it well; write programs to work together. Finally, Benkler suggests that low coordination costs are necessary to produce in a commons. In open source, coordination costs include both quality control over the modules, such as reviewing code, and integrating the contributions into the finished product, such as merging pull requests. Coordination work is expensive because it's not intrinsically motivated. For example, developers tend to be more excited about writing code than reviewing someone else's contribution. And as anyone who's tried to delegate work has probably noticed, it's usually faster to do things yourself than to train someone else to do it. A maintainer's biggest coordination costs come from reviewing and merging new contributions, so there's an incentive to keep these costs low. When the cost of coordination outpaces the benefits, the commons breaks down as a useful production model.

> **Self-note (p. 75):** Hidalgo on the cost of links?

### Page 75
Although the commons might not be as profitable as the firm, it is also more resilient, because the currency of its transactions is the desire to participate rather than money.

> **Self-note (p. 75):** What has AI done to this desire to participate?

### Page 79
> **Self-note (p. 79):** Platforms broke the commons. What does Cory Doctorow say about this?

### Page 97
Active contributors, also called regular contributors or long-term contributors, are considered members of the project based on their reputation or the consistency of their contributions. This is what we typically imagine when we think of open source contributors: a community of developers in which members are invested in one another and the project.

### Page 102
The ratio of casual to active contributors varies greatly between projects, depending on the size of their contributor community and how these terms are defined. One study suggests that casual contributors make up three-quarters of all contributions. Pandas, a Python library for data analysis, lists over 1,400 contributors, but just four developers contributed nearly half of all commits in 2018.

> **Self-note (p. 102):** Projects on GitHub — are they the same as tags on Stack Overflow? Can we treat them as such?

### Page 124
To quote Norbert Wiener, the mathematician who pioneered the field of cybernetics: information and entropy are not conserved, and are equally unsuited to being commodities.

> **Self-note (p. 124):** Are tokens commodities, then?

### Page 130
Eric S. Raymond once coined the aphorism "given enough eyeballs, all bugs are shallow." His point is that open source software presents an advantage over closed source software because if more people can inspect the code, it will increase the chance that more bugs will be discovered. The implication is that support can be handled in a fully decentralized manner that'll distribute its cost among the users. But as Fred Brooks wryly notes in his classic engineering book, *The Mythical Man-Month*, first published two decades before Raymond made his claim, although more users find more bugs, this results in a type of support cost that grows and is strongly affected by the number of users. As more people use open source software, more questions will be asked and more bugs will be found, but someone still needs to review, manage, and process these reports.

### Page 180
In open source, maintainers frequently push user support questions onto forums like Stack Overflow or group chats like Discord and Slack, where users can help answer one another's questions. In 2018, I analyzed a set of top 100 open source projects by issue volume and found that 89% were using something besides GitHub issues to manage their support needs, listing an average of two additional channels. The most popular channels were dedicated forums at 41% and Stack Overflow at 38%, followed by IRC (22%), GitHub (20%), and mailing lists (18%). These support channels are often driven by users who, like community moderators, derive satisfaction — and sometimes reputational benefits — from helping others. They tend to operate like satellites away from the GitHub repository where core developers congregate, but they still reduce the amount of support that maintainers have to do themselves. When implementing both user-to-user and automated systems, there will always be some coordination work involved to set up and manage these systems. Moderation needs can be partly resolved by algorithms and self-motivated users, but they will always require some degree of human involvement, if only to review appeals and arbitration. However, the cost of implementing and managing these systems is often far less than the cost to maintainers of doing it all themselves.

### Page 202
Hacktoberfest is an initiative that is sponsored by cloud infrastructure provider DigitalOcean and developer community DEV (GitHub was a sponsor in previous years). During the month of October, anyone who makes five pull requests to an open source project is eligible for a free T-shirt. This is a wonderful way to encourage newcomers to try their hand at making their first contribution, but it doesn't help to support the maintenance of open source projects, because casual contributors are already in abundance — adding an extrinsic reward only encourages people to make spammy, low-quality contributions to claim it. If you don't think this causes harm, trust me — it's incredible what developers will do for a free T-shirt.
