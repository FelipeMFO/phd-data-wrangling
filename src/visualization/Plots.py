import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class Plots():
    """Creates a new class that will be used for rendering the plots .
    """
    def __init__(self) -> None:
        pass
    
    def plot_spectrums(
        self, energies_dict: dict, title: str,
        figsize: tuple = (16,12), ncols:int = 2
    ) -> None:
        """AI is creating summary for plot_spectrum

        Args:
            energies_dict ([type]): [description]
            title ([type]): [description]
            tuple (tuple, optional): [description]. Defaults to (16,12).
            ncols (int, optional): [description]. Defaults to 2.
        """
        nrows = (len(energies_dict)//ncols) + 1
        fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize= figsize)
        fig.suptitle(title, fontsize=20)
        for key, ax in zip(energies_dict.keys(), axs.flat):
            data = energies_dict[key]
            spectre, bins = np.histogram(data,range = (0,data.max()*0.7),bins = 3000)

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
            

    # def plot_spectrum(self, energies_dict:dict, title: str,
    #                   figsize: tuple = (16,12), ncols:int = 2) -> None:
    #     """Plot the spectrum of the given dictionary .

    #     Args:
    #         dfs_dict (dict): [description]
    #         ncols (int, optional): [description]. Defaults to 2.
    #     """
    #     nrows = (len(energies_dict)//ncols) + 1
    #     fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    #     fig.suptitle(title, fontsize=20)

    #     for ax, key in zip(axs.flat, energies_dict.keys()):
    #         data = energies_dict[key]
    #         ax.set(xlim=(0, data.max()*1.1))
    #         ax.set_title(f"Single events of {key.capitalize()} spectrum")
    #         ax.set_xlabel("Energy (keV)")
    #         sns.histplot(
    #             data=data,
    #             ax = ax,
    #             bins=100,
    #             kde=True)
