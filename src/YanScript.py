import urllib.error
import re
from urllib.request import urlopen
import csv
from io import StringIO
import os
import argparse


class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAILMAGENTA = '\033[95m'
    FAILRED = '\033[91m'
    ENDC = '\033[0m'


def create_mac_file(name, n_runs, beam_size, material, pos_z, path):
    m = re.search(r'\d', name)
    if m:
        indices = [0, m.start()]
        parts = [name[i:j] for i, j in zip(indices, indices[1:] + [None])]
        query = "-".join(parts)
    else:
        query = name

    url = f"http://www.nucleide.org/Laraweb/Results/{query:s}.txt"
    try:
        page = urlopen(url)
    except urllib.error.HTTPError:
        print(f"{bcolors.FAILMAGENTA}Error: Could not find {query:s} in the nuclide database{bcolors.ENDC}")
        exit()
    txt_bytes = page.read()
    try:
        txt = txt_bytes.decode("ASCII")
        warning = re.search(r'([1-9]*) lines out of ([1-9]*)', txt)
        m = re.search(r'Energy \(keV\)', txt)
        n = re.search(r'==.*', txt)
        table_txt = txt[m.start():n.start()]
    except UnicodeDecodeError:
        txt = txt_bytes.decode("ISO-8859-1")
        warning = re.search(r'([1-9]*) lines out of ([1-9]*)', txt)
        m = re.search(r'Énergie \(keV\)', txt)
        n = re.search(r'==.*', txt)
        table_txt = txt[m.start():n.start()].replace(",", ".")

    alist = []
    with StringIO(table_txt) as f:
        reader = csv.reader((line.replace(' ; ', ';') for line in f), delimiter=';')
        for row in reader:
            alist.append(row)

    list_no_alpha = [i for i in alist if i[4] != 'a']
    tlist = list(zip(*list_no_alpha))
    relevant_list = [tlist[0], tlist[2]]
    relevant_list = list(zip(*relevant_list))
    relevant_list = [(i[0], i[1]) for i in relevant_list[1:]]

    basename = f"run_{name:s}_{beam_size:d}.mac"
    filename = os.path.join(path, basename)
    intro = f"""# Can be run in batch, without GUI
# or interactively: Idle> /control/execute {basename:s}
#
/run/initialize
#
# Limit thread output to 1 thread
#/control/cout/ignoreThreadsExcept 0
#
# Run processing
#
#
# {name:s} X- and gamma-ray spectrum"""
    params = f"""
#
#
#
/gps/source/list
#
/simul/event/setVerbose 1
/simul/event/setNEvtsPrint 1000000
#
#
/simul/wall/material {material:s}"""
    with open(filename, "w") as writer:
        writer.write(intro)
        for row in relevant_list:
            source = f"""
#
#
# Intensity
/gps/source/add {row[1]:s}
/gps/particle gamma
#
# the incident surface is in the x-y plane
/gps/pos/rot1 1 0 0
/gps/pos/rot2 0 1 0
#
/gps/pos/type Point
/gps/pos/centre 0. 0. {pos_z:n} cm
#
# the source is isotropic in +- 30 deg (theta)
# 0 degrees dispersion
/gps/ang/type iso
/gps/ang/mintheta 0 deg
/gps/ang/maxtheta 30 deg
#
# energy of the spectral line
/gps/ene/mono {row[0]:s} keV"""
            writer.write(source)
        writer.write(params)
        for i in range(n_runs):
            instruction = f"""
#
#
#
/analysis/setFileName run{i:d}_{name:s}.root
/run/beamOn {beam_size:d}"""
            writer.write(instruction)

    if warning:
        print(f"{bcolors.WARNING}Warning: The script was only able to retrieve {txt[warning.start(): warning.end()]:s} for {name:s}{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKCYAN}Created macro file at {os.path.abspath(filename):s}{bcolors.ENDC}")


if __name__ == "__main__":
    os.system('color')
    parser = argparse.ArgumentParser(description='Create a macro file containing commands to simulate a point source')
    parser.add_argument('nuclide', metavar='nuclide', help='name of the nuclide (ex Cs137)')
    parser.add_argument('-r', '--runs', metavar='nb_runs', help='number of runs', default=10, type=int)
    parser.add_argument('-b', '--beam', metavar='beam_size', help='number of simulated photons', default=5000000,
                        type=int)
    parser.add_argument('-m', '--material', metavar='material', help='material of the wall', default="G4_AIR", type=str)
    parser.add_argument('-d', '--distance', metavar='distance', help='distance between the source and the camera in cm',
                        default=10, type=int)
    parser.add_argument('-p', '--path', metavar='path', help='path to save the .mac file',
                        default='', type=str)
    args = parser.parse_args()
    create_mac_file(name=args.nuclide, n_runs=args.runs, beam_size=args.beam, material=args.material,
                    pos_z=args.distance, path=args.path)