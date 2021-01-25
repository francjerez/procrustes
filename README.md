# Procrustes

A tiny, clean and heavily-commented NumPy-powered script originally designed to average facial landmarks. 

## Details

*Procrustes analysis* is a well known method for the multidimensional transformation (rescaling, translation, rotation and reflection) of individual data matrices, in order to provide optimal data blending and/or comparability. 

Due to its simplicity and flexibility, PA is a common sparsity approach for preventing overparameterization while training deep neural networks. 

Depending on where the reference shape comes from, PA can be qualified as *Ordinary Procrustes Analysis* (fixed shape) or *Generalized Procrustes Analysis* (mean shape). 

The `procrustes` module found in this repository implements both [OPA and GPA] algorithms (the former, in fact, being a subset of the latter). 

## Testing 

You can test the output by typing `python3 ./try.py`.

A two-part sequence of `matplotlib` charts, based on the fly wing example from [this](https://en.wikipedia.org/wiki/Procrustes_analysis) Wikipedia's article *infobox*, will appear.

In both cases, a root-mean-square deviation (RMSD) measure is shown in the window's title bar.

## Examples

OPA (the dimmed blue line is the starting position of the solid blue line):
![OPA](https://user-images.githubusercontent.com/3150023/105704314-ea4c9380-5f0e-11eb-92b1-095e162f810f.png)

GPA (the middle red line is the *mean shape*):
![GPA](https://user-images.githubusercontent.com/3150023/105704323-ecaeed80-5f0e-11eb-9fa2-1ba683dca69f.png)

## Dependencies

Procrustes requires `numpy` and, if you want to run the provided `try.py` test, `matplotlib` too:

```
$ python3 -m pip install --upgrade pip --user
$ pip3 install numpy
$ pip3 install matplotlib
```

## Go deep 

* 1975 - Generalized Procrustes Analysis (J.C. Gower)
* 1977 - The Diffusion of Shape (D.G. Kendall)
* 1991 - Procrustes Methods in the Statistical Analysis of Shape (Colin Goodall)
* 1998 - Statistical Shape Analysis (I. Dryden, K.V. Mardia)
* 2015 - Analyzing Fluctuating Asymmetry with Geometric Morphometrics (C.P. Klingenberg)

