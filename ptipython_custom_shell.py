"""
This file shows how you can define a custom shell for PuDB. This is the
shell used when pressing the ! key in the debugger (it does not affect the
Ctrl-x shell that is built into PuDB).

To create a custom shell, create a file like this one with a function called
pudb_shell(_globals, _locals) defined at the module level. Note
that the file will be execfile'd.

Then, go to the PuDB preferences window (type Ctrl-p inside of PuDB) and add
the path to the file in the "Custom" field under the "Shell" heading.

The example in this file

"""


# Define this a function with this name and signature at the module level.
def pudb_shell(_globals, _locals) -> None:
    """
    This example shell runs a classic Python shell. It is based on
    run_classic_shell in pudb.shell.

    """
    # Many shells only let you pass in a single locals dictionary, rather than
    # separate globals and locals dictionaries. In this case, you can use
    # pudb.shell.SetPropagatingDict to automatically merge the two into a
    # single dictionary. It does this in such a way that assignments propogate
    # to _locals, so that when the debugger is at the module level, variables
    # can be reassigned in the shell.
    import os.path
    from ptpython.ipython import embed
    from ptpython.repl import run_config

    history_filename = os.path.expanduser('~/.config/ptpython/history')

    embed(
        globals=_globals,
        locals=_locals,
        history_filename=history_filename,
        configure=run_config,
    )
