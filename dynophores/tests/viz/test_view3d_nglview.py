"""
Unit tests for dynophore.viz.view3d.nglview.

Will only test if viewer raises errors.
"""

from pathlib import Path

import pytest

from dynophores.viz import view3d

PATH_TEST_DATA = Path(__name__).parent / "dynophores" / "tests" / "data"


@pytest.mark.parametrize(
    "pml_path, pdb_path, dcd_path",
    [
        (
            PATH_TEST_DATA / "1KE7-1/DynophoreApp/1KE7-1_dynophore.pml",
            PATH_TEST_DATA / "1KE7-1/startframe.pdb",
            None,
        ),
        (
            PATH_TEST_DATA / "1KE7-1/DynophoreApp/1KE7-1_dynophore.pml",
            PATH_TEST_DATA / "1KE7-1/startframe.pdb",
            PATH_TEST_DATA / "1KE7-1/trajectory.dcd",
        ),
    ],
)
def test_show_dynophore3d(pml_path, pdb_path, dcd_path):
    view3d.show_dynophore3d(pml_path, pdb_path, dcd_path)