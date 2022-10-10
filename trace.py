#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import *


# Question 1.
# Les distances sémantiques à l'exécution pour ce programme consiste à l'écriture des arguments.
# Les distances sémantiques à l'interprétation pour ce programme consiste à l'affichage des résultats dépendant de ce qu'on a écrit en argument

# Question 5 et 6 non réussi.
 
# ./trace.py -o graph.ps --xmin -150 --xmax 150 --nstep 50 "sin(pi*x/180)"

def trace(function, xmin, xmax, nstep, output):
    output.write("x, %s\n" % function)
    function = eval("lambda x:" + function)
    
    step = 1.*(xmax-xmin)/nstep
    for i in range(nstep+1):
        x = xmin + i*step
        try:
            y = function(x)
        except:
            continue
        output.write("%s, %s\n" % (x, y))


def trace_courbe(function, xmin, xmax, ymin, ymax, nstep, output):
    output.write("x, %s\n" % function)
    function = eval("lambda x:" + function)
    step = 1. * (xmax - xmin) / nstep
    
    #non réussi
    echelle = 450 * (xmax-xmin)/nstep
    for i in range(1, nstep + 1):
        x = xmin + i * step
        try:
            y = function(x)
        except:
            continue
        
        output.write("%s %s lineto\n" % (x*echelle, y*echelle))
    
    output.write("stroke\n")
    output.write("showpage\n")

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    import getopt
    try:
        # Quand je place le h après le o, le help est non fonctionnel, je n'ai pas trouvé la raison
        options, argv = getopt.getopt(argv[1:], "ho:", ["output=", "xmin=", "xmax=", "nstep="])
    except getopt.GetoptError as message:
        sys.stderr.write("%s\n" % message)
        sys.exit(1)
    
    output = sys.stdout
    xmin, xmax = 0., 1.
    nstep = 10
    
    for option, value in options:
        if option in ["-h", "--help"]:
            sys.stderr.write("-h: affichage de l'aide\n")
            sys.stderr.write("-o: écrire la sortie fichier\n")
        elif option in ["-o", "--output"]:
            output = open(value, "w")
        elif option in ["--xmin"]:
            xmin = float(value)
        elif option in ["--xmax"]:
            xmax = float(value)
        elif option in ["--nstep"]:
            nstep = int(value)
        else:
            assert False, "unhandled option"
    

    if len(argv) != 1:
        sys.stderr.write("vous n'avez pas mis assez d'argument, minimum 1 requis\n")
        sys.stderr.write("vous pouvez fournir la fonction a utilisé, et les paramètres requis tel que le output (fichier de sortie), le xmin, le xmax et également le nstep.")
        sys.exit(1)
    function = argv[0]

    trace_courbe(function, xmin, xmax, -2, 2, nstep, output)

    


if __name__ == "__main__":
    sys.exit(main())
