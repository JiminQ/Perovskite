#' Produce fitted values
#'
#' @param krrm A model of type krr.
#'
#' @return Fitted values
#'
#' @export
fitted.krr <- function(krrm) krrm$pred

#' Produce residuals
#'
#' @param krrm A model of type krr.
#'
#' @return Residuals
#'
#' @export
resid.krr <- function(krrm) krrm$residuals

#' Compute MSE
#'
#' @param krrm A model of type krr.
#'
#' @return Fitted values
#'
#' @export
MSE <- function(x) UseMethod("MSE", x)
MSE.krr <- function(krrm) krrm$MSE

#' Produce fitted value plot.
#'
#' @param krrm A model of type krr.
#'
#' @return An aesthetic plot.
#'
#' @export
plot.krr <- function(krrm) {
  x <- as.matrix(krrm$x)
  p <- ncol(x)
  if(p != 1) {
    stop("ERROR: Can only plot univariate predictors!")
  }

  y <- krrm$pred - krrm$residuals
  df <- data.frame(x, y, yhat = krrm$pred)
  df <- df[order(df$x),]
  plot(df$x, df$y, pch = 16, xlab = "x", ylab = "y")
  lines(df$x, df$yhat, col = "red", lwd = 2)
}
