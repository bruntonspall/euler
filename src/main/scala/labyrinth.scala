case class Coord(x: Int, y: Int)
trait Node {
	val coord: Coord
}

case class DeadEnd(coord: Coord) extends Node
case class Passage(next: Node, coord: Coord) extends Node
case class Fork(left: Node, right: Node, coord: Coord) extends Node

object Labyrinth {
	val labyrinth = 
	Fork(
		Fork(
			DeadEnd(Coord(1,3)),
			DeadEnd(Coord(3,3)), 
			Coord(2,2)),
		Passage(
			Fork(
				Passage(
					DeadEnd(Coord(3,5)),
					Coord(3,4)),
				DeadEnd(Coord(5,4)),
				Coord(4,3)),
			Coord(4,2)),
		Coord(3,1))

	def turnRight(f: Option[Node]):Option[Node] = f match {
		case Some(Fork(_, right, _)) => Some(right)
		case _ => None
	}

	def turnLeft(f: Node):Option[Node] = f match {
		case Fork(left, _, _) => Some(left)
		case _ => None
	}

	def keepStraightOn(f:Node):Option[Node] = f match {
		case Passage(n, _) => Some(n)
		case _ => None
	}
}