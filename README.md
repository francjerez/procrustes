# Procrustes

Procrustes is a tiny, clean and heavily-commented NumPy-powered script originally designed to average facial landmarks. 

## Details

The `procrustes` module implements both the *Ordinary Procrustes Analysis* and the *Generalized Procrustes Analysis* algorithms (the former, in fact, being a subset of the latter). 

You can test the output by typing `python3 ./try.py`. A two-part sequence of `matplotlib` charts, based on the fly wing example from [this](https://en.wikipedia.org/wiki/Procrustes_analysis) Wikipedia's article *infobox* (Klingenberg, 2015), will appear.

The OPA example (the dimmed blue line is the starting position):
![OPA](https://user-images.githubusercontent.com/3150023/105703649-da807f80-5f0d-11eb-84b8-4e3f53db0673.png)

The GPA example (the middle red line is the *mean shape*):
![GPA](https://user-images.githubusercontent.com/3150023/105703685-e5d3ab00-5f0d-11eb-80bf-00badf0fdfe8.png)

In both cases, a root-mean-square deviation (RMSD) measure is shown in the window's title bar.

## Dependencies

Procrustes requires `numpy` and, if you want to run the provided `try.py` test, `matplotlib` too:

```
$ python3 -m pip install --upgrade pip --user
$ pip3 install numpy
$ pip3 install matplotlib
```

## Go deep 

*1975 - Generalized Procrustes Analysis (J.C. Gower)
*1977 - The Diffusion of Shape (D.G. Kendall)
*1991 - Procrustes Methods in the Statistical Analysis of Shape (Colin Goodall)
*1998 - Statistical Shape Analysis (I. Dryden, K.V. Mardia) 			
*2015 - Analyzing Fluctuating Asymmetry with Geometric Morphometrics (C.P. Klingenberg)
*2020 - Walking on Kendall’s Shape Space (C.P. Klingenberg)
