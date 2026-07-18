import config as cfg
import math
from time import perf_counter
import numpy as np

def alg_test(dataset_generator, sum_alg, variation):
    errors = list()                                            #список для хранения ошибок

    timings = list()                                           #список для хранения среднего времени выполнения алгоритма

    rel_errors = list()                                        #список для хранения относительных ошибок
    
    for n in cfg.sizes:                     
        errors_tmp = list()                                    #временный массив для вычисления среднего значения 

        timings_tmp = list()                                   #временный массив для вычисление среднего значения

        rel_errors_tmp = list()                                #тоже самое шо и чуть выше

        for trial in range(cfg.seed_count):
            seed = n+trial                                     #генерация 50 неперекликающихся между собой сидов для каждого размера массива
            dataset = variation(dataset_generator(n, seed))    #генерация тестовых данных
            
            start = perf_counter()

            result = sum_alg(dataset)                          #вычисление результата с помощью тестируемого алгоритма
            
            timing = perf_counter() - start                    #вычисление времени выполнения

            reference_res = math.fsum(dataset)                 #вычисление референсного результата

            error = abs(reference_res-result)                  #вычисление абсолютной величины ошибки от референса
            errors_tmp.append(error)                           #добавление ошибки во временный лист для последующего вычисления среднего значения
            
            timings_tmp.append(timing)                         #добавление времени выполнения во временный массив
            
            if reference_res != 0 :
                rel_error = error/abs(reference_res)
                rel_errors_tmp.append(rel_error)



        mean_error = math.fsum(errors_tmp)/cfg.seed_count      #вычисляем среднее значение
        errors.append(mean_error)                                 #добавляем в список
        
        mean_timing = math.fsum(timings_tmp)/cfg.seed_count    #вычисляем среднее значение времени выполнения
        timings.append(mean_timing)                               #добавялем в список
        
        if len(rel_errors_tmp):
            mean_rel_error = math.fsum(rel_errors_tmp) / len(rel_errors_tmp)
            rel_errors.append(mean_rel_error)
        else:
            rel_errors.append(0)

    return errors, timings, rel_errors,

#def time_test(dataset_generator, sum_alg, sum_alg_name):
#    for n in cfg.sizes:
#        max_timing = 0
#        timings_trial = list()
#        for trial in range(cfg.seed_count):
#            seed = n+trial
#            dataset = dataset_generator(n,seed)
#            start = perf_counter()
#            sum_alg(dataset)
#            timing = perf_counter() - start
#            timings_trial.append(timing)
#            max_timing = max(max_timing, timing)
#        timings.append(math.fsum(timings_trial)/cfg.seed_count)
#        max_timings.append(max_timing)
#    return timings, max_timings
def alg_test_raw(dataset_generator, sum_alg, variation):
    results = list()
    for n in cfg.sizes:                     
        for trial in range(cfg.seed_count):
            seed = n+trial                                     #генерация 50 неперекликающихся между собой сидов для каждого размера массива
            dataset = variation(dataset_generator(n, seed))    #генерация тестовых данных
            
            start = perf_counter()

            result = sum_alg(dataset)                          #вычисление результата с помощью тестируемого алгоритма
            
            timing = perf_counter() - start                    #вычисление времени выполнения

            reference_res = math.fsum(dataset)                 #вычисление референсного результата

            error = abs(reference_res-result)                  #вычисление абсолютной величины ошибки от референса

            results.append([n, trial, reference_res, error, timing])

    return results

