import numpy as np
import math
import config as cfg
import dataset_generators as dg 
import algorithms as alg
import plots
import tests as t

algorithms = [
    ("naive", alg.naive_sum),
    ("kahan", alg.kahan_sum),
    ("pairwise", alg.pairwise_sum),
        ]

variations = [
    ("unsorted", lambda x: x),
    ("sorted", np.sort),
    ("reversed sort", lambda x: np.sort(x)[::-1]),
    ("abs sort", lambda x: x[np.argsort(np.abs(x))]),
        ]

datasets = [
    ("prandom", dg.prandom_nums),
    ("almost_cancellation", dg.almost_cancellation),
    ("cancellation", dg.cancellation),
    ("harmonic", dg.harmonic),
    ("diff_exp", dg.pizdec_raznye)
        ]
dop_infa = [
        "abs_error",
        "time",
        "rel_errors",
                    ]

#for algorithm_name, algorithm in algorithms: # csv формат
#    for dataset_type, dataset in datasets:
#        for variation_name, variation in variations:
#            np.savetxt(f'csv/{algorithm_name}_{dataset_type}_{variation_name}.csv',t.alg_test_raw(dataset, algorithm, 
#                                    variation),delimiter=',', newline='\n', header = "N,TRIAL,REFERENCE_RES,ERROR,TIMING")

#for algorithm_name, algorithm in algorithms:
#    for dataset_type, dataset in datasets:
#        for variation_name, variation in variations:
#            errors, timings, rel_errors, = t.alg_test(dataset, algorithm, variation)
#            dop_infa = [
#                (errors, "abs_error"),
#                (timings, "time"),
#                (rel_errors, "rel_errors"),
#                    ]
#            for inf_variation, inf_name in dop_infa:
#                plots.visualisation(inf_variation, cfg.sizes, algorithm_name, f'{variation_name}_{inf_name}',dataset_type)


#for dataset_name, dataset in datasets:
#    for variation_name, variation in variations:
#        oy1 = t.alg_test(dataset, alg.naive_sum, variation)
#        oy2 = t.alg_test(dataset, alg.kahan_sum, variation)
#        oy3 = t.alg_test(dataset, alg.pairwise_sum, variation)
#        dop_infa = ["abs_error", "time", "rel_errors",]
#        for i in range(3):
#            plots.visualisation3(oy1[i], oy2[i], oy3[i], cfg.sizes, "naive", "kahan", "pairwise", f'{variation_name}_{dop_infa[i]}' ,dataset_name)

for algorithm_name, algorithm in algorithms:
    for dataset_type, dataset in datasets:
        var_results = list()
        for variation_name, variation in variations:
                        var_results.append(t.alg_test(dataset, algorithm, variation))
        for l in range(3):
            plots.visualisation4(var_results[0][l], var_results[1][l], var_results[2][l], var_results[3][l], cfg.sizes, 
                                     variations[0][0], variations[1][0], variations[2][0], variations[3][0], 
                                     f'{algorithm_name}_{dop_infa[l]}',dataset_type)


