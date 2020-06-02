# modcell example

This repository is an example of notebooks using [modcell](https://github.com/wsuzume/modcell).

## Usage
### Construct virtual environment

```
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Activate modcell

In order to activate modcell, run

```python
import modcell

# for short form I recommend mods
import modcell as mods
```

at the head of the notebook. And now you can import IPython notebook, which extension is `.ipynb`.
`modcell` only imports cells which has

```
# modcell
```

comment at the head of the cell.

### Tagging
`modcell` supports selective import using tag. The syntax

```
# modcell: tagname
```

can be used for defining a tag. If you use `import` to import other notebooks, `modcell` imports `# modcell` cells if it has tagname or not.

To import only tagged cells, use following syntax.

```
# import only tagged cells
modname = mods._import('module_notebook', tag='tagname')
```

Which has almost the same meaning as

```
# import all cells which has '# modcell' comment
import module_notebook as modname
```

the former code imports only tagged but the latter one imports all.

### Compile
`modcell` can export cells which are read. You can generate multiple instances of modcell like

```
import modcell as mods

mod_1 = mods.ModCell()
mod_2 = mods.ModCell()
...
```

and you can import cells to the ModCell instances.

```
modname = mod_1._import('module_notebook')
```

And `compile` method exports imported cells to a file.

```
import modcell as mods

mod_debug = mods.ModCell()
nb1_debug = mod_debug._import('notebook_1', tag='debug')
nb2 = mod_debug._import('notebook_2')
nb3 = mod_debug._import('notebook_3')
with open('../module/mod_debug.py', mode='w') as f:
    mod_debug.compile(out=f)

mod_test = mods.ModCell()
nb1_test = mod_test._import('notebook_1', tag='test')
nb4 = mod_test._import('notebook_4')
with open('../module/mod_test.py', mode='w') as f:
    mod_test.compile(out=f)
```
