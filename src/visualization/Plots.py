import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


class Plots():
    """Creates a new class that will be used for rendering the plots .
    """
    def __init__(self) -> None:
        pass

    def plot_spectrum(self, energy_array: np.ndarray) -> None:
        """AI is creating summary for plot_spectrum

        Args:
            energy_array (np.ndarray): [description]
        """
        spectrum, bins = np.histogram(
            energy_array,
            range=(0, 400),
            bins=3000)
        plt.plot(bins[:-1], spectrum)
        plt.xlabel("Energy (keV)")
        plt.ylabel("Counts")

    def plot_spectrums(
        self, energies_dict: dict, title: str,
        figsize: tuple = (16, 12), ncols: int = 2,
        max_energy: int = 350
    ) -> None:
        """AI is creating summary for plot_spectrum

        Args:
            energies_dict ([type]): [description]
            title ([type]): [description]
            tuple (tuple, optional): [description]. Defaults to (16,12).
            ncols (int, optional): [description]. Defaults to 2.
        """
        nrows = (len(energies_dict)//ncols) + 1 if (len(energies_dict)%ncols) != 0 else len(energies_dict)//ncols
        fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize= figsize)
        fig.suptitle(title, fontsize=20)
        for key, ax in zip(energies_dict.keys(), axs.flat):
            data = energies_dict[key]
            spectre, bins = np.histogram(data,range = (0, max_energy),bins = 3000)

            ax.plot(bins[:-1],spectre)
            ax.set_xlabel("Energy (keV)")
            ax.set_ylabel("Counts")
            ax.set_title(f"Single events from {key.capitalize()} spectrum")
        plt.tight_layout()

    def plot_spectrums_overlapping(
        self, energies_dict: dict, title:str,
        figsize: tuple = (16,12)
    ) -> None:
        """AI is creating summary for plot_spectrums_overlapping

        Args:
            energies_dict (dict): [description]
            title (str): [description]
            figsize (tuple, optional): [description]. Defaults to (16,12).
        """
        
        plt.figure(figsize=figsize)
        plt.title(title)
        for key in energies_dict.keys():
            spectre, bins = np.histogram(energies_dict[key],range = (0,202),bins = 3000)
            
            plt.plot(bins[:-1],spectre)
            plt.xlabel("Energy (keV)")
            plt.ylabel("Counts")
