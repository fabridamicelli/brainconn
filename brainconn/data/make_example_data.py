import os.path as op

import numpy as np
import nibabel as nib
from nilearn import datasets, input_data
from nilearn.image import resample_to_img

from brainconn import utils

mask_img = datasets.load_mni152_brain_mask()
subjects = datasets.fetch_adhd(n_subjects=1)
power = datasets.fetch_coords_power_2011()

conf = subjects.confounds[0]
func_img = nib.load(subjects.func[0])
func_img = resample_to_img(func_img, mask_img)

coords = np.vstack((power.rois['x'], power.rois['y'], power.rois['z'])).T
spheres_masker = input_data.NiftiSpheresMasker(
    seeds=coords, smoothing_fwhm=4, radius=5.,
    detrend=True, standardize=True, low_pass=0.1, high_pass=0.01,
    t_r=func_img.header.get_zooms()[-1])

timeseries = spheres_masker.fit_transform(func_img,
                                          confounds=conf)
corr = np.corrcoef(timeseries.T)
np.savetxt(op.join(utils.get_resource_path(), 'example_corr.txt'), corr)
