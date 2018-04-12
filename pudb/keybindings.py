#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import bdb
import gc
import os
import sys
from functools import partial
from types import TracebackType

import urwid
from pudb.lowlevel import decode_lines
from pudb.py3compat import PY3, execfile, raw_input
from pudb.settings import load_config, save_config

__copyright__ = """
Copyright (C) 2009-2017 Andreas Kloeckner
Copyright (C) 2014-2017 Aaron Meurer
"""

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# Format: Cmd : keybind {str:str}

SOURCE_KEYBINDS = {
    'next': 'n',
    'step': 's',
    'finish': 'f',
    'finish': 'r',
    'cont': 'c',
    'run_to_cursor': 't',
    'move_down': 'j',
    'move_up': 'k',
    'page_down': 'ctrl d',
    'page_up': 'ctrl u',
    'page_down': 'ctrl f',
    'page_up': 'ctrl b',
    'scroll_left': 'h',
    'scroll_right': 'l',
    'search': '/',
    ',': 'search_previous',
    'search_next': '.',
    'move_home': 'home',
    'move_end': 'end',
    'move_home': 'g',
    'move_end': 'G',
    'go_to_line': 'L',
    'toggle_breakpoint': 'b',
    'pick_module': 'm',
    'move_stack_top': 'H',
    'move_stack_up': 'u',
    'move_stack_down': 'd',
}

CMDLINE_EDIT_KEYBINDS = {
    'cmdline_tab_complete': 'tab',
    'cmdline_append_newline': 'ctrl v',
    'cmdline_exec': 'enter',
    'cmdline_history_next': 'ctrl n',
    'cmdline_history_prev': 'ctrl p',
    'toggle_cmdline_focus': 'esc',
    'toggle_cmdline_focus': 'ctrl d',
    'cmdline_start_of_line': 'ctrl a',
    'cmdline_end_of_line': 'ctrl e',
    'cmdline_del_word': 'ctrl w',
    'cmdline_del_to_start_of_line': 'ctrl u',
}

CMDLINE_KEYBINDS = {
    'max_cmdline': '=',
    'grow_cmdline': '+',
    'min_cmdline': '_',
    'shrink_cmdline': '-',
}

# TODO rhs_col_sigwrap
RHS_COL_KEYBINDS = {
    'max_sidebar': '=',
    'grow_sidebar': '+',
    'min_sidebar': '_',
    'shrink_sidebar': '-',
}

# TODO top RHSColumnFocuser(x
TOP_KEYBINDS = {
    'toggle_cmdline_focus': 'ctrl x',
    'show_output': 'o',
    'reload_breakpoints': 'ctrl r',
    'run_cmdline': '!',
    'show_traceback': 'e',
    'focus_code': 'C',
    'RHColumnFocuser(0)': 'V',
    'RHColumnFocuser(1)': 'S',
    'RHColumnFocuser(2)': 'B',
    'quit': 'q',
    'do_edit_config': 'ctrl p',
    'redraw_screen': 'ctrl l',
    'help': 'f1',
    'help': '?',
}

CONTENT_KEYBINDS = {
    'enter': 'enter',
    'esc': 'esc',
}

# TODO var_list partials
VAR_LIST_KEYBINDS = {
    'change_var_state': '\\',
    'change_var_state': 't',
    'change_var_state': 'r',
    'change_var_state': 's',
    'change_var_state': 'c',
    'change_var_state': 'h',
    'change_var_state': '@',
    'change_var_state': '*',
    'change_var_state': 'w',
    'change_var_state': 'm',
    'edit_inspector_detail': 'enter',
    'insert_watch': 'n',
    'insert_watch': 'insert',
    partial(change_rhs_box, 'variables', 0, -1): '[',
    partial(change_rhs_box, 'variables', 0, 1): ']',
}

# TODO stack_list partials
STACK_LIST_KEYBINDS = {
    'examine_frame': 'enter',
    'move_stack_top': 'H',
    'move_stack_up': 'u',
    'move_stack_down': 'd',
    partial(change_rhs_box, 'stack', 1, -1): '[',
    partial(change_rhs_box, 'stack', 1, 1): ']',
}

# bp_list
BP_LIST_KEYBINDS = {
    'examine_breakpoint': 'enter',
    'delete_breakpoint': 'd',
    'save_breakpoints': 's',
    'enable_disable_breakpoint': 'e',
    partial(change_rhs_box, 'breakpoints', 2, -1): '[',
    partial(change_rhs_box, 'breakpoints', 2, 1): ']',
}

# vim: foldmethod=marker:expandtab:softtabstop=4
