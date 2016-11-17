#!/usr/bin/env python
# Adapted from pypairix and pysam
from setuptools import setup, find_packages, Extension

EXT_MODULES = [
    Extension("pairix",
        sources=[
            "bgzf.c", "bgzip.c", "index.c",
            "knetfile.c", "kstring.c",
            "python/pairixmodule.c"
        ],
        libraries=["z"],
        define_macros=[("_FILE_OFFSET_BITS", 64), ("_USE_KNETFILE", 1)]
    )
]

setup(
    name = "pypairix",
    version = "0.0.1",
    description = "Python interface for pairix",
    url = "https://github.com/4dn-dcic/pairix",
    author = "...",
    author_email = "...",
    license = "...",
    keywords = ["pairix","pairix", "bgzip", "bioinformatics", "genomics","hi-c"],
    packages = find_packages(),
    package_data = { "": ["*.gz", "*.gz.px2"] },
    ext_modules = EXT_MODULES,
    test_suite = "test",
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    long_description = """\
April 16, 2014

This module allows fast random access to files compressed with bgzip_ and
indexed by pairix_. It includes a C extension with code from klib_. The bgzip
and pairix programs are available here_.


Installation
------------

::

    pip install --user pypairix


Synopsis
--------

Genomics data is often in a table where each row corresponds to a genomic
region (start, end) or a position:


::

    chrom  pos      snp
    1      1000760  rs75316104
    1      1000894  rs114006445
    1      1000910  rs79750022
    1      1001177  rs4970401
    1      1001256  rs78650406


With pairix_, you can quickly retrieve all rows in a genomic region by
specifying a query with a sequence name, start, and end:


::

    import pairix

    # Open a remote or local file.
    url = "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20100804/"
    url += "ALL.2of4intersection.20100804.genotypes.vcf.gz"

    tb = pairix.open(url)

    # These 1D queries are identical. A query returns an iterator over the results.
    records = tb.query("1", 1000000, 1250000)
    records = tb.queryi(0, 1000000, 1250000)
    records = tb.querys("1:1000000-1250000")

    # Each record is a list of strings.
    for record in records:
        print record[:5]
        break


::

    ['1', '1000071', '.', 'C', 'T']


.. _bgzip: http://samtools.sourceforge.net/pairix.shtml
.. _pairix: http://samtools.sourceforge.net/pairix.shtml
.. _klib: https://github.com/jmarshall/klib
.. _here: http://sourceforge.net/projects/samtools/files/pairix/

"""
)