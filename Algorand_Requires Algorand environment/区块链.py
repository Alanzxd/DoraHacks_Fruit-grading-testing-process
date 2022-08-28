from pyteal import *
from pyteal.ast.bytes import Bytes
from pyteal_helpers import program

UINT64_MAX = 0xFFFFFFFFFFFFFFFF


def approval():
    # globals
    global_owner = Bytes("owner")  # byteslice
    global_counter = Bytes("counter")  # uint64

    op_good = Bytes("good")#good apple
    op_bad = Bytes("bad")#bad apple

    scratch_counter = ScratchVar(TealType.uint64)

    good = Seq(
        [
            scratch_counter.store(App.globalGet(global_counter)),
            # check overflow
            If(
                scratch_counter.load() < Int(UINT64_MAX),
                App.globalPut(global_counter, scratch_counter.load() + Int(2)),#good plus two
            ),
            Approve(),
        ]
    )

    bad = Seq(
        [
            scratch_counter.store(App.globalGet(global_counter)),
            # check underflow
            If(
                scratch_counter.load() > Int(0),
                App.globalPut(global_counter, scratch_counter.load() + Int(1)),#bad plus one
            ),
            Approve(),
        ]
    )

    return program.event(
        init=Seq(
            [
                App.globalPut(global_owner, Txn.sender()),
                App.globalPut(global_counter, Int(0)),
                Approve(),
            ]
        ),
        no_op=Cond(
            [Txn.application_args[0] == op_good, good],
            [Txn.application_args[0] == op_bad, bad],
        ),
    )


def clear():
    return Approve()
