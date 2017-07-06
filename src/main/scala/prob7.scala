import Problem3.isPrime

object Problem7 {
	def solution = 1 to 1000000 filter(n => isPrime(n)) drop 10000
}