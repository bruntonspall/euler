object Problem4 {
	def isPalindrome(n:Long):Boolean = {
		val s = n.toString
		s.reverse == s
	}

	def solution = 999 to (100,-1) combinations(2) filter { case Vector(a,b) => Problem4.isPalindrome(a*b) } map { case Vector(a,b) => a*b } max
}