import Gene
import Label


def get_genes_by_class(labels: [Label], genes: [Gene], cls: str) -> [[float]]:
    samples: [str] = Label.get_samples_by_class(labels, cls)
    return Gene.get_genes_by_samples(genes, samples)
