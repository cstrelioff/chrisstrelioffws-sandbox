
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

# use matplotlib style sheet
try:
    plt.style.use('ggplot')
except:
    # version of matplotlib might not be recent
    pass


class likelihood:
    def __init__(self, data):
        """Likelihood for binary data."""
        self.counts = {s:0 for s in ['0', '1']}
        self._process_data(data)
 
    def _process_data(self, data):
        """Process data."""
        temp = [str(x) for x in data]
        for s in ['0', '1']:
            self.counts[s] = temp.count(s)

        if len(temp) != sum(self.counts.values()):
            raise Exception("Passed data is not all 0`s and 1`s!")
    
    def _process_probabilities(self, p0):
        """Process probabilities."""
        n0 = self.counts['0']
        n1 = self.counts['1']

        if p0 != 0 and p0 != 1:
            # typical case
            logpr_data = n0*np.log(p0) + \
                         n1*np.log(1.-p0)
            pr_data = np.exp(logpr_data)
        elif p0 == 0 and n0 != 0:
            # p0 can't be 0 if n0 is not 0
            logpr_data = -np.inf
            pr_data = np.exp(logpr_data)
        elif p0 == 0 and n0 == 0:
            # data consistent with p0=0
            logpr_data = n1*np.log(1.-p0)
            pr_data = np.exp(logpr_data)            
        elif p0 == 1 and n1 != 0:
            # p0 can't be 1 if n1 is not 0
            logpr_data = -np.inf
            pr_data = np.exp(logpr_data)
        elif p0 == 1 and n1 == 0:
            # data consistent with p0=1
            logpr_data = n0*np.log(p0)
            pr_data = np.exp(logpr_data)

        return pr_data, logpr_data
        
    def prob(self, p0):
        """Get probability of data."""
        pr_data, _ = self._process_probabilities(p0)

        return pr_data
    
    def log_prob(self, p0):
        """Get log of probability of data."""
        _, logpr_data = self._process_probabilities(p0)

        return logpr_data


class prior:
    def __init__(self, p_list, p_probs=None):
        """The prior.

        p_list: list of allowed p0's
        p_probs: [optional] dict of prior probabilities
                 default is uniform
        """
        if p_probs:
            # make sure prior is normalized
            norm = sum(p_probs.values())
            self.log_pdict = {p:np.log(p_probs[p]) - \
                                np.log(norm) for p in p_list}
        else:
            n = len(p_list)
            self.log_pdict = {p:-np.log(n) for p in p_list}

    def __iter__(self):
        return iter(sorted(self.log_pdict))

    def log_prob(self, p):
        """Get log prior probability for passed p0."""
        if p in self.log_pdict:
            return self.log_pdict[p]
        else:
            return -np.inf

    def prob(self, p):
        """Get prior probability for passed p0."""
        if p in self.log_pdict:
            return np.exp(self.log_pdict[p])
        else:
            return 0.0


class posterior:
    def __init__(self, data, prior):
        """The posterior.

        data: a data sample as list
        prior: an instance of the prior class
        """
        self.likelihood = likelihood(data)
        self.prior = prior

        self._process_posterior()

    def _process_posterior(self):
        """Process the posterior using passed data and prior."""
        
        numerators = {}
        denominator = -np.inf
        for p in self.prior:
            numerators[p] = self.likelihood.log_prob(p) + \
                            self.prior.log_prob(p)

            if numerators[p] != -np.inf:
                # np.logaddexp(-np.inf, -np.inf) issues warning
                # skip-- this is adding 0 + 0
                denominator = np.logaddexp(denominator,
                                           numerators[p])

        # save denominator in Bayes' Theorem
        self.log_marg_likelihood = denominator

        # calculate posterior
        self.log_pdict = {}
        for p in self.prior:
            self.log_pdict[p] = numerators[p] - \
                                self.log_marg_likelihood

    def log_prob(self, p):
        """Get log posterior probability for passed p."""
        if p in self.log_pdict:
            return self.log_pdict[p]
        else:
            return -np.inf

    def prob(self, p):
        """Get posterior probability for passed p."""
        if p in self.log_pdict:
            return np.exp(self.log_pdict[p])
        else:
            return 0.0

    def plot(self):
        """Plot the inference resuults."""

        f, ax= plt.subplots(3, 1, figsize=(8, 6), sharex=True)

        # get candidate probabilities from prior
        x = [p for p in self.prior]
        
        # plot prior
        y1 = np.array([self.prior.prob(p) for p in x])
        ax[0].stem(x, y1, linefmt='r-', markerfmt='ro', basefmt='w-')
        ax[0].set_ylabel("Prior", fontsize=14)
        ax[0].set_xlim(-0.05, 1.05)
        ax[0].set_ylim(0., 1.05*np.max(y1))
        
        # plot likelihood
        y2 = np.array([self.likelihood.prob(p) for p in x])
        ax[1].stem(x, y2, linefmt='k-', markerfmt='ko', basefmt='w-')
        ax[1].set_ylabel("Likelihood", fontsize=14)
        ax[1].set_xlim(-0.05, 1.05)
        ax[1].set_ylim(0., 1.05*np.max(y2))

        # plot posterior 
        y3 = np.array([self.prob(p) for p in x])
        ax[2].stem(x, y3, linefmt='b-', markerfmt='bo', basefmt='w-')
        ax[2].set_ylabel("Posterior", fontsize=14)
        ax[2].set_xlabel("Probability of Zero", fontsize=14)
        ax[2].set_xlim(-0.05, 1.05)
        ax[2].set_ylim(0., 1.05*np.max(y3))
        
        plt.tight_layout()
        plt.show()



# data
data1 = [0,0,0,0,1,1,0,0,0,1]

# prior
A1 = prior([0.2, 0.4, 0.6, 0.8])

# posterior
post1 = posterior(data1, A1)
post1.plot()


# prior -- will be normalized by class
A2 = prior([0.2, 0.4, 0.6, 0.8],
           {0.2:1, 0.4:20, 0.6:1, 0.8:1})

# posterior
post2 = posterior(data1, A2)
post2.plot()


# set probability of 0
p0 = 0.23
# set rng seed to 42
np.random.seed(42)
# generate data
data2 = np.random.choice([0,1], 500, p=[p0, 1.-p0])

# prior
A3 = prior(np.arange(0.0, 1.01, 0.01))

# posterior
post3 = posterior(data2, A3)
post3.plot()
