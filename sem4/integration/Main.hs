import Debug.Trace
eps = 1.0e-7
a = 1
b = 2
f x = exp x / (1 + x ^ 2)
integrateTrapezoid n = h * sum ((f a + f b) / 2 : [f x | x <- [a + h, a + 2 * h .. b - h]]) where h = (b - a) / n
integrateSimpsons n = h / 3 * sum [f (x - h) + 4 * f x + f (x + h) | x <- [a + h, a + 3 * h .. b - h]] where h = (b - a) / n
runge i m n = traceShow (n, (b -a) / n, q1, q2, r) (if abs r < eps then q2 + r else runge i m (n * 2))
  where q1 = i n
        q2 = i (2 * n)
        r = (q2 - q1) / (2 ** m -1)
xs = [-0.861136311, 0.861136311, -0.339981043, 0.339981043]
p x = 2.5 * x ** 3 - 1.5 * x
c k = (1 - (xs !! k ** 2)) / (8 * (p (xs !! k) ** 2))
sub x = (a + b) / 2 + x * (b - a) / 2
gauss = (b - a) / 2 * sum [c i * f (sub (xs !! i)) | i <- [0 .. 3]]
main = do
  print gauss
  print $ runge integrateSimpsons  4 1
  print $ runge integrateTrapezoid 2 1
