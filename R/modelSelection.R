#' Choose best lambda via cross-validation.
#'
#' A very crude method to find the optimal lambda for a krr (kernel ridge
#' regression) model.
#'
#' @param x Quantitative explanatory variables (vector, matrix, or data.frame).
#' @param y Quantitative response variable.
#' @param lambda_index Vector of lambdas to scan for best model.
#'
#' @return Returns best lambda, MSE, and model.  Also returns a dataframe of
#' every lambda_index value and corresponding MSE.
#'
#' @export
cv_krr <- function(x, y, lambda_index) {
  if(is.numeric(x) & is.numeric(y)) {
    x <- as.matrix(x)
    n <- nrow(x)
    p <- ncol(x)
  } else {
    warning("Error: (x, y) must be numeric!")
  }

  # Segment data
  test_n <- sample(1:n, round(0.4*n), replace = FALSE)
  x_train <- x[-test_n,]
  x_test <- x[test_n]
  y_train <- y[-test_n]
  y_test <- y[test_n]

  test_MSE <- function(lambda) {
    mod <- krr(x_train, y_train, lambda)
    MSE <- predict(mod, x_test, y_test)$MSE
    return(MSE)
  }

  MSE <- sapply(lambda_index, test_MSE)

  lambda_best_index <- which.min(MSE)
  lambda_best <- lambda_index[which.min(MSE)]

  model_best <- krr(x, y, lambda_best)
  MSE_best <- model_best$MSE

  index_out <- data.frame(lambda_index, MSE)

  return(list("lambda_best" = lambda_best,
         "MSE_best" = MSE_best,
         "index" = index_out,
         "model_best" = model_best))
}

# TODO: Turn this into actual kfold cross validation.
