import pandas as pd
import numpy as np
import random
import itertools


class FeatureEngineering():
    """AI is creating summary for FeatureEngineering
    """
    def __init__(self) -> None:
        pass

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

    def count_bins_percentage(self, arr: np.ndarray) -> dict:
        """Receives arr already rounded and casted to string.

        Args:
            arr (np.ndarray): [description]

        Returns:
            dict: [description]
        """
        uniques, counts = np.unique(arr, return_counts=True)
        percentages = dict(zip(uniques, counts / len(arr)))
        return percentages

    def gen_mixed_energies_dict(self, energies_dict: dict, photons_amount: int,
                                amount_per_combination: int = 1000) -> dict:
        """Idea here is to receive the energy dict, just after data
        processing, them choose one key and combine with many others.
        If we have 7 keys, we will have 21 combinations 2 per 2.

        Args:
            energies_dict (dict): [description]

        Returns:
            dict: [description]
        """
        combinations_tuple = tuple(
            map(dict, itertools.combinations(energies_dict.items(), 2))
        )
        ans = {}
        for combination in combinations_tuple:
            print(f"Starting iteration through: \n {combination} \n")
            first_element = tuple(combination.items())[0]
            second_element = tuple(combination.items())[1]
            for i in range(amount_per_combination):
                ans[f"{first_element[0]}_{second_element[0]}_{i}"] = \
                    self.count_bins_percentage(
                        self.mix_numpy_arrays_comp_list(
                            tuple_arrays=(first_element[1], second_element[1]),
                            tuple_amounts=(photons_amount, photons_amount)
                        ).round().astype(str)
                    )
        return ans

        # ans = {
        #     combination.keys()
        #     for combination in combinations_tuple
        # }

    # def mix_numpy_arrays(self,
    #                      array1: np.ndarray,
    #                      array2: np.ndarray,
    #                      amount_first_array: int,
    #                      amount_second_array: int
    #                      ) -> np.ndarray:
    #     """IMPORTANTE A PORCENTAGEM VAI SER BASEADA DO TAMANHO DO OUTPUT

    #     Args:
    #         array1 (np.ndarray): [description]
    #         array2 (np.ndarray): [description]
    #         reduction_factor (int, optional): [description]. Defaults to 4.

    #     Returns:
    #         np.ndarray: [description]
    #     """
    #     return np.concatenate([
    #         np.random.choice(array1, amount_first_array),
    #         np.random.choice(array2, amount_second_array)
    #     ])        


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
    #     #TODO PAREI AQUI
    #     for i, elem_i in enumerate(energies_dict):
    #         for j, elem_j in enumerate(energies_dict[:i,i:]):
    #         random_element = random.choice(energies_tuple)
    #         ans[str(i)] = (random_element[0], self.count_bins(random_element[1]))
    #     return ans