import astropy
import pandas as pd


class Processing():
    """Processing DataFrames.
    """

    def get_objects(self, astro_obj: object) -> dict:
        """Get the objects from the given astropy object .

        Args:
            astro_obj (object): [description]

        Returns:
            dict: [description]
        """
        ans = {
            "event_num":  astro_obj.field("FRAME"),
            "mult":  astro_obj.field("MULTIPLICITY"),
            "mult_i":  astro_obj.field("MULT"),
            "time":  astro_obj.field("TIME"),
            "pixel":  astro_obj.field("PIXEL"),
            "x":  astro_obj.field("X"),
            "y":  astro_obj.field("Y"),
            "energy":  astro_obj.field("ENERGY"),
            "event_type":  astro_obj.field("TYPE")
        }
        return ans

    def get_energy_dict(self, fits_dict: dict, only_mult_1: bool = True) -> dict:
        """Create a dictionary containing the tabdata ds for the FITS file .

        Args:
            fits_dict (dict): [description]

        Returns:
            dict: [description]
        """
        ans = {}
        for key in fits_dict.keys():
            if only_mult_1:
                mult_filter = self.get_objects(fits_dict[key]['tabdata'])["mult"] == 1
                data_temp = self.get_objects(fits_dict[key]['tabdata'])["energy"][mult_filter]
            ans[key[0:2]] = data_temp
        return ans

    def get_energy_tuple(self, fits_dict: dict, only_mult_1: bool = True) -> tuple:
        """Create a dictionary containing the tabdata ds for the FITS file .
        BROKEN
        Args:
            fits_dict (dict): [description]

        Returns:
            dict: [description]
        """
        ans = tuple(
            (key[0:2], self.get_objects(fits_dict[key]['tabdata'])["energy"])
            for key in fits_dict.keys()
            if self.get_objects(fits_dict[key]['tabdata'])["mult"].any() == 1
        )
        return ans
