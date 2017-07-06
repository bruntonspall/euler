object Problem9 {
	def coOccuringPairs(max:Int):List[Tuple2[Int,Int]] = 1 to (max-1) zip (1 to (max-1) reverse) take (max/2) toList

	def guess(left:Int, right:Int):Option[Tuple2[Int,Int]] = {
		if (right < 1) None
		else coOccuringPairs(left).map(p => (p._1*p._1, p._2*p._2)).filter(p => (p._1+p._2) == (right*right)) match {
			case Nil => guess(left+1, right-1)
			case a :: tail => Some(a)
		}
	}

	def startGuessing(max:Int) = {
		// start at max/2, since a2+b2=c2, c can't be more than total/2
		// Also the sum a+b
		guess(max/2, max/2)
	}
	def solution = startGuessing(1000)
		.map(p => (Math.sqrt(p._1),Math.sqrt(p._2)))
		.map(p => (p._1,p._2,(1000-(p._1+p._2))))
		.map(p => (p._1*p._2*p._3).toLong)
}