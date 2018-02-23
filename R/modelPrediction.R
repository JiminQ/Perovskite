#' Predict new krr outcomes.
#'
#' A function for making predictions based on a krr (kernel ridge regression)
#' model.
#'
#' @param krr_mod A model produced by the \code{krr} function
#' @param xnew New quantitative explanatory variables to predict (vector,
#' matrix, or data.frame).
#' @param ynew Optional new response variables, helps compute MSE.
#'
#' @return Predicted values and MSE.
#'
#' @export
predict.krr <- function(krr_mod, xnew, ynew = NULL) {
  xnew <- as.matrix(xnew)
  nnew <- nrow(xnew)
  pnew <- ncol(xnew)
  x <- krr_mod$x
  n <- nrow(x)

  ker <- krr_mod$ker

  K_tilde <- kernlab::kernelMatrix(ker, xnew, x)

  f_tilde <- K_tilde %*% krr_mod$alpha_hat

  if (!is.null(ynew)) {
    MSE <- mean((f_tilde - ynew)^2)
    return(list(
      'pred' = f_tilde,
      'MSE' = MSE
    ))
  } else {
    return(f_tilde)
  }
}
