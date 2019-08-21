# coding: utf-8
# %load gen_code_languages.py
import yaml

with open('../languages.yml') as f:
    languages = yaml.load(f.read())
    
with open('README5.md', 'w') as f: 
    for k in languages.keys():
        if k in ['CoffeeScript', 'EmberScript', 'TSQL', 'GraphQL', 'ObjectScript', 'Erlang', 'Nearley', 'Shen', 'LiveScript', 'Mask', 'GDScript', 'Perl', 'P4', 'REXX', 'J', 'RobotFramework']:
            f.write('\n## ' + k + '\n### Results\n```' + k + '\n➜  all_the_single_ladies git:(master) ✗ python hack_single_ladies.py\n')
            f.write("\nA took a byte out of Gottfreid's sandwich, while he wasn't looking. Thank")
            f.write("\nGod I encrypted this, he'll never know the atrocities I committed, including stealing his")
            f.write("\nUDCTF{i'll_never_get_to_take_a_byte_out_of_a_jimmy_john's_sandwich_again_RIP_Jimmy_Johns} and stealing calculus.")
            f.write("\n```\n")
            
