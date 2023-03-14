def dft_read(
    nproc="8",
    ram="16",
    charge="0",
    multiplicity="1",
    basis="Basis-1",
    xyz="XYZ structure...",
    method="",
    pseudo="Pseudo Potential",
):
    n_line_xyz = len(xyz.split("\n"))
    if pseudo == "Pseudo Potential" or pseudo == "--":
        return f"""%NProcShared={nproc}
%mem={ram}gb
%chk=
{method}

test

{charge} {multiplicity}
{xyz}

1-{n_line_xyz} 0
{basis}
****

"""
    return f"""%NProcShared={nproc}
%mem={ram}gb
%chk=
{method}

test

{charge} {multiplicity}
{xyz}

1-{n_line_xyz} 0
{basis}
****

1-{n_line_xyz} 0
{pseudo}

"""


def dft_info(
    nproc="8",
    ram="16",
    name="",
    charge="0",
    multiplicity="1",
    basis1="Basis-1",
    basis2="Basis-2",
    method="",
):
    txt = f"""%NProcShared={nproc}
%mem={ram}gb
%chk={name}
{method}

test

{charge} {multiplicity}
-------------------------
{basis1}
****
{basis2}
****"""
    return txt


def dipole_info(
    nproc="8",
    ram="16",
    name="",
    charge="0",
    multiplicity="1",
    basis1="Basis-1",
    method="",
):
    txt = f"""%NProcShared={nproc}
%mem={ram}gb
%chk={name}
{method}

test

{charge} {multiplicity}
-------------------------
{basis1}
****"""
    return txt
