# TODO: indexed components:
#  local: generators, grid nodes, storages, stacks
#  global: generators, grid nodes, storages, stacks
#  transmission grids
#  zones

# TODO:
#  in central and local complexes there is something like interior energy demand (energetic cost of energy production)

# TODO:
#  base powers are per stack and (in case of local stacks) per zone
#  limits for p_min, p_max and max_p_incr, max_p_decr are not members of Unit based classes
#  power limits are per: zone and per whole system (local and central limits)
#  power ratio limits: min_peak2base, max_peak2base, min_stor2base, max_stor2base per stacks
#   - (for example if min_peak2base = m, then P_{peak} <= m*P_{base})
