# coding: utf-8
import yaml

with open('../languages.yml') as f:
    languages = yaml.load(f.read())
    
with open('README3.md', 'w') as f: 
    for k in languages.keys():
        if k in ['GraphQL', 'ObjectScript', 'Erlang', 'Nearley', 'Shen', 'LiveScript', 'Mask', 'GDScript', 'Perl', 'P4', 'REXX', 'J', 'RobotFramework']:
            f.write('\n## ' + k + '\n```' + k + '\nUDCTF{0h_n0_y0u_d1dnt_just_3xt3nd_my_h4sh}\n```')
        
