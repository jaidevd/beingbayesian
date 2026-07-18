# "Code Talkers" by Robert DeLine
### from *Making Software*, ed. Oram & Wilson

### Page 298
In the first study, from 2006, we conducted a survey of 157 randomly chosen programmers and follow-up interviews with 11 of them, asking them about their daily work activities and, in particular, what they found difficult. Their responses about the time they spent on various work activities were consistent with the findings of Perry et al. The average percentage of time spent on communication was higher than for any other activity. The survey also asked respondents to estimate the percentage of time they spent using various communication media, and to rate how effective they thought each medium was. The results are shown in Figure 16-1. These results are also in line with Perry et al., in that respondents spent the most of their time in unplanned face-to-face meetings; they also rated this as the most effective type of communication.

### Page 300
This story exemplifies points that we have heard repeatedly in the interviews. When a programmer gets stuck on an issue he doesn't understand, he does his due diligence before turning to a colleague for help — that is, he spends time learning about the code and its execution in order to ask educated questions. After the interviews, we conducted a follow-up survey of 187 programmers to get more details about what we learned during the interviews. From this, we learned that during this due diligence phase, on average, respondents spent 42% of their time examining the source code, 20% using the debugger, 16% examining check-in comments or version history, 9% examining test results, 8% using debug or print statements, and 5% using other means.

The search for rationale. What do we mean by the term "rationale"? In the follow-up survey, we asked what aspect of rationale is the most difficult. Out of the 187 respondents, 82% agreed that it takes a lot of effort to understand why the code is implemented the way it is; 73%, whether the code was written as a temporary workaround; 69%, how the code works; and 62%, what the code is trying to accomplish. In short, rationale is the backstory behind decisions — sometimes about decisions that were made, and sometimes about alternatives that were rejected.

### Page 301
**What Questions Do Programmers Ask?**

To understand the questions that programmers have as they do their daily work, we ran a second study at Microsoft [Ko et al. 2007]. We used an observational protocol very similar to the one that Perry et al. used in their study. We observed 17 programmers in their offices as they did their typical work, for roughly 90 minutes apiece. Like Perry et al., we asked the programmers to treat us like students trying to learn the job and would ask them questions when we couldn't tell what they were doing.

We also used what psychologists and social scientists call a *think-aloud protocol*. That is, we asked the programmers to chatter continually at us, telling us every thought that occurred to them and narrating every action they were taking. Here's a made-up example to illustrate what this sounds like:

> So, I'm looking for the code that opens the database, so I hit Ctrl-F to bring up the search box. I'm typing in "open". Damn, it didn't find anything. Let me try "database" instead. OK, here's the code I was looking for. It was called "access database", not "open" — that's why I didn't find anything before.

Although this kind of chatter may seem awkward or even annoying, participants get used to it very quickly. Without the think-aloud protocol, it would be impossible to understand the programmer's mental state. In particular, we would never have known most of the questions that our participants were wondering about, if they didn't say them aloud.

### Page 302
As our participants chattered away, we used a small digital clock and notepad to create a minute-by-minute transcript of everything they said and did. Whenever they got up to ask a colleague a question, we followed them and transcribed the conversations. After we recorded this data, we analyzed the transcripts and created a catalogue of all the information needs we witnessed, shown in Table 16-1.

**Table 16-1. Programmers' observed information needs, sorted by frequency**

| Information type | Average duration (minutes) | Maximum duration (minutes) |
|---|---:|---:|
| What have my coworkers been doing? | 1 | 11 |
| What code caused this program state? | 2 | 21 |
| In what situations does this failure occur? | 2 | 49 |
| What's the program supposed to do? | 1 | 21 |
| How have resources I depend on changed? | 1 | 9 |
| What code could have caused this behavior? | 2 | 17 |
| How do I use this data structure or function? | 1 | 14 |
| Why was this code implemented this way? | 2 | 21 |
| Is this problem worth fixing? | 2 | 6 |
| What are the implications of this change? | 2 | 9 |
| What is the purpose of this code? | 1 | 5 |
| What's statically related to this code? | 1 | 7 |
| Is this a legitimate problem? | 1 | 2 |
| Did I follow my team's conventions? | 7 | 25 |
| What does the failure look like? | 0 | 2 |
| Which changes are part of this submission? | 2 | 3 |
| How can I coordinate this with other code? | 1 | 4 |
| How difficult will this problem be to fix? | 2 | 4 |
| What can be used to implement this behavior? | 2 | 2 |
| What information was relevant to my task? | 1 | 1 |

*Frequency-and-outcome legend: ■ Acquired · □ Deferred · ☒ Gave up · — Beyond observation*

The information needs in the table are generalized forms of the particular questions we heard the participants ask. Alongside each information need, we show two pieces of information. First, the "duration" column shows the average and maximum number of minutes we saw programmers searching for answers to that information need. Second, the "frequency and outcomes" column has a symbol for every instance of the information need that we saw: a black box for successfully finding the answer; a white box for deferring the search to some later time; a box with an X for giving up on the search; and a dash for unknown outcomes because the observation session ended before the question was answered.

Where did programmers look for answers? Table 16-2 shows the sources of information consulted by the programmers we observed. Consistent with the previous studies, coworkers are consulted more often than any other source of information. The other sources, in order from most consulted to least consulted, were:

1. Various team-specific or company-specific tools
2. The programmer's own intuition, logical inferences, or memory (*brain*)
3. The bug database (*bugs*)
4. The debugger (*dbug*)
5. The source code, its comments, or its history (*code*)
6. Documents other than specifications (*docs*)
7. Email
8. Specification documents (*specs*)
9. The *logfiles* from program executions
10. Instant messages (*im*)

In addition to looking at the frequency of questions, we can also look at the most frustrating information needs — namely, those that had the longest search times and that were unsatisfied (deferred or given up) the most often. Based on these criteria, here are the seven most frustrating information needs:

1. What code caused this program state? (61% unsatisfied, max 21 minutes)
2. Why was the code implemented this way? (44%, 21 minutes)
3. In what situations does this failure occur? (41%, 49 minutes)
4. What code could have caused this behavior? (36%, 17 minutes)
5. How have the resources I depend on changed? (24%, 9 minutes)
6. What is the program supposed to do? (15%, 21 minutes)
7. What have my coworkers been doing? (14%, 11 minutes)

For all seven, the observed programmers turned to colleagues for answers, but also turned to other sources as well, often as part of their "due diligence."

So in addition to knowing that developers frequently talk to each other to ask each other questions, we also know which questions come up the most often and which ones are the most difficult to answer.
