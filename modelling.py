## 4. Modelling and Evaluation

### 4.1 Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

mae_rf =[]

for i in np.arange(5,40,2):
    model = RandomForestRegressor(max_depth=i, random_state=0)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae_rf.append(mean_absolute_error(y_test, y_pred))

plt.plot(np.arange(5,40,2),mae_rf)
print("MAE for Random Forest Regressor Model is: ",min(mae_rf))
# MAE for Random Forest Regressor Model is:  44040.613428818644
model_rf = RandomForestRegressor(max_depth=23, random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(mean_absolute_error(y_test, y_pred))
# 44161.07739361702

### 4.2 Gradient Boosting Regressor

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
mae_gbr = []
locx = []
locy = []
for i in range(1,10):
    for j in np.arange(0.05,0.51,0.05):
        gbr_model = GradientBoostingRegressor(learning_rate=j, max_depth=i)
        scores = cross_val_score(gbr_model, X_train, y_train, cv=5, scoring="neg_median_absolute_error")
        cv_mae = abs(sum(scores)/len(scores))
        mae_gbr.append(cv_mae)
        locx.append(i)
        locy.append(j)

#model = GradientBoostingRegressor(learning_rate=j, max_depth=i)
#y_pred = model.predict(X_test)

print ("MAE for Gradient Boosting Regressor Model is: ",min(mae_gbr),"\nat max depth of",locx[(mae_gbr.index(min(mae_gbr)))],"and learning rate of :",locy[(mae_gbr.index(min(mae_gbr)))])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(locx, locy, mae_gbr)
# MAE for Gradient Boosting Regressor Model is:  32343.175234815622 at max depth of 5 and learning rate of : 0.1
<mpl_toolkits.mplot3d.art3d.Path3DCollection at 0x7b2e047a9720>

from sklearn.metrics import mean_absolute_error

gbr_model = GradientBoostingRegressor(learning_rate=0.1, max_depth=5).fit(X_train, y_train)
y_pred = gbr_model.predict(X_test)
gbr_mae_scores = mean_absolute_error(y_test, y_pred)
print(gbr_mae_scores)
# 45210.36523987265
