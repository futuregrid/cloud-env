#!/usr/bin/env python

#import argparse
#import os
import pprint
import optparse
from cmd2 import Cmd
from cmd2 import make_option
from cmd2 import options
#from cmd2 import Cmd2TestCase

#from futuregrid.virtual.cluster.FGCluster import Cluster
#from FGCluster import Cluster

import unittest
import sys


class Shell(Cmd):
    #multilineCommands = ['None']
    #Cmd.shortcuts.update({'&': 'speak'})
    #maxrepeats = 3
    #Cmd.settable.append('maxrepeats')

    pp = pprint.PrettyPrinter(indent=0)

    echo = True
    timing = True
    cluster = None

    prompt = "fg> "

    logo = """
  _____       _                   ____      _     _
 |  ___|_   _| |_ _   _ _ __ ___ / ___|_ __(_) __| |
 | |_  | | | | __| | | | '__/ _ \ |  _| '__| |/ _` |
 |  _| | |_| | |_| |_| | | |  __/ |_| | |  | | (_| |
 |_|    \__,_|\__|\__,_|_|  \___|\____|_|  |_|\__,_|
----------------------------------------------------
    """

    def preloop(self):
        self.cluster = Cluster()
        print self.logo

    def postloop(self):
        print "BYE FORM GREGOR"

    @options([
        make_option('-f', '--file', type="string",
                    help="cluster name"),
        make_option('-i', '--interface', type="string",
                    help="interface")
        ])
    def do_config(self, args, opts):

        if not opts.file:
            self.cluster.parse_conf()
        else:
            self.cluster.parse_conf()
        self.cluster.set_interface(opts.interface)

    def do_debug(self, debug=True):
        print "to do debug"

    @options([
        make_option('-a', '--name', type="string",
                    help="cluster name"),
        make_option('-n', '--number', type="int",
                    help="number of computation nodes"),
        make_option('-t', '--type', type="string",
                    help="instance type"),
        make_option('-i', '--image', type="string",
                    help="image id"),
        ])
    def do_run(self, args, opts):
        print "run"

    @options([
        make_option('-a', '--name', type="string",
                    help="cluster name"),
        make_option('-c', '--controlb', type="string",
                    help="control node bucket"),
        make_option('-t', '--controln', type="string",
                    help="control node image"),
        make_option('-m', '--computeb', type="string",
                    help="compute node bucket"),
        make_option('-e', '--computen', type="string",
                    default='not specified',
                    help="compute node image"),
        ])

    @options([
        make_option('-a', '--name', type="string",
                    help="cluster name"),
        ])
    def do_example(self, args, opts):
        print "hallo example"
        print args
        print opts

def main():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--test',
                      dest='unittests',
                      action='store_true',
                      default=False,
                      help='Run unit test suite')
    (callopts, callargs) = parser.parse_args()
    if callopts.unittests:
        sys.argv = [sys.argv[0]]  # the --test argument upsets unittest.main()
        unittest.main()
    else:
        app = Shell()
        app.cmdloop()

if __name__ == '__main__':
    main()
