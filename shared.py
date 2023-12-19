###
# |          Nom          | Matricule  |   CIP    |
# |:---------------------:|:----------:|:--------:|
# |   Alexandre Theisse   | 23 488 180 | thea1804 |
# | Louis-Vincent Capelli | 23 211 533 | capl1101 |
# |      Tom Sartori      | 23 222 497 | sart0701 |
###

import Gene
import Label


def get_all_genes_by_class(labels: [Label], genes: [Gene], cls: str) -> [[float]]:
    samples: [str] = Label.get_samples_by_class(labels, cls)
    return Gene.get_genes_by_samples(genes, samples)


def get_one_gene_by_class(labels: [Label], genes: [Gene], cls: str, gene_id: int) -> [float]:
    genes_by_class: [[float]] = get_all_genes_by_class(labels, genes, cls)
    return [gene[gene_id] for gene in genes_by_class]
