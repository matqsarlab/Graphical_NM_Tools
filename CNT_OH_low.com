%NProcShared=8
%mem=16gb
%chk=CNT_OH_low
#p b3lyp gen SCF=(xqc,Tight,intrep,NoVarAcc,Maxcycle=512) GFInput
     IOp(6/7=3) symm=loose  int=(grid=ultrafine) scrf=(solvent=water) pop=(mk,nbo)

test

0 1
C      -1    -4.16384     -1.65755      2.77635
C      -1     2.12924     -2.59502      1.52267
C      -1    -3.41153     -1.80111      3.98466
C      -1     0.70586     -2.58477      1.52540
C      -1    -3.46258     -1.86255      1.54464
C      -1     2.74171     -2.17892      2.74228
C      -1     2.75121     -2.17377      0.30226
C      -1    -5.07251     -0.56097      2.77008
C      -1    -2.11670     -2.38378      3.98113
C      -1    -0.00890     -2.69186      2.74656
C      -1    -2.12942     -2.35844      1.53120
C      -1    -0.00884     -2.63760      0.29665
C      -1     2.08211     -2.40375      3.97312
C      -1    -1.41880     -2.51816      2.74956
C      -1     2.08625     -2.37996     -0.93686
C      -1    -4.06961     -1.49968      0.31645
C      -1     4.01590     -1.52613      0.30105
C      -1     4.00508     -1.50304      2.75112
C      -1    -5.54166     -0.02638      4.00196
C      -1     5.67927     -0.17285     -3.39965
C      -1    -5.57389     -0.03736      1.55199
C      -1     0.69235     -2.65383      3.97530
C      -1    -1.42547     -2.47129      0.29965
C      -1     4.63451     -1.12860     -3.39941
C      -1     0.68908     -2.62331     -0.93465
C      -1     4.60013     -1.11137      1.52070
C      -1    -5.13302     -0.57328      0.31017
C      -1     2.76603     -2.13293     -2.16770
C      -1     4.58740     -1.08603     -0.92924
C      -1     4.57453     -1.07484      3.98083
C      -1     4.05493     -1.54784     -2.16908
C      -1    -3.43363     -1.82103     -0.92535
C      -1     6.12294      0.36972     -2.16949
C      -1    -6.38358      1.17246     -3.36427
C      -1     7.14182      2.25392      3.98205
C      -1    -2.12064     -2.33913     -0.92879
C      -1    -6.27202      1.19189      4.01558
C      -1     7.18092      2.19212     -3.40816
C      -1    -6.31100      1.17353      1.55561
C      -1     5.64695     -0.14372     -0.93952
C      -1     2.08696     -2.33980     -3.39679
C      -1    -0.01284     -2.64722     -2.16337
C      -1     5.63682     -0.13477      1.52052
C      -1    -5.60545     -0.00815     -3.37791
C      -1    -5.60009     -0.02680     -0.90795
C      -1     6.93835      1.53402     -2.16891
C      -1     5.61190     -0.11236      3.98062
C      -1    -6.60121      1.81573      2.78734
C      -1    -1.42207     -2.48764     -2.16040
C      -1    -4.05412     -1.47296     -2.15354
C      -1    -5.12490     -0.53984     -2.14980
C      -1     6.89525      1.58620      2.76129
C      -1     6.08722      0.41519      2.75068
C      -1     6.10475      0.39952      0.29061
C      -1    -6.69463      1.80659     -2.13252
C      -1     0.69046     -2.59728     -3.39461
C      -1    -6.37151      1.16123     -0.90431
C      -1    -6.64086      1.81149      0.32740
C      -1     7.17415      2.22479      1.52193
C      -1    -3.42619     -1.77348     -3.38529
C      -1     6.92016      1.56382      0.29119
C      -1     7.19907      2.20239     -0.93817
C      -1    -2.11858     -2.32723     -3.38878
O      -1    -5.08674     -2.79170      2.84602
O      -1     2.38127     -4.02711      1.48957
H      -1    -5.99370     -2.46711      3.07834
H      -1     1.62232     -4.45878      1.07022

1-67 0
Choose Basis Set
****

