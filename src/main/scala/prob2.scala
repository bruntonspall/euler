object Problem2 {
	lazy val fibs:Stream[Int] = 0 #:: 1 #:: fibs.zip(fibs.tail).map { case (a,b) => a + b }
	def solution = fibs.takeWhile(_ < 4000000).filter(_ % 2 == 1).sum
}