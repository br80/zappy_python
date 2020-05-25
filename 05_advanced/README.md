### Nested loops

You can nest lists, dictionaries, and values together as deep as you like.

```python
alice =  {'name': 'alice', 'age': 21, 'height': 61, 'friends': ['bob', 'dan']}
bob = {'name': 'bob', 'age': 20, 'height': 64, 'friends': ['alice', 'charlie']}
charlie =  {'name': 'charlie', 'age': 21, 'height': 63, 'friends': ['bob']}
dan =  {'name': 'dan', 'age': 22, 'height': 66, 'friends': ['alice', 'bob']}

people = {'alice': alice, 'bob': bob, 'charlie': charlie, 'dan': dan}
# {
# 'alice': {'name': 'alice', 'age': 21, 'height': 61, 'friends': ['bob', 'dan']},
# 'bob': {'name': 'bob', 'age': 20, 'height': 64, 'friends': ['alice', 'charlie']},
# 'charlie': {'name': 'charlie', 'age': 21, 'height': 63, 'friends': ['bob']},
# 'dan': {'name': 'dan', 'age': 22, 'height': 66, 'friends': ['alice', 'bob']}
# }
```

You can run nested loops as well.

```python
for person in people:
    print(f'{person} is friends with:')
    for friend in people[person]['friends']:
        print(f'  {friend}')
# alice is friends with:
#   bob
#   dan
# bob is friends with:
#   alice
#   charlie
# charlie is friends with:
#   bob
# dan is friends with:
#   alice
#   bob
```


