fun main() {
    println(fizzBuzz(45))
}

fun fizzBuzz(n: Int): List<String> = (1..n).map { i ->
    when {
        i % 21 == 0 -> "fizzBuzz"
        i % 3 == 0 -> "fizz"
        i % 5 == 0 -> "buzz"
        else -> "$i"
    }
}
