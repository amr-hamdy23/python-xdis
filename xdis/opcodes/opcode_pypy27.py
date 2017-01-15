# (C) Copyright 2017 by Rocky Bernstein
"""
CPython PYPY 2.7 bytecode opcodes

This is a like Python 2.7's opcode.py with some classification
of stack usage.
"""

import xdis.opcodes.opcode_27 as opcode_27
from xdis.opcodes.base import (
    def_op, finalize_opcodes, init_opdata,
    jrel_op, name_op, varargs_op
    )

l = locals()

init_opdata(l, opcode_27, 2.7, is_pypy=True)

# PyPy only
# ----------
name_op(l,    'LOOKUP_METHOD',   201,  1, 2)
varargs_op(l, 'CALL_METHOD',     202, -1, 1)
l['hasnargs'].append(202)

# Used only in single-mode compilation list-comprehension generators
def_op(l, 'BUILD_LIST_FROM_ARG', 203)

# Used only in assert statements
jrel_op(l, 'JUMP_IF_NOT_DEBUG',     204)

# There are no opcodes to remove or change.
# If there were, they'd be listed below.

# FIXME remove (fix uncompyle6)
def updateGlobal():
    globals().update({'PJIF': l['opmap']['POP_JUMP_IF_FALSE']})
    globals().update({'PJIT': l['opmap']['POP_JUMP_IF_TRUE']})

updateGlobal()

finalize_opcodes(l)
