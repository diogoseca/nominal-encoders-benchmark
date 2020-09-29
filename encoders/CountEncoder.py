from measure import measure_encoder
from category_encoders import CountEncoder

class RobustCountEncoder:
    def __init__(self, cols=None):
        self.nominal_cols=cols
    
    def fit(self, X, y=None):
        self.encoder = CountEncoder(cols=self.nominal_cols).fit(X,y)
        return self

    def transform(self, X):
        X = self.encoder.transform(X)
        X = X.fillna(0)
        return X

measure_encoder(RobustCountEncoder, 'CountEncoder', save_results=True)