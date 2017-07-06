
object Problem1 {
  def solution = 1 to 999 filter(n => n % 3 == 0 || n % 5 == 0) sum
}

// vim: set ts=4 sw=4 et:
