# coding: utf-8
# %load gen_code_languages.py
import yaml


codes = {
    "paths": """/login/param_name/param_value
/createTable/{table_name}/{column_name}/{column_type}
/edit/{table_name}/{param_name}/{param_value}
""",
    "params": """/login?param_name=param_value
/createTable/{table_name}?column_name=column_type
/edit/{table_name}?param_name=param_value
""",
    "statements": """login with: 'param_name=param_value'
edit entries: 'param_name=param_value'
""",
}

with open('languages.yml') as f:
    languages = yaml.full_load(f.read())

for name, code in codes.items():
    with open(f'{name.upper()}_SHORT_LIST.md', 'w') as f:
        for k in languages.keys():
            if k in ['CoffeeScript', 'EmberScript', 'TSQL', 'GraphQL', 'ObjectScript', 'Erlang', 'Nearley', 'Shen', 'LiveScript', 'Mask', 'GDScript', 'Perl', 'P4', 'REXX', 'J', 'RobotFramework']:
                f.write(f'\n## {k}\n```{k}\n{code}\n```')

    with open(f'{name.upper()}_FULL_LIST.md', 'w') as f:
        for k in languages.keys():
            f.write(f'\n## {k}\n```{k}\n{code}\n```')
