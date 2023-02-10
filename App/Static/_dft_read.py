def dft_read(
    nproc="8",
    ram="16",
    charge="0",
    multiplicity="1",
    basis="Basis-1",
    xyz="XYZ structure...",
):
    txt = f"""%NProcShared={nproc}
%mem={ram}gb
%chk=
#p b3lyp gen SCF=(xqc,Tight,intrep,NoVarAcc,Maxcycle=512) GFInput
     IOp(6/7=3) charge   iop(1/6=100)  symm=loose  int=(grid=ultrafine) scrf=(solvent=water)

test
{charge} {multiplicity}

{xyz}

{basis}
****
"""
    return txt
