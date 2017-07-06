object Problem6 {
	def sum_squares(r: Seq[Int]) = r.map(m => m*m).sum
	def square_sum(r: Seq[Int]) = {
		val total = r.sum
		total*total
	}
	val numbers = 1 to 100
	def solution = square_sum(numbers) - sum_squares(numbers)
}