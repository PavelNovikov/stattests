import numpy as np
from functools import partial
import math


def _polynomial(*args):
    *coefficients, x = args
    result = coefficients[-1]
    for coef in coefficients[-2::-1]:
        result = result * x + coef

    return result


def percentage_point(p):
    """
    The function approximates percentage point z_p of the standard normal distribution
    corresponding to a prescribed value p for the lower tail area.

    :param p is a value between 0 and 1:
    :return value x between -inf and inf so that standard normal cdf of x is
    approximately equal to p:

    Wichura, Michael J. "Algorithm AS 241: The percentage points of the normal distribution."
    Journal of the Royal Statistical Society. Series C (Applied Statistics) 37.3 (1988): 477-484.
    """
    SPLIT1 = 0.425E0
    SPLIT2 = 5.0E0
    CONST1 = 0.180625E0
    CONST2 = 1.6E0

    A = partial(_polynomial,
                3.3871328727963666080E0,
                1.3314166789178437745E2,
                1.9715909503065514427E3,
                1.3731693765509461125E4,
                4.5921953931549871457E4,
                6.7265770927008700853E4,
                3.3430575583588128105E4,
                2.5090809287301226727E3
                )

    B = partial(_polynomial,
                1,
                4.2313330701600911252E1,
                6.8718700749205790830E2,
                5.3941960214247511077E3,
                2.1213794301586595867E4,
                3.9307895800092710610E4,
                2.8729085735721942674E4,
                5.2264952788528545610E3
                )

    C = partial(_polynomial,
                1.42343711074968357734E0,
                4.63033784615654529590E0,
                5.76949722146069140550E0,
                3.64784832476320460504E0,
                1.27045825245236838258E0,
                2.41780725177450611770E-1,
                2.27238449892691845833E-2,
                7.74545014278341407640E-4,
                )

    D = partial(_polynomial,
                1,
                2.05319162663775882187E0,
                1.67638483018380384940E0,
                6.89767334985100004550E-1,
                1.48103976427480074590E-1,
                1.51986665636164571966E-2,
                5.47593808499534494600E-4,
                1.05075007164441684324E-9
                )

    E = partial(_polynomial,
                6.65790464350110377720E0,
                5.46378491116411436990E0,
                1.78482653991729133580E0,
                2.96560571828504891230E-1,
                2.65321895265761230930E-2,
                1.24266094738807843860E-3,
                2.71155556874348757815E-5,
                2.01033439929228813265E-7
                )

    F = partial(_polynomial,
                1,
                5.99832206555887937690E-1,
                1.36929880922735805310E-1,
                1.48753612908506148525E-2,
                7.86869131145613259100E-4,
                1.84631831751005468180E-5,
                1.42151175831644588870E-7,
                2.04426310338993978564E-15
                )

    q = p - 0.5
    if abs(q) < SPLIT1:
        r = CONST1 - q ** 2
        ppnd16 = q * A(r) / B(r)
    else:
        r = p if q < 0 else 1 - p
        if r < 0:
            raise ValueError()
        r = math.sqrt(-math.log(r))
        if r < SPLIT2:
            r = r - CONST2
            ppnd16 = C(r) / D(r)
        else:
            r = r - SPLIT2
            ppnd16 = E(r) / F(r)
        if q < 0:
            ppnd16 = -ppnd16
    return ppnd16


def ztest(x, sigma, mu0):
    """
    """
    z = (np.mean(x) - mu0) / (sigma * np.sqrt(len(x)))

def mann_whitney():
    pass


def wilcoxon_rank_sum():
    pass


def wilcoxon_signed_rank():
    pass


def kruskal_wallis():
    pass


def friedman():
    pass


def chi_squared():
    pass


def shapiro_wilk():
    pass


def kolmogorov_smirnoff():
    pass


def levene():
    pass

def mauchly():
    pass


def durbin_watson():
    pass


def ttest():
    pass

