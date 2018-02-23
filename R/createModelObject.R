#' Kernel Ridge Regression
#'
#' A function for producing a krr (kernel ridge regression) model.
#'
#' @param x Quantitative explanatory variables (vector, matrix, or data.frame).
#' @param y Quantitative response variable.
#' @param lambda Tuning parameter for regression.
#' @param sigma Tuning parameter for Gaussian kernel.
#'
#' @return Returns the predictions, alphas, and MSE associated with the
#' regression, as well as the inputs x, y, the kernel function, and lambda.
#'
#' @export
krr <- function(x, y, lambda, sigma = 1) {

  if (is.numeric(x) & is.numeric(y)) {
    x <- as.matrix(x)
  }
  else {
    stop("Error: (x, y) must be numeric!")
  }

  n <- nrow(x)
  p <- ncol(x)

  if (length(y) != n) stop("Error: x and y of different lengths!")

  rbf <- kernlab::rbfdot(sigma = sigma)
  K <- kernlab::kernelMatrix(rbf, x)

  if (det(K + lambda*diag(n)) == 0) {
    stop("Error: Cannot invert matrix.  Choose larger lambda or smaller n")
  }
  else {
    alpha_hat <- solve(K + lambda*diag(n)) %*% y
  }

  f_hat <- K %*% alpha_hat
  
  residuals <- f_hat - y

  MSE <- mean((f_hat - y)^2)

  out <- list("pred" = f_hat,
              "alpha_hat" = alpha_hat,
              "lambda" = lambda,
              "ker" = rbf,
              "x" = x,
              "residuals" = residuals,
              "MSE" = MSE)
  
  class(out) <- "krr"
  
  return(out)
}

# TODO: Implement choices for kernel.
