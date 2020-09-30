from django.shortcuts import render
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import r2_score



Districts= None
Area = None
Year = None


def Aman(request): 
     y_pred=''
     District = ''
     y_pre = ''
     Crop =''


     if request.method == 'POST':
          District = request.POST['Districts']
          Crop = request.POST['Crop']
          if Crop == 'Aman':
               dataset_Aman = pd.read_csv(r'/home/akhtar/Desktop/499B/Crop/Aman/Aman.csv')
               X = dataset_Aman.iloc[:, :-1]
               y = dataset_Aman.iloc[:, -1]
               X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

               regressor = RandomForestRegressor(n_estimators=20)
               regressor.fit(X_train, y_train)

               if District == 'Barishal' and Crop == 'Aman':
                    Max_Temp = 30.3414285714286
                    Humidity = 82.17
                    Rainfall = 19.8476190476191
                    Sunshine = 7.48571428571429
                    Altitude = 4
                    Wind_Speed = 0.364761904761905        
                    Districts = 1  
               elif District == 'Bogra' and Crop == 'Aman':
                    Max_Temp = 30.2813333333333
                    Humidity = 77.7266666666667
                    Rainfall = 7.69333333333334
                    Sunshine = 6.558
                    Altitude = 20
                    Wind_Speed = 0.835333333333333        
                    Districts = 2  
               elif District == 'Chittagong' and Crop == 'Aman':
                    Max_Temp = 30.5570362222222
                    Humidity = 75.5925913333333
                    Rainfall = 25.0370375555555
                    Sunshine = 7.9492
                    Altitude = 6
                    Wind_Speed = 1.49333337777778        
                    Districts = 3  
               elif District == 'Comilla' and Crop == 'Aman':
                    Max_Temp = 30.1111111111111
                    Humidity = 77.3962962962963
                    Rainfall = 17.862962962963
                    Sunshine = 7.24347923681257
                    Altitude = 10
                    Wind_Speed = 0.698888888888889        
                    Districts = 4  
               elif District == 'Dhaka' and Crop == 'Aman':
                    Max_Temp = 29.9481481481482
                    Humidity = 71.7111111111111
                    Rainfall = 15.8518518518519
                    Sunshine = 7.30703703703704
                    Altitude = 9
                    Wind_Speed = 0.584814814814815    
                    Districts = 5      
               elif District == 'Dinajpur' and Crop == 'Aman':
                    Max_Temp = 28.7044444444444
                    Humidity = 76.8259259259259
                    Rainfall = 7.76296296296297
                    Sunshine = 6.55524444444444
                    Altitude = 37
                    Wind_Speed = 0.615555555555555        
                    Districts = 6 
               elif District == 'Faridpur' and Crop == 'Aman':
                    Max_Temp = 29.4614814814815
                    Humidity = 77.162962962963
                    Rainfall = 15.9333333333333
                    Sunshine = 7.31463601532567
                    Altitude = 9
                    Wind_Speed = 0.736666666666667       
                    Districts = 7 

               elif District == 'Jessore' and Crop == 'Aman':
                    Max_Temp = 30.5118518518518
                    Humidity = 76.3407407407407
                    Rainfall = 17.2444444444444
                    Sunshine = 6.89444444444445
                    Altitude = 7
                    Wind_Speed = 0.896666666666667        
                    Districts = 8  
     
               elif District == 'Khulna' and Crop == 'Aman':
                    Max_Temp = 30.2855555555556
                    Humidity = 77.5259259259259
                    Rainfall = 15.7925925925926
                    Sunshine = 7.48881481481482
                    Altitude = 4
                    Wind_Speed = 0.648148148148148         
                    Districts = 9 
     
               # elif District == 'Mymensingh' and Crop == 'Aman':
               #      Max_Temp = 
               #      Humidity = 
               #      Rainfall =
               #      Sunshine =
               #      Altitude =
               #      Wind_Speed =         
               #      Districts = 10  
               elif District == 'Noakhali' and Crop == 'Aman':
                    Max_Temp = 29.8037037037037
                    Humidity = 78.0518518518519
                    Rainfall = 23.0888888888889
                    Sunshine = 7.30416347381865
                    Altitude = 6
                    Wind_Speed = 0.593333333333333       
                    Districts = 11  
               elif District == 'Pabna' and Crop == 'Aman':
                    Max_Temp = 29.6481481481481
                    Humidity = 75.6703703703704
                    Rainfall = 10.8518518518519
                    Sunshine = 7.02763729246488
                    Altitude = 14
                    Wind_Speed = 0.902222222222222       
                    Districts = 12  
               elif District == 'Patuakhali' and Crop == 'Aman':
                    Max_Temp = 30.2170731707317
                    Humidity = 79.2689180737961
                    Rainfall = 17.2726704190119
                    Sunshine = 6.84929913092234
                    Altitude = 3
                    Wind_Speed = 0.853252032520325       
                    Districts = 13  
               elif District == 'Rajshahi' and Crop == 'Aman':
                    Max_Temp = 29.3477777777778
                    Humidity = 76.4666666666667
                    Rainfall = 10.8814814814815
                    Sunshine = 7.3044126984127
                    Altitude = 20
                    Wind_Speed = 0.936666666666666       
                    Districts = 14
               elif District == 'Rangamati' and Crop == 'Aman':
                    Max_Temp = 30.2142857142857
                    Humidity = 79.7809523809524
                    Rainfall = 22.9047619047619
                    Sunshine = 7.46641975308642
                    Altitude = 63
                    Wind_Speed = 0.612380952380952       
                    Districts = 15
               elif District == 'Rangpur' and Crop == 'Aman':
                    Max_Temp = 28.4818518518519
                    Humidity = 81.5333333333333
                    Rainfall = 8.01481481481482
                    Sunshine = 7.02197883597884
                    Altitude = 34
                    Wind_Speed = 0.825925925925926        
                    Districts = 16 
               elif District == 'sylhet' and Crop == 'Aman':
                    Max_Temp = 29.9208230452675
                    Humidity = 75.2831275720165
                    Rainfall = 14.3958847736625
                    Sunshine = 7.83995884773662
                    Altitude = 35
                    Wind_Speed = 1.26609053497942        
                    Districts = 17
               elif District == 'Tangail' and Crop == 'Aman':
                    Max_Temp = 29.6549382716049
                    Humidity = 81.0679012345679
                    Rainfall = 14.5308641975309
                    Sunshine = 6.7858024691358
                    Altitude = 10
                    Wind_Speed = 0.764197530864197        
                    Districts = 18   
     

               Area = request.POST['Area']
               Year = request.POST['Year']
               y_pred = float(regressor.predict([[Districts, Area, Year, Max_Temp, Rainfall, Humidity, Wind_Speed, Sunshine, Altitude]]))      
               y_pr = regressor.predict(X_test)
               y_pre = int(r2_score(y_test, y_pr) * 100)

          elif Crop == 'Aus':

               dataset_Aman = pd.read_csv(r'/home/akhtar/Desktop/499B/Crop/Aus/Aus.csv')
               X = dataset_Aman.iloc[:, :-1]
               y = dataset_Aman.iloc[:, -1]
               X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

               regressor = RandomForestRegressor(n_estimators=20)
               regressor.fit(X_train, y_train)

               if District == 'Barishal' and Crop == 'Aus':
                    Max_Temp = 34.06714286
                    Humidity = 89.3428571428571
                    Rainfall = 392.357142857143
                    Sunshine = 3.95
                    Altitude = 4
                    Wind_Speed = 1.46428571428571     
                    Districts = 1  
               elif District == 'Bogra' and Crop == 'Aus':
                    Max_Temp = 35.2488888888889
                    Humidity = 85.6888888888889
                    Rainfall = 333.566666666667
                    Sunshine = 4.65222222222222
                    Altitude = 20
                    Wind_Speed = 1.52666666666667       
                    Districts = 2  
               elif District == 'Chittagong' and Crop == 'Aus':
                    Max_Temp = 33.7944444444445
                    Humidity = 85.9333333333333
                    Rainfall = 609.711111111111
                    Sunshine = 4.52666666666667
                    Altitude = 6
                    Wind_Speed = 4.31222222222222      
                    Districts = 3  
               elif District == 'Comilla' and Crop == 'Aus':
                    Max_Temp = 34.4744444444444
                    Humidity = 86.2
                    Rainfall = 357.5
                    Sunshine = 4.9
                    Altitude = 10
                    Wind_Speed = 2.33       
                    Districts = 4  
               elif District == 'Dhaka' and Crop == 'Aus':
                    Max_Temp = 34.28
                    Humidity = 83.7111111111111
                    Rainfall = 347.244444444444
                    Sunshine = 4.67111111111111
                    Altitude = 9
                    Wind_Speed = 1.55555555555556  
                    Districts = 5      
               elif District == 'Dinajpur' and Crop == 'Aus':
                    Max_Temp = 34.7311111111111
                    Humidity = 84.6555555555556
                    Rainfall = 392.733333333333
                    Sunshine = 4.748
                    Altitude = 37
                    Wind_Speed = 0.992222222222222     
                    Districts = 6 
               elif District == 'Faridpur' and Crop == 'Aus':
                    Max_Temp = 34.0922222222222
                    Humidity = 86.2666666666667
                    Rainfall = 320.266666666667
                    Sunshine = 4.69482758620689
                    Altitude = 9
                    Wind_Speed = 1.77      
                    Districts = 7 

               elif District == 'Jessore' and Crop == 'Aus':
                    Max_Temp = 35.04
                    Humidity = 86.5333333333333
                    Rainfall = 311.122222222222
                    Sunshine = 4.15555555555556
                    Altitude = 7 
                    Wind_Speed = 2.97888888888889      
                    Districts = 8  
     
               elif District == 'Khulna' and Crop == 'Aus':
                    Max_Temp = 34.7266666666667
                    Humidity = 87.3666666666667
                    Rainfall = 332.911111111111
                    Sunshine = 4.12666666666667
                    Altitude = 4
                    Wind_Speed = 1.64555555555556         
                    Districts = 9 
     
               elif District == 'Mymensingh' and Crop == 'Aus':
                    Max_Temp = 35.4416666666667
                    Humidity = 80.0606060606061
                    Rainfall = 284.522727272727
                    Sunshine = 5.72
                    Altitude = 19
                    Wind_Speed = 1.925        
                    Districts = 10  
               elif District == 'Noakhali' and Crop == 'Aus':
                    Max_Temp = 33.5544444444444
                    Humidity = 87.2666666666667
                    Rainfall = 667.7
                    Sunshine = 4.10862068965518
                    Altitude = 6
                    Wind_Speed = 1.82666666666667   
                    Districts = 11  
               elif District == 'Pabna' and Crop == 'Aus':
                    Max_Temp = 35.1244444444444
                    Humidity = 85.3444444444444
                    Rainfall = 284.144444444444
                    Sunshine = 4.63275862068966
                    Altitude = 14
                    Wind_Speed = 2.12777777777778      
                    Districts = 12  
               elif District == 'Patuakhali' and Crop == 'Aus':
                    Max_Temp = 33.640243902439
                    Humidity = 89.3461538461538
                    Rainfall = 491.679487179487
                    Sunshine = 3.37413793103449
                    Altitude = 3
                    Wind_Speed = 1.80365853658537    
                    Districts = 13  
               elif District == 'Rajshahi' and Crop == 'Aus':
                    Max_Temp = 35.15 
                    Humidity = 86.5444444444445
                    Rainfall = 291.722222222222
                    Sunshine = 4.74571428571429
                    Altitude = 20
                    Wind_Speed = 1.63444444444444     
                    Districts = 14
               elif District == 'Rangamati' and Crop == 'Aus':
                    Max_Temp = 34.6557142857143
                    Humidity = 85.2142857142857
                    Rainfall = 490.371428571429
                    Sunshine = 4.246296296
                    Altitude = 63
                    Wind_Speed = 1.20285714285714     
                    Districts = 15
               elif District == 'Rangpur' and Crop == 'Aus':
                    Max_Temp = 34.9955555555556
                    Humidity = 85.5555555555556
                    Rainfall = 414.666666666667
                    Sunshine = 4.74714285714286
                    Altitude = 34
                    Wind_Speed = 1.45444444444444       
                    Districts = 16 
               elif District == 'sylhet' and Crop == 'Aus':
                    Max_Temp = 35.2733333333333
                    Humidity = 86.8222222222222
                    Rainfall = 709.744444444444
                    Sunshine = 4.07666666666667
                    Altitude = 35
                    Wind_Speed = 1.48111111111111       
                    Districts = 17
               elif District == 'Tangail' and Crop == 'Aus':
                    Max_Temp = 34.7055555555555
                    Humidity = 85.537037037037
                    Rainfall = 293.814814814815 
                    Sunshine = 4.33333333333333
                    Altitude = 10
                    Wind_Speed = 1.65925925925926       
                    Districts = 18 

               Area = request.POST['Area']
               Year = request.POST['Year']
               y_pred = float(regressor.predict([[Districts, Area, Year, Max_Temp, Rainfall, Humidity, Wind_Speed, Sunshine, Altitude]]))      
               y_pr = regressor.predict(X_test)
               y_pre = int(r2_score(y_test, y_pr) * 100)

          elif Crop == 'Boro':

               dataset_Aman = pd.read_csv(r'/home/akhtar/Desktop/499B/Crop/Boro/Boro.csv')
               X = dataset_Aman.iloc[:, :-1]
               y = dataset_Aman.iloc[:, -1]
               X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

               regressor = RandomForestRegressor(n_estimators=20)
               regressor.fit(X_train, y_train)

               if District == 'Barishal' and Crop == 'Boro':
                    Max_Temp = 35.9352941176471
                    Humidity = 83.6176470588235
                    Rainfall = 236.147058823529
                    Sunshine = 6.26666666666667
                    Altitude = 4
                    Wind_Speed = 1.74411764705882       
                    Districts = 1  
               elif District == 'Bogra' and Crop == 'Boro':
                    Max_Temp = 37.5333333333333
                    Humidity = 76.8787878787879
                    Rainfall = 203.219696969697
                    Sunshine = 6.65
                    Altitude = 20
                    Wind_Speed = 1.74772727272727     
                    Districts = 2  
               elif District == 'Chittagong' and Crop == 'Boro':
                    Max_Temp = 34.7265151515152
                    Humidity = 80.43939394
                    Rainfall = 347.477272727273
                    Sunshine = 6.45833333333333
                    Altitude = 6
                    Wind_Speed =  4.0719696969697     
                    Districts = 3  
               elif District == 'Comilla' and Crop == 'Boro':
                    Max_Temp = 35.2621212121212
                    Humidity = 82.3863636363636
                    Rainfall = 267.227272727273
                    Sunshine = 6.43535353535354
                    Altitude = 10
                    Wind_Speed = 2.39848484848485       
                    Districts = 4  
               elif District == 'Dhaka' and Crop == 'Boro':
                    Max_Temp = 36.2325757575758
                    Humidity = 76.8484848484849
                    Rainfall = 261.280303030303
                    Sunshine = 6.59015151515152
                    Altitude = 9
                    Wind_Speed = 1.818181818
                    Districts = 5      
               elif District == 'Dinajpur' and Crop == 'Boro':
                    Max_Temp = 36.6727272727273
                    Humidity = 74.0909090909091
                    Rainfall = 206.856060606061
                    Sunshine = 6.5
                    Altitude = 37
                    Wind_Speed = 1.13863636363636      
                    Districts = 6 
               elif District == 'Faridpur' and Crop == 'Boro':
                    Max_Temp = 36.9
                    Humidity = 78.9242424242424
                    Rainfall = 232.416666666667
                    Sunshine = 6.68735632183908
                    Altitude = 9
                    Wind_Speed = 2.02045454545455      
                    Districts = 7 

               elif District == 'Jessore' and Crop == 'Boro':
                    Max_Temp = 38.1560606060606
                    Humidity = 76.5984848484848
                    Rainfall = 177.166666666667
                    Sunshine = 6.547727273
                    Altitude = 7
                    Wind_Speed = 3.73939393939394     
                    Districts = 8  
     
               elif District == 'Khulna' and Crop == 'Boro':
                    Max_Temp = 37.0401515151515
                    Humidity = 79.969696969697
                    Rainfall = 197.80303030303
                    Sunshine = 6.86222222222222
                    Altitude = 4
                    Wind_Speed = 1.9030303030303         
                    Districts = 9 
     
               elif District == 'Mymensingh' and Crop == 'Boro':
                    Max_Temp = 35.4416666666667
                    Humidity = 80.0606060606061
                    Rainfall = 284.522727272727 
                    Sunshine = 5.72
                    Altitude = 19
                    Wind_Speed = 1.925        
                    Districts = 10  
               elif District == 'Noakhali' and Crop == 'Boro':
                    Max_Temp = 35.2598484848485
                    Humidity = 81.6969696969697
                    Rainfall = 342.340909090909
                    Sunshine = 6.0632183908046
                    Altitude = 6
                    Wind_Speed = 1.79772727272727    
                    Districts = 11  
               elif District == 'Pabna' and Crop == 'Boro':
                    Max_Temp = 39.055303030303
                    Humidity = 73.780303030303
                    Rainfall = 178.333333333333
                    Sunshine = 6.87126436781609 
                    Altitude = 14
                    Wind_Speed = 2.4280303030303     
                    Districts = 12  
               elif District == 'Patuakhali' and Crop == 'Boro':
                    Max_Temp = 35.669918699187
                    Humidity = 83.4146341463415
                    Rainfall = 281.439024390244
                    Sunshine = 5.49195402298851
                    Altitude = 3 
                    Wind_Speed = 2.12845528455285     
                    Districts = 13  
               elif District == 'Rajshahi' and Crop == 'Boro':
                    Max_Temp = 38.9083333333333
                    Humidity = 73.7121212121212
                    Rainfall = 149.325757575758
                    Sunshine = 6.98571428571429
                    Altitude = 20
                    Wind_Speed = 1.86136363636364      
                    Districts = 14
               elif District == 'Rangamati' and Crop == 'Boro':
                    Max_Temp = 36.3383838383838
                    Humidity = 78.1313131313131
                    Rainfall = 311.131313131313 
                    Sunshine = 6.20123456790123
                    Altitude = 63
                    Wind_Speed = 1.35858585858586     
                    Districts = 15
               elif District == 'Rangpur' and Crop == 'Boro':
                    Max_Temp = 35.8734848484848
                    Humidity = 79.6893939393939
                    Rainfall = 268.151515151515
                    Sunshine = 6.23333333333333
                    Altitude = 34
                    Wind_Speed = 1.7030303030303      
                    Districts = 16 
               elif District == 'sylhet' and Crop == 'Boro':
                    Max_Temp = 35.175
                    Humidity = 81.2575757575758
                    Rainfall = 579.5
                    Sunshine = 5.43333333333333
                    Altitude = 35
                    Wind_Speed = 1.73409090909091      
                    Districts = 17
               elif District == 'Tangail' and Crop == 'Boro':
                    Max_Temp = 36.9370370370371 
                    Humidity = 79.2716049382716
                    Rainfall = 225.024691358025
                    Sunshine = 6.16296296296296
                    Altitude = 10
                    Wind_Speed = 1.81234567901235       
                    Districts = 18 

               Area = request.POST['Area']
               Year = request.POST['Year']
               y_pred = float(regressor.predict([[Districts, Area, Year, Max_Temp, Rainfall, Humidity, Wind_Speed, Sunshine, Altitude]]))      
               y_pr = regressor.predict(X_test)
               y_pre = int(r2_score(y_test, y_pr) * 100) 

          elif Crop == 'Jute':

               dataset_Aman = pd.read_csv(r'/home/akhtar/Desktop/499B/Crop/Jute/Jute.csv')
               X = dataset_Aman.iloc[:, :-1]
               y = dataset_Aman.iloc[:, -1]
               X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

               regressor = RandomForestRegressor(n_estimators=20)
               regressor.fit(X_train, y_train)

               if District == 'Barishal' and Crop == 'Jute':
                    Max_Temp = 35.8984848484848
                    Humidity = 81.6893939393939
                    Rainfall = 190.742424242424
                    Sunshine = 6.66666666666667
                    Altitude = 4
                    Wind_Speed = 1.59242424242424       
                    Districts = 1  
               elif District == 'Bogra' and Crop == 'Jute':
                    Max_Temp = 37.1668604651163
                    Humidity = 73.8720930232558
                    Rainfall = 157.616279069767
                    Sunshine = 7.08255813953489
                    Altitude = 20
                    Wind_Speed = 1.64186046511628       
                    Districts = 2  
               elif District == 'Chittagong' and Crop == 'Jute':
                    Max_Temp = 34.5604651162791
                    Humidity = 78.7093023255814
                    Rainfall = 274.197674418605
                    Sunshine = 6.85988372093024
                    Altitude = 6
                    Wind_Speed = 3.70872093023256     
                    Districts = 3  
               elif District == 'Comilla' and Crop == 'Jute':
                    Max_Temp = 35.0151162790698
                    Humidity = 80.7848837209302
                    Rainfall = 220.28488372093
                    Sunshine = 6.80454545454546
                    Altitude = 10
                    Wind_Speed = 2.16395348837209      
                    Districts = 4  
               elif District == 'Dhaka' and Crop == 'Jute':
                    Max_Temp = 36.2075581395349 
                    Humidity = 73.0988372093023
                    Rainfall = 210.052325581395
                    Sunshine = 6.97616279069767
                    Altitude = 9
                    Wind_Speed = 1.69360465116279   
                    Districts = 5      
               elif District == 'Dinajpur' and Crop == 'Jute':
                    Max_Temp = 36.4325581395349
                    Humidity = 70.703488372093
                    Rainfall = 159.023255813953
                    Sunshine = 6.894
                    Altitude = 37
                    Wind_Speed = 1.12383720930233     
                    Districts = 6 
               elif District == 'Faridpur' and Crop == 'Jute':
                    Max_Temp = 36.8354651162791
                    Humidity = 75.796511627907
                    Rainfall = 183.703488372093
                    Sunshine = 6.98534482758621
                    Altitude = 9
                    Wind_Speed = 1.90232558139535      
                    Districts = 7 

               elif District == 'Jessore' and Crop == 'Jute':
                    Max_Temp = 37.9511627906977
                    Humidity = 74.4011627906977
                    Rainfall = 145.029069767442
                    Sunshine = 6.8203488372093
                    Altitude = 7
                    Wind_Speed = 3.3906976744186     
                    Districts = 8  
     
               elif District == 'Khulna' and Crop == 'Jute':
                    Max_Temp = 36.9552325581395
                    Humidity = 77.7848837209302
                    Rainfall = 159.691860465116
                    Sunshine = 7.21583333333334
                    Altitude = 4
                    Wind_Speed = 1.78139534883721        
                    Districts = 9 
     
               elif District == 'Mymensingh' and Crop == 'Jute':
                    Max_Temp = 35.1933823529412
                    Humidity = 76.4779411764706
                    Rainfall = 224.808823529412
                    Sunshine = 6.06155462184874
                    Altitude = 19
                    Wind_Speed = 1.73455882352941        
                    Districts = 10  
               elif District == 'Noakhali' and Crop == 'Jute':
                    Max_Temp = 35.0654761904762
                    Humidity = 80.3214285714286
                    Rainfall = 274.065476190476 
                    Sunshine = 6.52222906403941 
                    Altitude = 6
                    Wind_Speed = 1.56309523809524   
                    Districts = 11  
               elif District == 'Pabna' and Crop == 'Jute':
                    Max_Temp = 38.5994047619048
                    Humidity = 70.8154761904762
                    Rainfall = 140.904761904762
                    Sunshine = 7.20260673234811
                    Altitude = 14
                    Wind_Speed = 2.13392857142857    
                    Districts = 12  
               elif District == 'Patuakhali' and Crop == 'Jute':
                    Max_Temp = 35.5611842105263
                    Humidity = 81.5249662618084
                    Rainfall = 214.242408906883
                    Sunshine = 6.0100499092559
                    Altitude = 3
                    Wind_Speed = 1.88355263157895     
                    Districts = 13  
               elif District == 'Rajshahi' and Crop == 'Jute':
                    Max_Temp = 38.5809523809524
                    Humidity = 70.75
                    Rainfall = 120.053571428571
                    Sunshine = 7.31215986394558
                    Altitude = 20
                    Wind_Speed = 1.66369047619048     
                    Districts = 14
               elif District == 'Rangamati' and Crop == 'Jute':
                    Max_Temp = 35.896875
                    Humidity = 75.65625
                    Rainfall = 259.458333333333
                    Sunshine = 6.61516203703704
                    Altitude = 63
                    Wind_Speed = 1.234375      
                    Districts = 15
               elif District == 'Rangpur' and Crop == 'Jute':
                    Max_Temp = 35.5178571428571
                    Humidity = 77.4464285714286
                    Rainfall = 208.791666666667
                    Sunshine = 6.63656462585034
                    Altitude = 34
                    Wind_Speed = 1.6125      
                    Districts = 16 
               elif District == 'sylhet' and Crop == 'Jute':
                    Max_Temp = 34.9446428571429
                    Humidity = 77.7797619047619
                    Rainfall = 468.119047619048
                    Sunshine = 5.96904761904762
                    Altitude = 35
                    Wind_Speed = 1.72797619047619       
                    Districts = 17
               elif District == 'Tangail' and Crop == 'Jute':
                    Max_Temp = 36.425
                    Humidity = 77.2222222222222
                    Rainfall = 188.402777777778
                    Sunshine = 6.58194444444444
                    Altitude = 10
                    Wind_Speed = 1.68888888888889       
                    Districts = 18

               Area = request.POST['Area']
               Year = request.POST['Year']
               y_pred = float(regressor.predict([[Districts, Area, Year, Max_Temp, Rainfall, Humidity, Wind_Speed, Sunshine, Altitude]]))      
               y_pr = regressor.predict(X_test)
               y_pre = int(r2_score(y_test, y_pr) * 100)



     return render(request, 'prediction.html', {'y_pred':y_pred, 'District':District, 'y_pre':y_pre, 'Crop':Crop})



