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

    def get_tabdata_dfs_dict(self, fits_dict: dict, only_mult_1:bool = True) -> dict:
        """Create a dictionary containing the tabdata ds for the FITS file .

        Args:
            fits_dict (dict): [description]

        Returns:
            dict: [description]
        """
        ans = {}
        for key in fits_dict.keys():
            df_temp = pd.DataFrame(self.get_objects(fits_dict[key]['tabdata']))
            if only_mult_1: df_temp.drop(df_temp[df_temp.mult != 1].index, inplace=True)
            ans[key[0:2]] = df_temp
        return ans
