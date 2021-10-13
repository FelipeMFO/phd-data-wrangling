import pandas as pd
import numpy as np
import random


class FeatureEngineering():
    """AI is creating summary for FeatureEngineering
    """
    def __init__(self) -> None:
        pass

    def mix_numpy_arrays(self,
                         array1: np.ndarray,
                         array2: np.ndarray,
                         amount_first_array: int,
                         amount_second_array: int
                         ) -> np.ndarray:
        """IMPORTANTE A PORCENTAGEM VAI SER BASEADA DO TAMANHO DO OUTPUT

        Args:
            array1 (np.ndarray): [description]
            array2 (np.ndarray): [description]
            reduction_factor (int, optional): [description]. Defaults to 4.

        Returns:
            np.ndarray: [description]
        """
        return np.concatenate([
            np.random.choice(array1, amount_first_array),
            np.random.choice(array2, amount_second_array)
        ])

    def mix_numpy_arrays_comp_list(self,
                                   tuple_arrays: tuple,
                                   tuple_amounts: tuple
                                   ) -> np.ndarray:
        """AI is creating summary for mix_numpy_arrays_comp_list

        Args:
            tuple_arrays (tuple): [description]
            tuple_amounts (tuple): [description]

        Returns:
            np.ndarray: [description]
        """
        return np.concatenate(
            [np.random.choice(arr, amount)
                for arr, amount in zip(tuple_arrays, tuple_amounts)]
        )

    def count_bins(self, arr: np.ndarray) -> tuple:
        return np.unique(arr.round(), return_counts=True)

    # def gen_df_mixed_energies(self, df_len: int,
    #                           energies_dict: dict) -> pd.DataFrame:
    #     """AI is creating summary for gen_df_mixed_energies

    #     Args:
    #         df_len (intenergies_dict): [description]

    #     Returns:
    #         pd.DataFrame: [description]
    #     """
    #     energies_tuple = tuple(energies_dict.items())
    #     ans = {}
    #     for i in len(df_len):
    #         random_element = random.choice(energies_tuple)
    #         ans[str(i)] = (random_element[0], self.count_bins(random_element[1]))
    #     return ans

    def gen_df_mixed_energies(self, df_len: int,
                              energies_dict: dict) -> pd.DataFrame:
        """AI is creating summary for gen_df_mixed_energies

        Args:
            df_len (intenergies_dict): [description]

        Returns:
            pd.DataFrame: [description]
        """
        energies_tuple = tuple(energies_dict.items())
        ans = {}
        #TODO PAREI AQUI
        for i, elem_i in enumerate(energies_dict):
            for j, elem_j in enumerate(energies_dict[:i,i:]):
            random_element = random.choice(energies_tuple)
            ans[str(i)] = (random_element[0], self.count_bins(random_element[1]))
        return ans