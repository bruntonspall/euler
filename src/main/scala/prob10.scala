import Problem3._
object Problem10 {
	def solution = 1 to 1999999 filter(isPrime(_)) map(BigInt(_)) sum
}