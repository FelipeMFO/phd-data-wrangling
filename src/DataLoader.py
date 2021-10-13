import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


class DataLoader():
    """A class loader that handles the same data loader .
    """

    def __init__(self, folder: str) -> None:
        self.folder = folder

    def load_fits(self, files: list, remove_na: bool = True) -> dict:
        """Load FITS files.

        Args:
            files (list): list of files to open.

        Returns:
            dict: dictionary with readen files.
        """
        ans = {
            f"{file.replace('.fits', '').lower()}": {
                "header": fits.open(self.folder+file)[1].header,
                "tabdata": fits.open(self.folder+file)[1].data
            }
            for file in files
        }
        if remove_na:
            del ans["na_recalibrated_touslespix"]
        return ans
