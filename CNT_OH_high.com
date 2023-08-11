%NProcShared=8
%mem=16gb
%chk=CNT_OH_high
#p b3lyp gen SCF=(xqc,Tight,intrep,NoVarAcc,Maxcycle=512) GFInput
     IOp(6/7=3) symm=loose  int=(grid=ultrafine) scrf=(solvent=water) pop=(mk,nbo)

test

0 1
C      -1    29.67938     20.75327     36.64393
C      -1    25.38030     20.64917     36.67141
C      -1    27.51389     20.43864     32.97715
C      -1    31.63144     21.60882     30.48889
C      -1    33.18647     23.24899     36.60231
C      -1    34.84705     27.18475     36.52903
C      -1    34.32539     24.95374     30.42351
C      -1    21.63696     22.75769     36.66344
C      -1    23.31568     21.34099     30.52401
C      -1    20.25771     24.36599     30.48557
C      -1    26.80193     20.63348     36.66661
C      -1    33.83167     24.38079     29.21629
C      -1    28.92142     20.81096     35.44528
C      -1    26.82346     20.57632     34.20717
C      -1    32.56096     22.68511     30.47441
C      -1    33.81816     24.52401     36.58500
C      -1    28.90179     20.78205     32.97542
C      -1    30.89098     21.52036     36.64451
C      -1    24.75033     21.02172     35.45611
C      -1    26.80969     20.65808     31.75512
C      -1    30.90143     21.45707     29.27425
C      -1    26.80127     20.59997     29.30581
C      -1    24.70886     21.02424     30.53523
C      -1    22.84709     21.99351     36.67410
C      -1    20.15502     25.07848     29.24170
C      -1    30.91172     21.46503     31.71454
C      -1    21.24758     23.34325     30.50211
C      -1    32.56748     22.81133     35.39289
C      -1    33.82006     24.43794     31.65570
C      -1    34.49744     26.50725     35.32335
C      -1    34.52162     26.36200     30.39514
C      -1    22.83858     21.91685     31.73466
C      -1    22.84831     21.90985     29.30427
C      -1    27.51893     20.58706     35.44471
C      -1    33.07700     23.18111     29.23257
C      -1    21.33637     23.41278     35.43140
C      -1    20.19341     25.13773     31.69088
C      -1    29.60225     20.92286     34.20038
C      -1    25.42304     20.82314     34.21735
C      -1    27.50555     20.64087     30.53272
C      -1    29.61263     20.89529     31.74040
C      -1    29.59155     20.90673     29.28976
C      -1    25.41076     20.86475     31.75609
C      -1    31.50236     21.88014     35.41500
C      -1    25.40273     20.79664     29.30697
C      -1    19.76242     26.44402     29.20628
C      -1    33.01394     23.27651     31.68141
C      -1    23.43794     21.58189     35.44982
C      -1    34.63069     27.03255     29.15133
C      -1    34.11939     25.14188     35.34153
C      -1    19.84773     26.62123     36.58397
C      -1    21.73348     22.79755     29.28084
C      -1    21.76264     22.83644     31.73046
C      -1    28.91180     20.76447     30.51524
C      -1    31.51424     21.81241     32.94580
C      -1    30.88024     21.52200     34.18402
C      -1    24.72998     21.01299     32.99587
C      -1    23.40985     21.51263     32.98079
C      -1    33.03318     23.31542     34.15107
C      -1    20.26954     25.27681     36.61886
C      -1    19.78125     26.49272     31.66575
C      -1    34.16129     25.07549     32.88220
C      -1    21.75306     22.84422     34.20083
C      -1    20.55019     24.60320     35.40084
C      -1    19.85853     26.58387     34.13417
C      -1    32.55827     22.77300     32.93318
C      -1    22.85744     21.96574     34.20412
C      -1    34.66720     27.15992     34.06968
C      -1    34.64875     27.10123     31.61040
C      -1    20.48217     24.53261     32.94198
C      -1    33.78819     24.50490     34.12499
C      -1    21.30676     23.38349     32.96160
C      -1    20.29068     25.22964     34.15922
C      -1    34.52931     26.44029     32.85406
O      -1    30.20164     19.39132     36.60879
O      -1    25.05437     19.22498     36.65055
O      -1    27.61896     18.98973     32.89521
O      -1    32.45727     20.41817     30.42930
O      -1    34.38841     22.43389     36.58400
O      -1    36.29339     27.03856     36.45670
O      -1    35.68531     24.45465     30.38842
O      -1    20.62590     21.71792     36.65749
O      -1    22.69544     20.02600     30.52207
O      -1    19.02662     23.58873     30.51526
H      -1    28.14408     18.77389     32.08740
H      -1    32.96604     20.29391     31.27008
H      -1    35.12573     23.01867     36.37983
H      -1    36.49880     26.09142     36.24452
H      -1    35.86148     24.19350     29.48274
H      -1    20.19084     21.74455     35.79836
H      -1    23.38994     19.37867     30.35225
H      -1    18.32792     24.00154     29.95955

1-92 0
Choose Basis Set
****

