import numpy as np
import struct
try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def bin_to_float(b):
    """ Convert binary string to a float. """
    # https://docs.python.org/3/library/struct.html
    return struct.unpack('<d', b)[0] # read double in little-endian


def convert_cls2fls(data_cls,NbClasses,NbMaps):
    # helper function
    # data_cls: dict of np array
    # create features and labels from data_cls
    i = 0
    j = 0
    features = np.zeros((NbClasses*NbMaps,data_cls[i][j,...].size))
    labels = np.zeros((NbClasses*NbMaps))
    sid = 0 # sample id
    for i in range(NbClasses):
        for j in range(NbMaps):
            #print(sid,NbClasses*NbMaps)
            #print(data_cls[i][j,:])
            #print(features.shape)
            #print(data_cls[i][j,:].shape)
            features[sid,:] = data_cls[i][j,...].reshape(-1)
            labels[sid] = i
            sid += 1
    return features,labels

def isotropic_powspec(image):
    """
	Adapted from pywavan package: https://github.com/jfrob27/pywavan/tree/master
	Calculate the power spectrum of a 2D image.

	Parameters
	----------
	image : array_like
		Input array, must 2-dimentional and real

	Returns
	-------

	tab_k : Array of spatial scales used for the decomposition
	spec_k: The power spectrum
	"""
    na = float(image.shape[1])
    nb = float(image.shape[0])
    nf = max(na, nb)
    
    k_crit = nf/2    
    bins = np.arange(k_crit+1)

	#Fourier transform & 2D power spectrum
	#---------------------------------------------

    imft = np.fft.fft2(image)
    ps2D = np.abs(imft)**2 / (na*nb)
    del imft

	#Set-up kbins
	#---------------------------------------------

    x = np.arange(na)
    y = np.arange(nb)
    x, y = np.meshgrid(x, y)

    if (na % 2) == 0:
        x = (1.*x - ((na)/2.)) / na
        shiftx = na/2.
    else:
        x = (1.*x - (na-1)/2.)/ na
        shiftx = (na-1.)/2. + 1

    if (nb % 2) == 0:
        y = (1.*y - ((nb/2.))) / nb
        shifty = nb/2.
    else:
        y = (1.*y - (nb-1)/2.)/ nb
        shifty = (nb-1.)/2. + 1

    k_mat = np.sqrt(x**2 + y**2)
    k_mat = k_mat * nf 
	
    k_mat = np.roll(k_mat, int(shiftx), axis=1)
    k_mat = np.roll(k_mat, int(shifty), axis=0)
    k_mod = np.round(k_mat,decimals=0)

    hval, _ = np.histogram(k_mod, bins=bins)

	#Average values in same k bin
	#---------------------------------------------

    kval = np.zeros(np.int(k_crit))
    kpow = np.zeros(np.int(k_crit))

    for j in range(np.int(k_crit)):

        kval[j] = np.sum(k_mod[k_mod == np.float(j)]) / hval[j]
        kpow[j] = np.sum(ps2D[k_mod == np.float(j)]) / hval[j]
            
    spec_k = kpow[1:np.size(hval)-1]
    tab_k = kval[1:np.size(hval)-1] / (k_crit * 2.)

    return tab_k, spec_k


from colorsys import hls_to_rgb

def colorize(z):
    n, m = z.shape
    c = np.zeros((n, m, 3))
    c[np.isinf(z)] = (1.0, 1.0, 1.0)
    c[np.isnan(z)] = (0.5, 0.5, 0.5)

    idx = ~(np.isinf(z) + np.isnan(z))
    A = (np.angle(z[idx]) + np.pi) / (2*np.pi)
    A = (A + 0.5) % 1.0
    B = 1.0/(1.0 + abs(z[idx])**0.3)
    c[idx] = [hls_to_rgb(a, b, 0.8) for a, b in zip(A, B)]
    return c

