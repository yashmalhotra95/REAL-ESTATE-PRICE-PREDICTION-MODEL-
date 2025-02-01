## 4. Modelling and Evaluation

### 4.1 Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

mae_rf =[]
class RandomForestRegressor(
    n_estimators: Int = 100,
    *,
    criterion: Literal['squared_error', 'absolute_error', 'friedman_mse', 'poisson'] = "squared_error",
    max_depth: Int | None = None,
    min_samples_split: float | int = 2,
    min_samples_leaf: float | int = 1,
    min_weight_fraction_leaf: Float = 0,
    max_features: float | int | Literal['sqrt', 'log2'] = 1,
    max_leaf_nodes: Int | None = None,
    min_impurity_decrease: Float = 0,
    bootstrap: bool = True,
    oob_score: bool = False,
    n_jobs: Int | None = None,
    random_state: Int | None = None,
    verbose: Int = 0,
    warm_start: bool = False,
    ccp_alpha: float = 0,
    max_samples: float | int | None = None
)
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
class GradientBoostingRegressor(
    *,
    loss: Literal['squared_error', 'absolute_error', 'huber', 'quantile'] = "squared_error",
    learning_rate: Float = 0.1,
    n_estimators: Int = 100,
    subsample: Float = 1,
    criterion: Literal['friedman_mse', 'squared_error'] = "friedman_mse",
    min_samples_split: float | int = 2,
    min_samples_leaf: float | int = 1,
    min_weight_fraction_leaf: Float = 0,
    max_depth: int | None = 3,
    min_impurity_decrease: Float = 0,
    init: str | BaseEstimator | None = None,
    random_state: Int | None = None,
    max_features: float | int | Literal['auto', 'sqrt', 'log2'] | None = None,
    alpha: Float = 0.9,
    verbose: Int = 0,
    max_leaf_nodes: Int | None = None,
    warm_start: bool = False,
    validation_fraction: Float = 0.1,
    n_iter_no_change: Int | None = None,
    tol: Float = 0.0001,
    ccp_alpha: float = 0
)
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

import pickle
pickle.dump(model, open('REIT_gbr_model.sav', 'wb'))
