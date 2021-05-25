1. Why use the Webtool?
The Webtool is designed to answer specific questions on the spread of infectious diseases that can be addressed with the help of mathematical models. 
The Webtool interface is supposed to be intuitive and easy to handle. Nonetheless, in the continuous effort of improving and enlarging our Webtool simulation library, we encourage the users to send us feedback and suggestions at their convenience (barbarossa@fias.uni-frankfurt.de).


2. Why use mathematical models for disease spread?
Mathematical models can help projecting how infectious diseases spread in a population and show possible outcomes of an epidemic under specific conditions. For instance, abstract scenarios based on deliberate assumptions can be used to (i) understand key mechanisms underlying the transmission dynamics of an infectious disease, (ii) investigate the importance of contact reduction in mitigating an outbreak, (iii) demonstrate the effects of treatment or isolation, or (iv) to simulate the distribution of vaccination, possibly investigating different prioritization strategies. Another possible goal of mathematical models, not pursued in this Webtool, would be short term forecasting of case or fatality counts following calibration to available data for a given geographic region. For COVID-19 cases/deaths forecasts we refer to the [German and Polish Forecast Hub](https://kitmetricslab.github.io/forecasthub/forecast) and to the [European Forecast Hub](https://covid19forecasthub.eu/index.html).


3. Are the simulations in the Webtool based on real data?
The major goal of the Webtool is to address general questions about the spread/control of infectious diseases. Though the models are not calibrated on reported time series, the simulations behind the Webtool are loosely based on the outbreak dynamics of the novel coronavirus pandemic (COVID-19) in Germany during 2020-21. 


4. What is the basic idea behind a disease transmission model?
Mechanistic compartment models like those underlying the Webtool divide a population into different groups (compartments) and use differential equations to describe the size change of these groups over time. A typical epidemic model contains at least compartments of infectious and susceptible individuals. Many models use more compartments, such as recovered, deceased, and exposed (infected but not yet infectious) individuals. An important feature of most COVID-19 models is the distinction between detected and undetected infected individuals.


5. What is the reproduction number?
The **basic reproduction number**, **R0**, of an infectious disease tells us how many other persons one single infectious individual would infect, when introduced in a totally naive (hence with no immunity nor specific protection against the disease) population. For most infectious diseases, people who have recovered are immune for a certain time, hence cannot be infected again. As a general estimate, a (1-1/R0 ) fraction of the population needs to become immune (either by natural infection or perfect vaccination) in order to achieve herd immunity. For COVID-19, R0 is estimated to be larger than 2 (a typical estimate is 3.5), meaning that more than two thirds of a population must be immune to reach herd immunity.

Once the presence of a new infectious disease is known, populations tend to employ counter measures like contact restrictions in order to curtail its spread. The resulting **control reproduction number**, **Rc**, is typically smaller than R0. As more and more individuals recover from the disease or are successfully vaccinated, the pool of susceptible individuals decreases and some contacts of any given infectious person will be with non-susceptible individuals. This effect is captured by the **effective reproduction number**, **Rt**, denoting the actual average number of people infected by any given infectious person at time t.
A reproduction number larger than 1 leads to rising incidence, whereas for a reproduction number lower than 1 the incidence decreases.


6. What is the difference between daily incidence and 7-day-incidence?
***Daily incidence*** indicates the number of persons entering a specific state (for example, daily new infected, daily new dead, daily new recovered) on any given day. This number is reported for the total population (for example, 83 million people). The ***7-day-incidence*** is calculated as the number of new reported cases within the past week per 100,000 inhabitants.
For example, if the daily incidences of a certain week sum up to 120.000 total new cases in a population of 83 million, this corresponds to a 7-days-incidence of 120.000/(83.000.000/100.000) = 144.6


7. What is the difference between reported and total cases?
For a disease which in some cases causes mild and unspecific symptoms, such as COVID-19, detection of all infected persons might be not possible. Therefore, some of the infectious individuals will circulate undetected and might importantly contribute to the spread of the disease in the population. ***Reported cases*** correspond to the number of infected people who have been confirmed by testing and have been reported to health authorities, whereas ***total cases*** include both reported cases and estimates for the underreported fraction of infected people.