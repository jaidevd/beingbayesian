The findings here are obtained by loosely imagining welfare interventions as
randomized controlled trials-"loosely" being the operative word. Actual RCTs are
expensive and take a very long time to conduct. The Household Consumption
Expenditure Survey (HCES), on the other hand, gives us observations for sample
households. No matter how we spin the data, it can't exactly mimic the
conditions of an RCT. The HCES contains nationally representative observations
of households, but participation in welfare programs is not randomly assigned.
The household characteristics certainly are not controlled, and the outcomes
(which are, in this case, expenditure on and consumption of various goods and
services) cannot be meaningfully linked to a trial intervention. As such, we
lose causality, and limit ourselves to infer only associations. It's true that
correlation isn't causation, but it's not nothing. A friend used to say that
throwing correlation away just because it's not causation is like throwing the
baby out with the bathwater.

So we end up with tenuous simulations of RCTs. We imagine welfare schemes as
interventions, with each scheme having a fixed eligibility criterion. Based on
this, we create a cohort of eligible households which we divide into "treatment"
and "control" groups. For example, if we consider PDS as the intervention, then
every household that has a ration card is eligible. Households that actually
_used_ the card to purchase subsidized goods end up in the treatment group.
Instead, if the intervention is midday meals, then the eligibility changes to
households that have children enrolled in public schools. Thankfully, much of
this information can be found readily in the HCES.

However, eligibility alone is not enough; households must also be comparable in
the socio-economic sense. Even without any intervention, consumption patterns
vary widely. Household size, number of children and elderly members, religion,
caste, and geography all influence what people buy. For example, a Dalit
household in Vidarbha is bound to eat very differently than one in coastal
Maharashtra, even if both are in the same state. So the eligible cohort needs to
be further filtered down to only include households that are similar along
observable socio-economic characteristics to each other, except for the
intervention itself. We use a method called propensity score matching, which
estimates the _likelihood_ of a household receiving an intervention based on
various attributes. Using the estimated propensity scores, we limit the analysis to households that have more than a 60% chance of being selected in a program (the top two quintiles of
the PSM scores), and then we divide them between those that received the
treatment and those that did not.

All numbers you see here are the differences in average expenditure between such
cohorts, and the comparisons are statistically significant at the 5% level. The
code and data needed to reproduce these results are available
[here](https://github.com/jaidevd/beingbayesian).
