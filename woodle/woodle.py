import csv
import optparse
import os
import shutil
from tempfile import NamedTemporaryFile

import pandas as pd


def convert(input, output, col, bareme):
    if not os.path.exists(input):
        raise Exception('Le fichier de promo n\'existe pas')
    if input.endswith('.csv'):
        donnees_promo = pd.read_csv(input, sep=',')
    else:
        donnees_promo = pd.read_excel(input).set_index('Numéro d\'identification')
    print(donnees_promo)

    tempfile = NamedTemporaryFile(mode='w+', encoding='iso-8859-1', delete=False)

    with open(output, 'r', encoding='iso-8859-1') as csvFile, tempfile:
        reader = csv.reader(csvFile, delimiter=';', quotechar='"')
        writer = csv.writer(tempfile, delimiter=';', quotechar='"')

        for row in reader:
            try:
                code = int(row[0])
                note = donnees_promo[col][code]
                if note != '-':
                    row[4] = note
                    row[5] = bareme
            except:
                pass
            writer.writerow(row)

    shutil.move(tempfile.name, output)


def main():
    """
    Point d'entrée pour le traitement.

    :return: codes de sortie standards.
    """
    # noinspection SpellCheckingInspection
    usage = 'usage: %prog <fichier moodle> <fichier snw> <colonne>'
    parser = optparse.OptionParser(usage=usage, add_help_option=False)
    parser.add_option('-b', dest="bareme", help="Barême.", metavar="BAREME",
                      default=20)
    parser.add_option('-h', '--help', action='help',
                      help="Affiche ce message d'aide et termine.")
    (opt, args) = parser.parse_args()
    if len(args) != 3:
        parser.error("Mauvais nombre de paramètres.")

    input = args[0]
    output = args[1]
    col = args[2]

    convert(input, output, col, opt.bareme)


if __name__ == '__main__':
    main()
