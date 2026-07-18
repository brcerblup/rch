import matplotlib.pyplot as plt
import numpy as np
from math import fsum 

def visualisation(oy, sizes, alg_name, type_test, dataset_type): #type_test - массив {не отсортирован, отсортирован по возрастанию,
    plot, axes = plt.subplots(figsize=(8,5))                     #                  отсортирован по убыванию, отсортирован по модулю}
    axes.set_title(f'{alg_name} {dataset_type} {type_test}')     #dataset_type - алгоритм генерации датасета
    axes.set_xlabel("Размер массива, n")
    axes.set_xscale("log")
    axes.plot(sizes,oy)
    axes.grid(True)
    plot.tight_layout()
    plot.savefig(f'images/v/{alg_name}_{dataset_type}_{type_test}.png', dpi=300)
    plt.close(plot)
    
def visualisation3(oy1, oy2, oy3, sizes, alg_name1, alg_name2, alg_name3, type_test, dataset_type): #type_test - массив {не отсортирован, отсортирован по возрастанию,
    plot, axes = plt.subplots(figsize=(8,5))                                 #                  отсортирован по убыванию, отсортирован по модулю}
    axes.set_title(f'{dataset_type} {type_test}')                 #dataset_type - алгоритм генерации датасета
    axes.set_xlabel("Размер массива, n")
    axes.set_xscale("log")
    axes.plot(sizes,oy1, label = f'{alg_name1}')
    axes.plot(sizes,oy2, label = f'{alg_name2}')
    axes.plot(sizes,oy3, label = f'{alg_name3}')
    axes.grid(True)
    axes.legend(loc = "best")
    plot.tight_layout()
    plot.savefig(f'images/v3/{dataset_type}_{type_test}.png', dpi=300)
    plt.close(plot)

def visualisation4(oy1, oy2, oy3, oy4, sizes, var_name1, var_name2, var_name3, var_name4, type_test, dataset_type): #type_test - массив {не отсортирован, отсортирован по возрастанию,
    plot, axes = plt.subplots(figsize=(8,5))                                 #                  отсортирован по убыванию, отсортирован по модулю}
    axes.set_title(f'{dataset_type} {type_test}')                 #dataset_type - алгоритм генерации датасета
    axes.set_xlabel("Размер массива, n")
    axes.set_xscale("log")
    axes.plot(sizes,oy1, label = f'{var_name1}')
    axes.plot(sizes,oy2, label = f'{var_name2}')
    axes.plot(sizes,oy3, label = f'{var_name3}')
    axes.plot(sizes,oy4, label = f'{var_name4}')
    axes.grid(True)
    axes.legend(loc = "best")
    plot.tight_layout()
    plot.savefig(f'images/v4/{dataset_type}_{type_test}.png', dpi=300)
    plt.close(plot)

