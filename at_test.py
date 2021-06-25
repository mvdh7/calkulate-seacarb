import calkulate as calk, pandas as pd, numpy as np

analyte_density = calk.density.seawater_1atm_MP81(salinity=38, temperature=23.15736389)
analyte_mass = 25.753e-3 * ((1 - (0.0012013 / 8)) / (1 - (0.0012013 / analyte_density)))

read_dat_kwargs = dict(delimiter=",", skip_header=1)
ds = calk.Dataset(
    {
        "file_name": ["alkalinity.csv"],
        "file_path": ["data/"],
        "salinity": [38.0],
        "analyte_mass": [analyte_mass],
        "alkalinity_certified": [2193.19],
        "dic": [0.0],
        "total_borate": [0.0],
        "emf0_R": [405.221],
        "molinity_NaCl": 0,
    }
)
ds.calibrate(read_dat_kwargs=read_dat_kwargs)
ds["titrant_molinity"] = 0.1 / calk.density.HCl_NaCl_25C_DSC07()
ds.solve(read_dat_kwargs=read_dat_kwargs)
ds = pd.DataFrame(ds)
