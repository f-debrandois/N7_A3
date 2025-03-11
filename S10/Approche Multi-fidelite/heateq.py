import numpy as np
import math

################################################################
################################ Initial Condition
################################################################

def G(xi):
    return 50 * (4*np.abs(xi[4]) - 1) * (4*np.abs(xi[5]) - 1) * (4*np.abs(xi[6]) - 1)

def I(xi):
    return 3.5 * (np.sin(xi[0]) + 7*np.sin(xi[1])**2 + 0.1*np.sin(xi[0])*xi[2]**4 )

def F1(x):
    return np.sin(np.pi*x)

def F2(x):
    return np.sin(2*np.pi*x) + np.sin(3*np.pi*x) + \
        50 * ( np.sin(9*np.pi*x) + np.sin(21*np.pi*x) )

def initial_cond(x, xi):
    """
    Args:
        x: discretized x coordinate
        xi: numpy array of dimension 7.
    """
    return F1(x)[:, None]*G(xi)[None, :] + F2(x)[:, None]*I(xi)[None, :]

################################################################
################################ H_n
################################################################

def H_n(t, alpha_min, alpha_max, n):
    """
    Args:
        t: considered time.
        alpha_min: lower bound of the r.v. alpha = xi[3].
        alpha_max: upper bound of the r.v. alpha = xi[3].
        n: mode index
    """
    deltaAlpha = alpha_max - alpha_min
    n2pi2t = (n * math.pi)**2 * t
    term1 = n2pi2t * deltaAlpha
    term2 = math.exp(-n2pi2t * alpha_min)
    term3 = math.exp(-n2pi2t * alpha_max)
    return (term2 - term3) / term1

################################################################
################################ Discrete solution using quadrature (Equation 5.4)
################################################################

def sol_quad(t, xi, x, n, sn):
    u0 = initial_cond(x, xi)                                                    # -> (nx, ns)
    snu0 = sn[:, :, None] * u0[None, :, :]                                      # -> (n_modes, nx, ns)
    A_n_quad = np.trapz(snu0, x=x, axis=1)                                      # -> (n_modes, ns)
    term2 = A_n_quad * np.exp(-xi[3][None, :] * (n[:, None] * np.pi)**2 * t)    # -> (n_modes, ns)

    return 2 * np.sum(sn[:, :, None] * term2[:, None, :], axis=0)            # -> (nx, ns)

def QoI_quad(t, xi, x, n, sn):
    sol_x = sol_quad(t, xi, x, n, sn)                                           # -> (nx, ns)
    return np.trapz(sol_x, x=x, axis=0)

################################################################
# Esperance exacte (de la solution continue exacte)
################################################################
def E_QoI(t, alpha_min, alpha_max):
    """
    Args:
        t: considered time.
        alpha_min: lower bound of the r.v. alpha.
        alpha_max: upper bound of the r.v. alpha.
    """
    term1 = 100  * H_n(t, alpha_min, alpha_max, n=1)  / math.pi
    term2 = 49   * H_n(t, alpha_min, alpha_max, n=3)  / (6 * math.pi)
    term3 = 1225 * H_n(t, alpha_min, alpha_max, n=9)  / (9 * math.pi)
    term4 = 175  * H_n(t, alpha_min, alpha_max, n=21) / (3 * math.pi)
    return term1 + term2 + term3 + term4


################################################################
# Esperance exacte de la solution discretisee par quadrature
################################################################

def E_QoI_quad(t, alpha_min, alpha_max, x, n, sn):
    H = np.array( [H_n(t, alpha_min, alpha_max, n=k) for k in n] )  # shape (n_modes,)

    snF1 = sn * F1(x)                                               # shape (n_modes, nx)
    snF2 = sn * F2(x)                                               # shape (n_modes, nx)

    quad_sn = np.trapz(sn, x=x)                                     # shape (n_modes,)
    quad_snF1 = np.trapz(snF1, x=x)                                 # shape (n_modes,)
    quad_snF2 = np.trapz(snF2, x=x)                                 # shape (n_modes,)

    return ( H * quad_sn * ( 100.*quad_snF1 + 24.5*quad_snF2 ) ).sum()



################################################################
# Simulateurs : fidelite = (nombre de points de quadrature, nombre de termes dans la serie tronquee)
################################################################
class Exact:
    def __init__(self):
        self.mu = E_QoI(0.5, 0.001, 0.009)

class Simulateur:
    def __init__(self, n_term=21, n_quad=100):
        self.n_modes = n_term
        self.nx = n_quad
        self.x = np.linspace(start=0., stop=1., num=self.nx)    # -> nx
        self.n = np.arange(1, self.n_modes + 1, dtype=int)      # -> n_modes
        xx, nn = np.meshgrid(self.x, self.n, copy=False)        # -> (n_modes, nx)
        self.sn = np.sin(xx * nn * math.pi)                     # -> (n_modes, nx)
        self.mu = E_QoI_quad(0.5, 0.001, 0.009, self.x, self.n, self.sn)

    def __call__(self, xi, nbatch=10000):
        ns = xi.shape[1]
        assert(xi.ndim == 2)
        assert(xi.shape[0] == 7)
        assert(ns > 0)

        if ns <= nbatch:
            return QoI_quad(0.5, xi, self.x, self.n, self.sn)
        else:
            Y = np.zeros(ns)
            ns_remaining = ns
            istart = 0
            while ns_remaining > 0:
                ns_batch = min(nbatch, ns_remaining)
                Y[istart:istart+ns_batch] = QoI_quad(0.5, xi[:,istart:istart+ns_batch], self.x, self.n, self.sn)
                istart += ns_batch
                ns_remaining -= ns_batch
            return Y