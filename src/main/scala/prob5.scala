import Math.pow

object Problem5 {

	// Googled for Common multipliers gives the method to find common prime multipliers
	// essentially, work out the factors of 2 -> 20, then account for each of the greater magnitudes
	// Multiply them all together to get the total.
	def solution = (pow(19,1)*pow(17,1)*pow(13,1)*pow(11,1)*pow(7,1)*pow(5,1)*pow(3,2)*pow(2,4)).toLong
}