import scala.annotation.tailrec
import math._
object Problem3 {
	@tailrec
	def factors(max: Long, n: Long = 2, acc: List[Long] = Nil):List[Long] = 
	     if (max/2 < n) acc
	     else if (max % n == 0) factors(max, n+1, n :: acc)
	     else factors(max, n+1, acc)

	def findDivisor(max:Long, test:Long):Long = 
		if (sqrt(max) < test) max
		else if (max % test == 0) test
		else findDivisor(max, test+1)

	def smallestDivisor(n: Long) = findDivisor(n, 2)

	def isPrime(n:Long):Boolean = 
	if (n == 1) false 
	else smallestDivisor(n) == n

	def primeFactors(n:Long) = factors(n).filter(isPrime)

	def solution = primeFactors(600851475143L)
}