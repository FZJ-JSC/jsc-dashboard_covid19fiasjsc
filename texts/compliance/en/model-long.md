#### **The question**
First attempts to slow down the spread of a novel infectious disease are based on the introduction of measures aimed at reducing contacts within the population. The effectiveness of these measures is determined, among other factors, by the level of compliance in the population, that is how many people actually adhere to the regulations. The question arises as to whether **it is more effective to introduce very strict measures**, which are likely to be **followed by only a small part of the population**, **or to impose moderate measures, which are likely to be followed by a larger part of the population**. CoSiMo-Webtool users can answer this question with the simulation tool provided here. 

---

#### **The model**
The underlying mathematical model is related to the spread of COVID-19 among the German population. The simulated time “pre-intervention” reproduces a period of mild control measures adhered to by the whole population, resulting in a moderate increase in the number of infections. The reproduction number for the time before intervention is 1.5. To effectively contain a wave of infection, a reproduction number lower than 1 is necessary. At a specified point in time (labeled **day 0**, determined by reaching 20000 daily new cases in a population of 83 million) additional contact restrictions are introduced in the simulations. The model accounts for detected (hence reported) and undetected infectious individuals.

For further information on the mathematical background see:

Barbarossa, M.V.; Fuhrmann, J.  
Compliance with NPIs and Possible Deleterious Effects on Mitigation of an Epidemic Outbreak, Preprints 2021,  
https://www.preprints.org/manuscript/202102.0178/v2

---

#### **The webtool**
CoSiMo-Webtool users can select (i) the severity of the measures (intervention severity) and (ii) the proportion of the population that adheres to the additional measures (compliance level). Users can then choose which information from the model (for example new infections, cumulative infections, or total number of deaths) they want to visualize. In this way the user can observe how the course of the outbreak develops from the time the contact restrictions are introduced.

---

**Disclaimer**: In reality, the compliance degree with contact restriction measures will be different from person to person. In the mathematical model underlying these simulations the population is divided into two groups, with one group fully following the new measures (“compliant”) and the other group not modifying their behavior (“noncompliant”) after restrictions are introduced. It was also assumed that nobody changes from one group (“compliant” or “noncompliant”) to the other one.

