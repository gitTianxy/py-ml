# coding=utf8
import numpy as np
import requests
import io
from PIL import Image

iris_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'


def index_by_group():
    r = requests.get(iris_url)
    iris = np.genfromtxt(io.StringIO(r.content.decode('utf8')), delimiter=',', dtype=np.object)
    np.random.seed(100)
    species_small = np.sort(np.random.choice(iris[:, 4].astype(np.str), size=20))
    print("array:", species_small)
    uniqs, counts = np.unique(species_small, return_counts=True)
    out = []
    for u in uniqs:
        grp = species_small[species_small == u]
        out.extend([i for i, val in enumerate(grp)])
    print("index by group:", out)


def one_hot_encoding():
    np.random.seed(101)
    arr = np.random.randint(1, 4, size=6)
    print("arr:", arr)
    uniqs = np.unique(arr)
    code_nums = np.array([2 ** (a - 1) for a in arr])
    mask = 1 << np.arange(len(uniqs))
    out = ((code_nums[:, None] & mask) > 0).astype(np.int)
    print("one-hot code:", out)


def id_by_group():
    r = requests.get(iris_url)
    iris = np.genfromtxt(io.StringIO(r.content.decode('utf8')), delimiter=',', dtype=np.object)
    np.random.seed(100)
    species_small = np.sort(np.random.choice(iris[:, 4].astype(np.str), size=20))
    print("array:", species_small)
    uniqs = np.unique(species_small)
    # full
    out = np.zeros(species_small.shape, dtype=np.int)
    for i, u in enumerate(uniqs):
        out[species_small == u] = i
    print(out)
    # reduced
    print([i for i, u in enumerate(uniqs) for val in species_small[species_small == u]])


def rank_index():
    np.random.seed(10)
    a = np.random.randint(20, size=10)
    print("array:", a)
    # from point-view of sorted array
    print("index in ori array for elements in sorted-array:", a.argsort())
    # from point-view of original array
    print("index in sorted array for elemens in ori-array:", a.argsort().argsort())


def get_max():
    np.random.seed(100)
    a = np.random.randint(1, 10, [5, 3])
    print("array:", a)
    # print(np.sort(a, axis=1)[:, -1])
    print(np.amax(a, axis=1))


def apply_along_axis():
    np.random.seed(100)
    a = np.random.randint(1, 10, [5, 3])
    print("array:", a)
    out = np.apply_along_axis(lambda x: np.min(x) / np.max(x), arr=a, axis=1)
    print("min/max:", out)


def uniq_positions():
    np.random.seed(100)
    a = np.random.randint(0, 5, 10)
    print('Array: ', a)
    out = np.full(a.shape, fill_value=True, dtype=np.bool)
    uniq_pos = np.unique(a, return_index=True)[1]
    out[uniq_pos] = False
    print(out)


def mean_by_group():
    r = requests.get(iris_url)
    iris = np.genfromtxt(io.BytesIO(r.content), delimiter=',', dtype=np.object)
    print(iris)
    species = iris[:, 4]
    sepalwidth = iris[:, 1].astype(np.float)
    species_uniq = np.unique(species)
    out = [(su, np.round(sepalwidth[species == su].mean(), decimals=4)) for su in species_uniq]
    print(out)


def img_array_conversion():
    url = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
    r = requests.get(url)
    # img 2 array
    img = Image.open(io.BytesIO(r.content))
    arr = np.asarray(img.resize([150, 150]))
    print(arr)
    # array 2 img
    im = Image.fromarray(arr)
    Image.Image.show(im)


if __name__ == '__main__':
    # one_hot_encoding()
    # index_by_group()
    # id_by_group()
    # rank_index()
    # get_max()
    # apply_along_axis()
    # uniq_positions()
    # mean_by_group()
    img_array_conversion()
