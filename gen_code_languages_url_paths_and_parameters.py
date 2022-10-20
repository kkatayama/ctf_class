# coding: utf-8
# %load gen_code_languages.py
import yaml


code = """/login/param_name/param_value
/login/param_name=param_value
login with: 'param_name=param_value'
/createTable/{table_name}/{column_name}/{column_type}
/createTable/{table_name}?column_name=column_type
/edit/{table_name}/{param_name}/{param_value}
/edit/{table_name}?param_name=param_value
/edit/{table_name}/filter/{filter_string}
/edit/{table_name}?filter=filter_string
edit entries: 'param_name=param_value'
"""

with open('languages.yml') as f:
    languages = yaml.full_load(f.read())
    
with open('README6.md', 'w') as f:
    for k in languages.keys():
        if k in ['CoffeeScript', 'EmberScript', 'TSQL', 'GraphQL', 'ObjectScript', 'Erlang', 'Nearley', 'Shen', 'LiveScript', 'Mask', 'GDScript', 'Perl', 'P4', 'REXX', 'J', 'RobotFramework']:
            f.write(f'\n## {k} + \n```{k}\n{code}\n```')
