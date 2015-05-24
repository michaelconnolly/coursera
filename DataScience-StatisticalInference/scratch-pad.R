
nosim <- 1000
cfunc <- function(x, n) 2 * sqrt(n) * (mean(x) - 0.5) 
dat <- data.frame(
  x = c(apply(matrix(sample(0:1, nosim * 10, replace = TRUE), 
                     nosim), 1, cfunc, 10),
        apply(matrix(sample(0:1, nosim * 20, replace = TRUE), 
                     nosim), 1, cfunc, 20),
        apply(matrix(sample(0:1, nosim * 30, replace = TRUE), 
                     nosim), 1, cfunc, 30)
  ),
  size = factor(rep(c(10, 20, 30), rep(nosim, 3))))
g <- ggplot(dat, aes(x = x, fill = size)) + geom_histogram(binwidth=.3, colour = "black", aes(y = ..density..)) 
g <- g + stat_function(fun = dnorm, size = 2)
g + facet_grid(. ~ size)


n <- 10000; means <- cumsum(rnorm(n)) / (1  : n); library(ggplot2)
g <- ggplot(data.frame(x = 1 : n, y = means), aes(x = x, y = y)) 
g <- g + geom_hline(yintercept = 0) + geom_line(size = 2) 
g <- g + labs(x = "Number of obs", y = "Cumulative mean")
g

sample_size <- 40
lambda <- 0.2
sample1 <- rexp(sample_size, lambda)
sample1_mean = mean(sample1)
hist(sample1)


sample1_frame <- data.frame(x = 1 : sample_size, y = sample1)

graph_sample1 <- ggplot(sample1, aes(x=x, y=y)) + geom_point() 
graph_sample1

sample_means = NULL
sample_means_zero_based = NULL
sample_size <- 40
lambda <- 0.2
expected_mean <- 5.0
simulation_count <- 100000
for (i in 1 : simulation_count) {
  sample <- rexp(sample_size, lambda)
  sample_mean = mean(sample)
  sample_means_zero_based = c(sample_means_zero_based, (sample_mean - expected_mean))
  sample_means = c(sample_means, sample_mean)
}
hist(sample_means)
expected_variation <- expected_mean^2 / simulation_count
calculated_variation <- var(sample_means)
expected_variation
calculated_variation
expected_mean^2



sample_means = NULL
sample_size <- 40
lambda <- 0.2
expected_mean <- 5.0
simulation_count <- 1000
for (i in 1 : simulation_count) {
  sample <- rexp(sample_size, lambda)
  sample_mean = mean(sample)
  sample_means = c(sample_means, (sample_mean - expected_mean))
}
hist(sample_means)
v



df <- data.frame(sample1)

sample_means = NULL
sample_size <- 40
lambda <- 0.2
simulation_count <- 1000
for (i in 1 : simulation_count) {
  sample <- rexp(sample_size, lambda)
  sample_mean = mean(sample)
  sample_means = c(sample_means, sample_mean)
}
hist(sample_means)



sample_means = NULL
sample_means_zero_based = NULL
sample_size <- 40
lambda <- 0.2
variance <- (1 / (lambda^2))
expected_mean <- (1 / lambda)
standard_deviation <- sqrt(variance)
simulation_count <- 100000
for (i in 1 : simulation_count) {
  sample <- rexp(sample_size, lambda)
  sample_mean = mean(sample)
  sample_means_zero_based = c(sample_means_zero_based, (sample_mean - expected_mean))
  sample_means = c(sample_means, sample_mean)
}
hist(sample_means_zero_based)

expected_var_mean = variance / simulation_count
calculated_var_mean = var(sample_means)
expected_var_mean
calculated_var_mean


teeth <- ToothGrowth
group_oj <- teeth[teeth$supp=="OJ",]
group_vc <- teeth[teeth$supp=="VC",]
group_diff <- group_oj$len - group_vc$len
group_diff_mean <- mean(group_diff)
group_diff_sd <- sd(group_diff)
group_diff_count <- length(group_diff)
t.test(group_diff)
group_diff_mean + c(-1, 1) * qt(.975, group_diff_count - 1) * group_diff_sd / sqrt(group_diff_count)
