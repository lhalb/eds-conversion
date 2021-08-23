"""
!/Users/ebeam02/AppData/Local/Programs/Python
!/usr/bin/env python
 -*- coding: utf-8 -*-
Script zum Einlesen von EDX-Linenscans aus dem REM
Author: Hollmann
Date: 2019-07-03
"""
# import matplotlib
# import numpy as np

# matplotlib.use('Qt5Agg')
# import matplotlib.pyplot as plt
import pandas as pd
from os import walk
import os.path as op


def write_data_to_file(df, path, mode, sheet_name):
    with pd.ExcelWriter(path, mode=mode) as writer:
        df.to_excel(writer, sheet_name=sheet_name)
    return


def gleit_durch(x, N=20):
    return x.rolling(window=N).mean()


def get_data(fname):
    """
    Funktion zum Einlesen der Daten.
    Hier kann festgelegt werden, wie auf die verschiedenen Formate des Export reagiert wird.
    Rückgabewerte:
    - einzelner Datenframe für Messwerte
    - Datenframe für Prozessdaten
    - Einheiten für weitere Berechnungen
    """
    def get_encoding(file):
        from chardet import detect
        rawdata = open(file, 'rb').read()
        result = detect(rawdata)
        return result['encoding']
    encode = get_encoding(fname)
    # importiere die ersten 100 Zeilen der 1. Spalte der 1. Spalte
    cs = pd.read_csv(fname, names=['a', 'b', 'c'], usecols=[0], nrows=100, delimiter=',', header=None, encoding=encode, skipinitialspace=True)
    # ersetze Kommas (falls vorhanden), damit Zahlen erkannt werden
    cs = cs.a.str.replace(',.', '.', regex=True)
    # konvertiere in numerische Werte und setze alle Texte auf 'nan'
    cs = pd.to_numeric(cs, errors='coerce')
    # verwerfe 'nan' und gebe ersten numerischen Wert zurück (= Beginn der Daten)
    skr = cs.dropna().index[0]
    # lese Kopf ein (um elementnamen zu bekommen)
    head = pd.read_csv(fname, skiprows=skr-1, nrows=1, delimiter=',', header=None, encoding=encode,skipinitialspace=True).values[0]
    info = pd.read_csv(fname,nrows=skr-1,header=None, encoding=encode)

    df = pd.read_csv(fname, index_col=[0], usecols=head[:-2], names=head[:-2], skiprows=skr, delimiter=',', decimal='.', header=None, encoding=encode, skipinitialspace=True)
    type = info.values[11, 1]  # hier steht, ob es ROI, AT% oder WT% ist
    elements = head[2:-2:1]
    return df, type, elements


def get_files_to_process(path):
    files_to_process = []

    if op.isfile(path):
        files_to_process.append(path)
    else:
        for root, dirs, files in walk(path, topdown=False):
            for name in files:
                files_to_process.append(op.normpath(op.join(root, name)))
    return files_to_process


def get_smoothed_data(df, elements, n):
    # Erzeuge einen neuen DataFrame mit den geglätteten Werten
    df_smooth = pd.DataFrame(gleit_durch(df[elements], n), columns=elements)
    # Erzeuge neue Namen für die Überschriften
    new_elements = [f'{n} (filt)' for n in elements]
    #  Ersetze die alten Spaltenüberschriften
    df_smooth.columns = new_elements

    #  Erzeuge neue Rohdaten für die Ausgabe
    old_elements = [f'{n} (raw)' for n in elements]
    #  Füge die Distanzspalte hinzu
    old_elements.insert(0, 'Distance (um)')

    #  Kopiere den alten DataFrame
    df_raw = df.copy()
    #  Ersetze die Alten Spaltenüberschriften mit den neuen(enthält den Zusatz"(raw)"
    df_raw.columns = old_elements

    # Füge beide Dataframes zusammen
    df_out = pd.concat([df_raw, df_smooth], axis=1)

    return df_out


# def plot_data(x, y, y2=None, messtyp='', n=''):
#     plt.figure()
#     plt.plot(x, y, 'b-', label='Rohdaten')
#     if y2 is None:
#         pass
#     else:
#         plt.plot(x, y2, 'r-', label='Geglättet')
#     plt.legend()
#     plt.ylabel(f'{y.name}-{messtyp}', fontweight='bold')
#     plt.xlabel(x.name, fontweight='bold')
#     plt.title(f'{y.name.split(" ")[0]}, Art:{messtyp}, n={n}', fontsize=12, fontweight='bold')
#     plt.show()


def run_process(path, smooth_data=False, smooth_window=10,
                plot_only=False, dtype='.csv', output_folder='', plot_elements=False):

    smooth = smooth_data
    window = smooth_window

    files = get_files_to_process(path)

    old_dir = None
    for f in files:
        processed_dir = op.basename(op.dirname(f))

        filename = op.split(f)[1]

        # überspringe die bereits erstellten XLSX Dateien
        if op.splitext(f)[1] == dtype:
            pass
        else:
            continue

        df, calc_type, elements = get_data(f)

        if not plot_elements:
            elements_to_plot = elements
        else:
            elements_to_plot = plot_elements

        if smooth:
            #  Setze den Wert der Ausgabevariablen
            export_data = get_smoothed_data(df, elements, window)
            # if plot_only:
            #     for el in elements_to_plot:
            #         plot_data(export_data['Distance (um)'],
            #                   export_data[f'{el} (raw)'], export_data[f'{el} (filt)'],
            #                   messtyp=calc_type, n=window)
        else:
            export_data = df
            # if plot_only:
            #     for el in elements_to_plot:
            #         plot_data(export_data['Distance (um)'], export_data[el], messtyp=calc_type, n=window)

        if not plot_only:
            export_data['Filename'] = filename
            export_data.iloc[1:, export_data.columns.get_loc('Filename')] = ''


            #  wenn der Ordner noch nicht abgearbeitet wurde
            if processed_dir != old_dir:
                # erzeuge neue Datei
                mode = 'w'
            else:
                #  Ansonsten schreibe in der aktuellen weiter
                mode = 'a'

            # print(f)

            if output_folder == '':
                out_dir = op.dirname(f)
                # print(out_dir)
            else:
                out_dir = output_folder

            fname = processed_dir + '.xlsx'

            fout = op.join(out_dir, fname)

            # print(f'Ich würde unter {fout} im Modus {mode} speichern.')

            write_data_to_file(export_data, fout, mode, calc_type)

            # Setze den alten Ordner als aktuellen Ordner, um zu gewährleisten,
            # dass man im gleichen Verzeichnis arbeitet
            old_dir = processed_dir
        else:
            continue


def check_path(p):
    if p is not None:
        if op.exists(p):
            if op.isfile(p):
                ret_string = 'datei'
            else:
                ret_string = 'ordner'
        else:
            ret_string = 'anderes'
    else:
        ret_string = 'anderes'

    return ret_string



if __name__ == '__main__':
    run_process()