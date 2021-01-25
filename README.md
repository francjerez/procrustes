# Procrustes

A tiny, clean and heavily-commented NumPy-powered script originally designed to average facial landmarks. 

## Details

The `procrustes` module implements both the *Ordinary Procrustes Analysis* and the *Generalized Procrustes Analysis* algorithms (the former, in fact, being a subset of the latter). 

You can test the output by typing `python3 ./try.py` (a two-part sequence of `matplotlib` charts, based on the fly wing example from [this](https://en.wikipedia.org/wiki/Procrustes_analysis) Wikipedia's article *infobox*, will appear).

OPA (the dimmed blue line is the starting position of the solid blue line):
![OPA](https://user-images.githubusercontent.com/3150023/105704314-ea4c9380-5f0e-11eb-92b1-095e162f810f.png)

GPA (the middle red line is the *mean shape*):
![GPA](https://user-images.githubusercontent.com/3150023/105704323-ecaeed80-5f0e-11eb-9fa2-1ba683dca69f.png)

In both cases, a root-mean-square deviation (RMSD) measure is shown in the window's title bar.

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

