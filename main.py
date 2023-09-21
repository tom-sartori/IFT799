from Gene import Gene
from Label import Label
from read_data import get_labels, get_genes


if __name__ == '__main__':
    labels: [Label] = get_labels()
    print(labels[0].sample)

    genes: [Gene] = get_genes()
    print(genes[0].sample)
