#!/usr/bin/env python
# coding: utf-8

import argparse
import os

def criarprojeto_input(project):
    print '-'*60
    print 'Maven comand line'
    print '-'*60
    print 'Project Package (ex: com.company.samples):'
    package = raw_input('')
    criarprojeto(project, package)
    
def criarprojeto(project, package):
    command = 'mvn archetype:generate -DarchetypeGroupId=br.com.caelum.vraptor.archetypes' + \
              ' -DarchetypeArtifactId=vraptor-hibernate-archetype' + \
              ' -DarchetypeVersion=0.0.1' + \
              ' -DgroupId=' + package + \
              ' -DartifactId=' + project + \
              ' -Dversion=0.0.1' + \
              ' -DpackageName=' + package + \
              ' -DinteractiveMode=false'
              
    print 'Executing...', command
    os.system(command)
    print 'Done!'
    print ''
    
parser = argparse.ArgumentParser(description='MVN-2-CODE')
parser.add_argument('project', help='project name')

args = parser.parse_args()
criarprojeto_input(args.project)
