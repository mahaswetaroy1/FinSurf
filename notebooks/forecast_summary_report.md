| Segment                | Target Variable   | Model Used   |             MAE |             RMSE | Notes                                           |
|:-----------------------|:------------------|:-------------|----------------:|-----------------:|:------------------------------------------------|
| All Data               | Total Repayment   | Prophet      |     8.13501e+07 |      8.17198e+07 | Full portfolio repayment forecast               |
| All Data               | Total Repayment   | Prophet      |     6.76116e+07 |      1.27602e+08 | Accuracy reported separately                    |
| All Data               | Churn Rate        | Prophet      |     0.1062      |      0.1624      | Applied Prophet to churn over time              |
| Long-term Sleepers     | Loan Volume       | Prophet      |     3.20326e+06 |      4.02852e+06 | Segment-level forecast                          |
| At-Risk Value Drainers | Loan Volume       | Prophet      |     1.12424e+07 |      1.39636e+07 | Segment-level forecast                          |
| High-Value Champions   | Loan Volume       | Prophet      |     1.77736e+07 |      2.17073e+07 | Segment-level forecast                          |
| Budget Loyalists       | Loan Volume       | Prophet      |     1.4186e+07  |    nan           | RMSE not reported                               |
| At-Risk Value Drainers | Loan Volume       | ARIMA        | 84524.5         | 108355           | ARIMA applied to this segment                   |
| All Segments           | Loan Volume       | ARIMA        |     1.70618e+07 |    nan           | Total ARIMA RMSE not available for all segments |